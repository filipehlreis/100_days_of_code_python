
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from flask import redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TodoList Configuration
class Todolist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250), nullable=False)
    status = db.Column(db.String(250), nullable=False)
    date_add = db.Column(db.String(250), nullable=False)
    date_done = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same
        #  thing.
        # return {column.name: getattr(self, column.name) for column in
        # self.__table__.columns}


class TodoListForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired()])
    status = SelectField(
        'Task Status?', validators=[DataRequired()], choices=[
            ("Não iniciado", "Não iniciado"),
            ("Pendente", "Pendente"),
            ("Em progresso", "Em progresso"),
            ("Concluido", "Concluido"),
        ], validate_choice=True)

    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating,
# power outlet rating fielrereasdfds
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_todo_task():
    form = TodoListForm()
    if form.validate_on_submit():
        print("True\n\n")

        date_now = datetime.now()

        todotask = Todolist(
            task=request.form.get("task"),
            status=request.form.get("status"),
            date_add=date_now.date(),
            date_done=date_now.date()
        )

        db.session.add(todotask)
        db.session.commit()

        return redirect(url_for('get_all_todolist'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route("/todolist")
def get_all_todolist():
    todolist_tasks = db.session.query(Todolist).all()
    # This uses a List Comprehension but you could also split it into 3 lines.
    list_of_rows = []
    for task in todolist_tasks:
        list_of_rows.append(task)

    return render_template('todolist.html', tasks=list_of_rows)


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:task_id>")
def delete_task(task_id):
    task = db.session.query(Todolist).get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()

    return redirect(url_for('get_all_todolist'))


@app.route("/edit", methods=["GET", "POST"])
def edit_task():
    task_id = request.args.get('task_id')
    task_selected = Todolist.query.get(task_id)

    form = TodoListForm(obj=task_selected)
    form.populate_obj(task_selected)

    if form.validate_on_submit():
        print("True\n\n")

        date_now = datetime.now()

        task_id_form = task_id
        print(f"'{task_id}' tem algo?")
        task_to_update = Todolist.query.get(task_id_form)
        print(form.task.data)
        task_to_update.task = form.task.data
        task_to_update.status = form.status.data
        task_to_update.date_done = date_now.date()

        db.session.commit()

        return redirect(url_for('get_all_todolist'))

    return render_template("edit.html", task=task_selected, form=form)


if __name__ == '__main__':
    app.run(debug=True)
