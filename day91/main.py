import cv2 as cv
from flask import Flask, render_template, request
from flask import redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField
from werkzeug.utils import secure_filename
from sklearn.cluster import KMeans
import numpy as np

n_clusters = 10

image_name = "default.jpg"
FILE_DIR = "day91\\static"


def get_pallete(FILENAME, n_clusters=5):
    def palette(clusters):
        width = 300
        palette = np.zeros((50, width, 3), np.uint8)
        steps = width/clusters.cluster_centers_.shape[0]
        for idx, centers in enumerate(clusters.cluster_centers_):
            palette[:, int(idx*steps):(int((idx+1)*steps)), :] = centers
        return palette

    img_2 = cv.imread(FILENAME)
    img_2 = cv.resize(img_2, (100, 100))
    img_2 = cv.cvtColor(img_2, cv.COLOR_BGR2RGB)

    clt_3 = KMeans(n_clusters)
    clt_3.fit(img_2.reshape(-1, 3))

    pallete_lista = np.ndarray.tolist(palette(clt_3))

    pallete_lista_final = []
    for x in pallete_lista[0]:
        if x not in pallete_lista_final:
            pallete_lista_final.append(x)

    img_palette_hex = [
        ('#%02x%02x%02x' % tuple(color)).upper()
        for color in pallete_lista_final
    ]

    return img_palette_hex


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class ImageColorGeneratteForm(FlaskForm):
    image = FileField('Image File')
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    global image_name
    image_name = "default.jpg"

    return render_template("index.html")


@app.route("/imgcolorpallete", methods=["GET", "POST"])
def get_imgcolorpallete():
    global image_name, n_clusters
    form = ImageColorGeneratteForm()

    if request.method == "POST":
        if form.validate_on_submit():
            f = form.image.data
            image_name = secure_filename(f.filename)
            filename = f"{FILE_DIR}\\{image_name}"
            img_palette = get_pallete(filename, n_clusters)

            return render_template(
                'imgcolorpallete.html',
                img_pallete=img_palette,
                img_url=image_name,
                form=form)

    filename = f"{FILE_DIR}\\{image_name}"
    img_palette = get_pallete(filename, n_clusters)

    return render_template(
        'imgcolorpallete.html',
        img_pallete=img_palette,
        img_url=image_name,
        form=form)


@app.route('/get_image', methods=["GET", "POST"])
def get_image():
    global image_name
    form = ImageColorGeneratteForm()

    if form.validate_on_submit():
        image_name = secure_filename(form.image.data.filename)
        return redirect(url_for('get_imgcolorpallete'))

    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
