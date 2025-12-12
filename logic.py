from flask import Flask, render_template, request, redirect, url_for
from datetime import date
import sqlite3


app = Flask(__name__)
DB_path = f"dates.db"

def init():
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS DateTable(
            id INTEGER PRIMARY KEY,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_date():
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM DateTable')
    events = cursor.fetchall()
    conn.close()
    return events

def add_date(val):
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO DateTable (date) VALUES (?)', (val,))
    conn.commit()
    conn.close()

def delete_date(id):
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM DateTable WHERE id = ?', (id,))
    conn.commit()
    conn.close()


@app.route('/')
@app.route('/home') 
def homePage():
    return render_template('index.html')

@app.route('/service')
@app.route('/services')
def servicePage():
    return render_template('services.html')

@app.route('/contact')
def contactPage():
    events = get_date()
    return render_template('contact.html', events = events)

@app.route('/gallery')
def galleryPage():
    return render_template('gallery.html')

@app.route('/getData', methods=['POST'])
def insertDate():
    name = request.form.get('u_name')
    mobile = request.form.get('u_mobile')
    bk_date = request.form.get('u_bk_date')
    f=open('logs.txt', 'a')
    f.write(f'Date: {date.today()}\n')
    f.write(f'[Name: {name}]\t')
    f.write(f'[Mobile: {mobile}]\t')
    f.write(f'[Book date: {bk_date}]\n\n')
    f.close()
    return render_template('feed.html', u_name = name)

@app.route('/admin')
def adminPage():
    events = get_date()
    return render_template('admin.html', events = events)

@app.route('/postData', methods=['POST'])
def postData():
    val = request.form.get('event_date')
    add_date(val)
    return redirect(url_for('adminPage'))

@app.route('/remove_data', methods=['POST'])
def remove_data():
    pass



if __name__ == "__main__":
    init()
    app.run(debug=True)