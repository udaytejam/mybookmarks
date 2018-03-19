from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, flash
from logging import DEBUG

from forms import BookmarkForm

app = Flask(__name__)
#app.logger.setLevel(DEBUG)
app.config['SECRET_KEY'] = '\xdb\xa3\x1ciV\x8a\xa43\x93\x995\xda[\x1b5\xbc\x08g\x8fCI4\x0f\xa0'

bookmarks = []
#using global bookmarks as a variable to store data. Database to follow.
def store_bookmark(url, description):
    bookmarks.append(dict(
        url = url,
        description = description,
        user = 'uday',
        date = datetime.utcnow()
    ))

def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks = new_bookmarks(5))

@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        #url = request.form['url']  #getting data from 'form' dictionary(works with request reference)
        store_bookmark(url, description)
        flash('Bookmark saved: {}'.format(description))
        #app.logger.debug('stored url:' + url)
        return redirect(url_for('index'))
    return render_template('add.html', form = form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__=='__main__':
    app.run(debug=True)