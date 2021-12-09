from flask import Flask, render_template, request, redirect
from dbm import mydb, mycursor


app = Flask(__name__)

@app.route('/')
def index():
    mycursor.execute("SELECT * FROM customers")
    customers = mycursor.fetchall()
    return render_template('index.html', customers = customers)


@app.route('/add', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'GET':
        return render_template('post_form.html')
    if request.method == 'POST':
        _first_name = request.form['first_name']
        _last_name = request.form['last_name']
        _address = request.form['address']
        _age = request.form['age']
        sql = 'INSERT INTO customers (name, address, age) VALUES (%s, %s, %s)'
        val = (_first_name,_last_name, _address, _age)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('admin_details.html')


@app.route('/details/<int:id>')
def customer_details(id):
    mycursor.execute(f'SELECT * FROM customers WHERE ID={id}')
    customer = mycursor.fetchone()
    return render_template('customer_detail.html', customer = customer)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_customer(id):
    if request.method == 'GET':
        mycursor.execute(f'SELECT * FROM customers WHERE ID={id}')
        customer = mycursor.fetchone()
        return render_template('edit_customer.html', customer = customer)
    if request.method == 'POST':
        _name = request.form['name']
        _address = request.form['address']
        _age = request.form['age']
        sql = f'UPDATE customers SET name = %s, address = %s, age=%s WHERE ID = %s'
        values = (_name, _address, _age, id)
        mycursor.execute(sql, values)
        mydb.commit()
        return redirect('admin_details.html')


@app.route('/delete/<int:id>')
def delete_customer(id):
    sql = f'DELETE FROM customers WHERE ID={id}'
    mycursor.execute(sql)
    mydb.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run()