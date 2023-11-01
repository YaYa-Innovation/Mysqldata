from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Set up MySQL connection
mysql_conn = mysql.connector.connect(
    host="your_mysql_host",
    user="your_mysql_user",
    password="your_mysql_password",
    database="stock_management"
)
cursor = mysql_conn.cursor(dictionary=True)

@app.route('/')
def index():
    cursor.execute("SELECT * FROM spares")
    spares = cursor.fetchall()
    return render_template('index.html', spares=spares)

@app.route('/add_spare', methods=['GET', 'POST'])
def add_spare():
    if request.method == 'POST':
        data = request.form
        cursor.execute("INSERT INTO spares (spare_number, spare_name, category, sub_category, spare_description, location, quantity, receiver_name, bearer_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (data['spare_number'], data['spare_name'], data['category'], data['sub_category'], data['spare_description'], data['location'], data['quantity'], data['receiver_name'], data['bearer_number']))
        mysql_conn.commit()
        return redirect(url_for('index'))
    return render_template('add_spare.html')

@app.route('/edit_spare/<int:spare_id>', methods=['GET', 'POST'])
def edit_spare(spare_id):
    cursor.execute("SELECT * FROM spares WHERE id = %s", (spare_id,))
    spare = cursor.fetchone()

    if request.method == 'POST':
        data = request.form
        cursor.execute("UPDATE spares SET spare_number=%s, spare_name=%s, category=%s, sub_category=%s, spare_description=%s, location=%s, quantity=%s, receiver_name=%s, bearer_number=%s WHERE id=%s",
                       (data['spare_number'], data['spare_name'], data['category'], data['sub_category'], data['spare_description'], data['location'], data['quantity'], data['receiver_name'], data['bearer_number'], spare_id))
        mysql_conn.commit()
        return redirect(url_for('index'))

    return render_template('edit_spare.html', spare=spare)

@app.route('/view_spare/<int:spare_id>')
def view_spare(spare_id):
    cursor.execute("SELECT * FROM spares WHERE id = %s", (spare_id,))
    spare = cursor.fetchone()
    return render_template('view_spare.html', spare=spare)

if __name__ == '__main__':
    app.run(debug=True)
