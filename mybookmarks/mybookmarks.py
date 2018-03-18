from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, flash
from logging import DEBUG

app = Flask(__name__)
#app.logger.setLevel(DEBUG)
app.config['SECRET_KEY'] = '\xdb\xa3\x1ciV\x8a\xa43\x93\x995\xda[\x1b5\xbc\x08g\x8fCI4\x0f\xa0'

bookmarks = []
#using global bookmarks as a variable to store data. Database to follow.
def store_bookmark(url):
    bookmarks.append(dict(
        url = url,
        user = 'uday',
        date = datetime.utcnow()
    ))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = {'firstname': 'Ivan', 'lastname': 'Pavlov'},
                           description = 'Future and Ed collaborated.')

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url)
        flash('Bookmark saved: {}'.format(url))
        #app.logger.debug('stored url:' + url)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__=='__main__':
    app.run(debug=True)