from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreateProductForm, RegisterForm, LoginForm, CommentForm
from flask_gravatar import Gravatar
from functools import wraps
from flask import abort
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# CONNECT TO DB
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)


gravatar = Gravatar(app, size=100, rating='g', default='retro',
                    force_default=False, force_lower=False, use_ssl=False,
                    base_url=None)

# CONFIGURE TABLES


# Create the User Table
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

    # This will act like a List of BlogPost objects attached to each User.
    # The "author" refers to the author property in the BlogPost class.
    products = relationship("StoreProduct", back_populates="author")

    # *******Add parent relationship*******#
    # "comment_author" refers to the comment_author property in the Comment class.
    comments = relationship("Comment", back_populates="comment_author")


class StoreProduct(db.Model):
    __tablename__ = "store_products"
    id = db.Column(db.Integer, primary_key=True)

    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # Create reference to the User object, the "posts" refers to the posts protperty in the User class.
    author = relationship("User", back_populates="products")

    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    price = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    # ***************Parent Relationship*************#
    comments = relationship("Comment", back_populates="parent_product")


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    # *******Add child relationship*******#
    # "users.id" The users refers to the tablename of the Users class.
    # "comments" refers to the comments property in the User class.
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")

    # ***************Child Relationship*************#
    product_id = db.Column(db.Integer, db.ForeignKey("store_products.id"))
    parent_product = relationship("StoreProduct", back_populates="comments")


# Create all the tables in the database
# db.create_all()

carrinho = []
soma_carrinho = 0

# Create admin-only decorator


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def get_all_products():
    products = StoreProduct.query.all()
    return render_template("index.html", all_products=products, current_user=current_user, carrinho=carrinho)

@app.route('/empty_cart')
def empty_cart():
    global carrinho
    carrinho = []
    return redirect(url_for("get_all_products"))


@app.route('/carrinho')
def get_carrinho():
    soma_carrinho = 0

    for item in carrinho:
        soma_carrinho += float(item['product'].price) * item['quantity']

    soma_carrinho = round(soma_carrinho, 2)
    soma_carrinho = f"{soma_carrinho:.2f}"

    return render_template("carrinho.html", soma=soma_carrinho, current_user=current_user, carrinho=carrinho)


@app.route('/register', methods=["GET", "POST"])
def register():
    # Register new users into the User database
    form = RegisterForm()
    if form.validate_on_submit():

        # If user's email already exists
        if User.query.filter_by(email=form.email.data).first():
            # Send flash messsage
            flash("You've already signed up with that email, log in instead!")
            # Redirect to /login route.
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=hash_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()

        # This line will authenticate the user with Flask-Login
        login_user(new_user)

        return redirect(url_for("get_all_products"))

    return render_template("register.html", form=form, current_user=current_user, carrinho=carrinho)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        # Email doesn't exist
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        # Password incorrect
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('get_all_products'))

    return render_template("login.html", form=form, current_user=current_user, carrinho=carrinho)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_products'))


@app.route("/product/<int:product_id>", methods=["GET", "POST"])
def show_product(product_id):
    form = CommentForm()
    requested_product = StoreProduct.query.get(product_id)

    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login"))

        new_comment = Comment(
            text=form.comment_text.data,
            comment_author=current_user,
            parent_product=requested_product
        )
        db.session.add(new_comment)
        db.session.commit()

    return render_template("product.html", product=requested_product, current_user=current_user, form=form, carrinho=carrinho)


@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user, carrinho=carrinho)


@app.route("/contact")
def contact():
    return render_template("contact.html", current_user=current_user, carrinho=carrinho)


@app.route("/checkout")
def checkout():
    soma_carrinho = 0

    for item in carrinho:
        soma_carrinho += float(item['product'].price) * item['quantity']

    soma_carrinho = round(soma_carrinho, 2)
    soma_carrinho = f"{soma_carrinho:.2f}"

    return render_template("checkout.html", soma=soma_carrinho, current_user=current_user, carrinho=carrinho)


@app.route("/new-product", methods=["GET", "POST"])
# Mark with decorator
@admin_only
def add_new_product():
    form = CreateProductForm()
    if form.validate_on_submit():
        price_product = float(form.price.data)
        price = f"{price_product:.2f}"
        new_product = StoreProduct(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            price=price,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for("get_all_products"))
    return render_template("make-product.html", form=form, current_user=current_user, carrinho=carrinho)


@app.route("/edit-product/<int:product_id>", methods=["GET", "POST"])
@admin_only
def edit_product(product_id):
    product = StoreProduct.query.get(product_id)
    edit_form = CreateProductForm(
        title=product.title,
        subtitle=product.subtitle,
        img_url=product.img_url,
        price=product.price,
        author=current_user,
        body=product.body
    )
    if edit_form.validate_on_submit():

        price_product = float(edit_form.price.data)
        price = f"{price_product:.2f}"

        product.title = edit_form.title.data
        product.subtitle = edit_form.subtitle.data
        product.img_url = edit_form.img_url.data
        product.price = price
        product.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_product", product_id=product.id))

    return render_template("make-product.html", form=edit_form, is_edit=True, current_user=current_user, carrinho=carrinho)


@app.route("/delete/<int:product_id>")
@admin_only
def delete_product(product_id):
    product_to_delete = StoreProduct.query.get(product_id)
    db.session.delete(product_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_products'))


@app.route("/delete_from_card/<int:product_id>")
@admin_only
def delete_product_from_cart(product_id):
    product_to_delete = StoreProduct.query.get(product_id)

    for produto in carrinho:
        if product_to_delete.id == produto['product'].id:
            carrinho.remove(produto)
            print(carrinho)

            return redirect(url_for('get_carrinho'))

    print(carrinho)
    return redirect(url_for('get_carrinho'))


@app.route("/add_to_card/<int:product_id>")
@admin_only
def add_product_to_card(product_id):
    product_to_add = StoreProduct.query.get(product_id)

    for produto in carrinho:
        if product_to_add.id == produto['product'].id:
            produto['quantity'] += 1
            total_price = float(product_to_add.price) * produto['quantity']
            total_price = round(total_price, 2)
            produto['total_price'] = total_price
            print(produto['quantity'])
            print(carrinho)
            return redirect(url_for('get_all_products'))

    cart = {
        'product': product_to_add,
        'quantity': 1,
        'total_price': product_to_add.price,
    }

    carrinho.append(cart)

    print(carrinho)

    return redirect(url_for('get_all_products'))


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5000, debug=True)
