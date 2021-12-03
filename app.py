from flask import Flask, render_template, request, url_for, redirect
import flask_cors as CORS
import sqlite3 as sql
from sqlite3 import Error

app = Flask(__name__)
# CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['FLASK_ENV'] = 'development'
app.config['DEBUG'] = True
app.config['FLASK_APP'] = 'app.py'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():

    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['content']

        if email == '' or subject == '' or message == '':
            return render_template('index.html', error='Please fill in all fields')
        else:
            try:
                conn = sql.connect('message_box.db')
                c = conn.cursor()
                c.execute("INSERT INTO messages (email, subject, message) VALUES (?, ?, ?)", (email, subject, message))
                conn.commit()    
                return render_template('index.html', success='Your message has been sent')
            except Error as e:
                print(e)
                return render_template('index.html', error='Something went wrong')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()