from flask import Flask, render_template, send_file, request, redirect, url_for
from werkzeug import secure_filename
import base64
import smtplib


app = Flask(__name__)

UPLOAD_FOLDER = '/where you want uploaded books to go'
app.config['/where you want uploaded books to go'] = UPLOAD_FOLDER

#Each of the below methods are genres

# Python Books
@app.route('/python/', methods=['POST'])
def python():

    bookName = request.form['book']
    return send_file('static/books/python/' + bookName + '.pdf', attachment_filename = bookName + '.pdf')


# Lisp Books
@app.route('/lisp/', methods=['POST'])
def lisp():

    bookName = request.form['book']
    return send_file('static/books/lisp/' + bookName + '.pdf', attachment_filename = bookName + '.pdf')

# C++ Books
@app.route('/c++/', methods=['POST'])
def cPlus():

    bookName = request.form['book']
    return send_file('static/books/c++/' + bookName + '.pdf', attachment_filename = bookName + '.pdf')

# C Books
@app.route('/c/', methods=['POST'])
def c():

    bookName = request.form['book']
    return send_file('static/books/c/' + bookName + '.pdf', attachment_filename = bookName + '.pdf')

# Raspberry pi and Arduino Books
@app.route('/raspberryPiArduino/', methods=['POST'])
def raspberryPiArduino():

    bookName = request.form['book']
    return send_file('static/books/raspberryPiArduino/' + bookName + '.pdf', attachment_filename = bookName + '.pdf')


# Security Books
@app.route('/security/', methods=['POST'])
def security():

    bookName = request.form['book']
    return send_file('static/books/security/' + bookName + '.pdf', attachment_filename = bookName + '.pdf')

# upload and email notifier
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():

    if request.files['file'].filename == '':
        return 'No file uploaded...'

    if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))



      # Send an email notifying that a new book has been placed
      smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
      smtpObj.ehlo()
      smtpObj.starttls()

      # add email and password
      smtpObj.login(' yourMail@mail.com ', ' yourPassword ')

      # send a message from your email to yourself (or any person) to notify the new book
      smtpObj.sendmail(' yourMail@mail.com ', ' yourMail@mail.com ', 'Subject: New Book.\nThe book ' + f.filename + ' has been added.')
      smtpObj.quit()

      return render_template("library.html")

@app.route('/')
def homepage():
    return render_template("library.html")

if __name__ == "__main__":
    app.run()
