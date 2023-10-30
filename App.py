from flask import Flask, render_template, request, redirect, url_for
from database import insert, update, select, delete, create_table

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert', methods=['GET', 'POST'])
def insert_data():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        insert(name, age, city)
        return redirect(url_for('index'))
    return render_template('insert.html')

@app.route('/update', methods=['GET', 'POST'])
def update_data():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        update(name, age, city, id)
        return redirect(url_for('index'))
    return render_template('update.html')

@app.route('/select')
def select_data():
    result = select()
    return render_template('select.html', result=result)

@app.route('/delete', methods=['POST'])
def delete_data():
    id = request.form['id']
    delete(id)
    return redirect(url_for('select_data'))

@app.route('/create_table', methods=['GET', 'POST'])
def create_table_page():
    if request.method == 'POST':
        table_name = request.form['table_name']
        columns = request.form['columns'].split(',')
        create_table(table_name, columns)
        return redirect(url_for('index'))
    return render_template('create_table.html')

if __name__ == '__main__':
    app.run(debug=True)
