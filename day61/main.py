from flask_bootstrap import Bootstrap
from wtforms import PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf import FlaskForm
from flask import Flask, render_template


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[
                       DataRequired(), Email(check_deliverability=True)])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


email_check = "admin@email.com"
password_check = "123456789"

app = Flask(__name__)
app.secret_key = "gdfio2t80945g45r09h8gre09873408yt"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == email_check and \
                login_form.password.data == password_check:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
