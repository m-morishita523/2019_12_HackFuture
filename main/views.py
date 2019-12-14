import flask 
from main import app
from main.models import Entry, EnglishArchive
from main import db
from main.function import jp2en_transrator
import requests
import glob

@app.route('/')
def show_images():
    images_data = []
    img_path = 'img/*'
    img_path_list = glob.glob(img_path)
    for path in img_path_list:
        item = {'image': path, 'area': 'dammy'}
        # item['image'] = path
        # item['area'] = 'dammy'
        images_data.append(item)

    return flask.render_template('index.html', images_data = images_data)



# @app.route('/')
# def show_entries():
#     entries = Entry.query.all()

#     return flask.render_template('index.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    entry = Entry(
        title = flask.request.form['title'],
        text = flask.request.form['text']
    )
    db.session.add(entry)
    db.session.commit()

    return flask.redirect(flask.url_for('show_entries'))

@app.route('/archives.html')
def show_archives():
    archives = EnglishArchive.query.all()

    return flask.render_template('archives.html', archives=archives)


@app.route('/add_archive', methods=['POST'])
def add_archive():
    archive = EnglishArchive(
        shopname = flask.request.form['shopname'],
        description = flask.request.form['description']
    )

    # result_shopname = requests.get('https://script.google.com/macros/s/AKfycbxjITyi5QlS-NhSAzg6BRQbiWPSK05qnOF1DYl9H_FC_4tzlOM/exec?text=' + archive.shopname + '&source=ja&target=en')
    # result_shopname.encoding
    archive.shopname = jp2en_transrator(archive.shopname)
    archive.description = jp2en_transrator(archive.description)

    db.session.add(archive)
    db.session.commit()

    return flask.redirect(flask.url_for('show_archives'))