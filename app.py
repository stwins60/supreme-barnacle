from flask import Flask, render_template, request, url_for, redirect
import sqlite3 as sql
from sqlite3 import Error
import mailer

mysite = Flask(__name__)

mysite.config['CORS_HEADERS'] = 'Content-Type'
mysite.config['FLASK_ENV'] = 'development'
mysite.config['DEBUG'] = True
mysite.config['FLASK_APP'] = 'app.py'

@mysite.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@mysite.route('/contact', methods=['POST'])
def contact():

    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        message = request.form['content']

        if message == '':
            return render_template('index.html', error='Please fill in all fields')
        else:
            try:
                # conn = sql.connect('message_box.db')
                # c = conn.cursor()
                # c.execute("INSERT INTO messages (email, subject, message) VALUES (?, ?, ?)", (email, subject, message))
                # conn.commit()
                subject = 'Message from MySite'
                mailer.sendMyEmail('idrisniyi94@gmail.com', 'idrisniyi94@gmail.com', subject, fname, lname, email, message) 
                return render_template('index.html', success='Your message has been sent')
            except Error as e:
                print(e)
                return render_template('index.html', error='Something went wrong')

    return redirect(url_for('index'))

if __name__ == '__main__':
    mysite.run()