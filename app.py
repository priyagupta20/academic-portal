from flask import Flask, render_template, request, redirect, url_for, flash, abort, session, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/news1')
def news1():
    return render_template('news1.html')

@app.route('/news2')
def news2():
    return render_template('news2.html')

@app.route('/news3')
def news3():
    return render_template('news3.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login_student')
def login_student():
    return render_template('login_student.html')

@app.route('/login_teacher')
def login_teacher():
    return render_template('login_teacher.html')

@app.route('/student_dashboard')
def student_dashboard():
    return render_template('student_dashboard.html')

@app.route('/upload_content')
def upload_content():
    return render_template('upload_content.html')

@app.route('/view_content')
def view_content():
    return render_template('view_content.html')

@app.route('/view_submission')
def view_submission():
    return render_template('view_submission.html')
