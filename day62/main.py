from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
file_csv = "C:\\github\\100_days_of_code_python\\day62\\cafe-data.csv"
# {{ wtf.quick_form(form) }}


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    url = StringField(
        'Cafe Location on Google Maps (URL)',
        validators=[DataRequired(), URL()])
    open_time = StringField('Opening Time', validators=[DataRequired()])
    closing_time = StringField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField(
        'Coffee Rating', validators=[DataRequired()], choices=[
            ("0", "✘"),
            ("1", "☕️"),
            ("2", "☕️☕️"),
            ("3", "☕️☕️☕️"),
            ("4", "☕️☕️☕️☕️"),
            ("5", "☕️☕️☕️☕️☕️")
        ], validate_choice=True)
    wifi_rating = SelectField(
        'WiFi Rating', validators=[DataRequired()], choices=[
            ("0", "✘"),
            ("1", "🔌"),
            ("2", "🔌🔌"),
            ("3", "🔌🔌🔌"),
            ("4", "🔌🔌🔌🔌"),
            ("5", "🔌🔌🔌🔌🔌")
        ], validate_choice=True)
    power_rating = SelectField(
        'Power Rating', validators=[DataRequired()], choices=[
            ("0", "✘"),
            ("1", "💪"),
            ("2", "💪💪"),
            ("3", "💪💪💪"),
            ("4", "💪💪💪💪"),
            ("5", "💪💪💪💪💪")
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
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True\n\n")
        # print(form.cafe.data)

        linha = []
        for item in form:
            if item.name == "coffee_rating":
                if int(item.data) == 0:
                    rating = "✘"
                else:
                    rating = "☕️" * int(item.data)
                linha.append(rating)
            elif item.name == "wifi_rating":
                if int(item.data) == 0:
                    rating = "✘"
                else:
                    rating = "🔌" * int(item.data)
                linha.append(rating)
            elif item.name == "power_rating":
                if int(item.data) == 0:
                    rating = "✘"
                else:
                    rating = "💪" * int(item.data)
                linha.append(rating)
            else:
                linha.append(item.data)

        # print(linha[:7])

        with open(
                file_csv, mode="a", newline='\n', encoding="utf8") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(linha[:7])

        return redirect(url_for('cafes'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open(file_csv, newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:

            list_of_rows.append(row)

        # print('\n\n')
        # print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
