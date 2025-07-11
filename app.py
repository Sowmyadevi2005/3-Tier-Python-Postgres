from flask import Flask, render_template, request, redirect, url_for
from models import db, Author, Book
import config

app = Flask(__name__)
app.config.from_object(config.Config)
db.init_app(app)

@app.route('/')
def index():
    books = Book.query.all()
    authors = Author.query.all()
    return render_template('index.html', books=books, authors=authors)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        author_id = request.form['author_id']
        new_book = Book(title=title, genre=genre, author_id=author_id)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('index'))
    authors = Author.query.all()
    return render_template('add_book.html', authors=authors)

@app.route('/edit_book/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    book = Book.query.get_or_404(id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.genre = request.form['genre']
        book.author_id = request.form['author_id']
        db.session.commit()
        return redirect(url_for('index'))
    authors = Author.query.all()
    return render_template('edit_book.html', book=book, authors=authors)

@app.route('/delete_book/<int:id>')
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        name = request.form['name']
        new_author = Author(name=name)
        db.session.add(new_author)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_author.html')

@app.route('/edit_author/<int:id>', methods=['GET', 'POST'])
def edit_author(id):
    author = Author.query.get_or_404(id)
    if request.method == 'POST':
        author.name = request.form['name']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_author.html', author=author)

@app.route('/delete_author/<int:id>')
def delete_author(id):
    author = Author.query.get_or_404(id)
    db.session.delete(author)
    db.session.commit()
    return redirect(url_for('index'))

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

