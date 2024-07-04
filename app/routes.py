from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from app import db
from app.models import User, Book
from app.forms import RegistrationForm, LoginForm, BookForm
from app.utils import generate_book_content
import json

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)
book = Blueprint('book', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('main.index'))

@book.route('/create_book', methods=['GET', 'POST'])
@login_required
def create_book():
    form = BookForm()
    if form.validate_on_submit():
        book_content = generate_book_content(form.title.data)
        new_book = Book(title=form.title.data, content=json.dumps(book_content), author=current_user)
        db.session.add(new_book)
        db.session.commit()
        flash('Book created successfully!', 'success')
        return redirect(url_for('book.view_book', book_id=new_book.id))
    return render_template('create_book.html', form=form)

@book.route('/my_books')
@login_required
def my_books():
    books = current_user.books.all()
    return render_template('my_books.html', books=books)

@book.route('/book/<int:book_id>')
@login_required
def view_book(book_id):
    book = Book.query.get_or_404(book_id)
    if book.author != current_user:
        flash('You do not have permission to view this book.', 'error')
        return redirect(url_for('book.my_books'))
    content = json.loads(book.content)
    return render_template('view_book.html', book=book, content=content)
