from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect
from logging import DEBUG

app = Flask(__name__)
app.logger.setLevel(DEBUG)

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
    return render_template('index.html', title = {'firstname': 'Ivan', 'lastname': 'Pavlov'}, description = 'Future and Ed collaborated.')

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url)
        app.logger.debug('stored url:' + url)
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