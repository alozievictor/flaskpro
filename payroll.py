from flask import Flask, render_template, request, redirect,url_for
  # from werkzeug.datastructures import RequestCacheControl
from dbs import mydb, mycursor

app = Flask(__name__)

# @app.route('/')
# @app.route('/admin') 
# def admin_page():
#     return render_template('admin.html')

@app.route('/') 
def index():
    return render_template('index.html')



@app.route('/adm', methods= ['GET', 'POST'])
def admin():
    message = ''
    username = 'Boss'
    password = 'independent'
    if request.method == 'GET':
        return render_template("admin.html")
    if request.method == 'POST':
        _username = request.form['username']
        _password = request.form['password']
        if _username == username and _password == password:
            #  return redirect("/register")
            return render_template("register.html")
        else:
            message = 'Wrong Username or Password'
        return render_template('admin.html', message  = message)
        # return redirect('/emp',message = message)

@app.route('/emp', methods=['GET', 'POST'])
def employee():
    if request.method == 'GET':
        return render_template('employee.html')
    if request.method == 'POST':
        _name = request.form['name']
        _department = request.form['department']
        _gender = request.form['gender']
        _email = request.form['email']
        sql = f' INSERT INTO employees(name, department, gender, email) VALUES (%s, %s, %s, %s)'
        val = (_name, _department, _gender, _email)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect("/row")
    return render_template("admin.html")
    
@app.route('/back')
def back():
    return render_template("index.html")


@app.route('/addemployee', methods=['GET','POST'])
def addemployee():
    if request.method == 'GET':
       return render_template("viewemp.html")
    if request.method == 'POST':
        _name = request.form['name']
        _clarification = request.form['clarification']
        _gender = request.form['gender']
        _age = request.form['age']
        _phone_number = request.form['phone_number']
        sql = 'INSERT INTO employ (name, clarification, gender, age, phone_number) VALUES (%s, %s, %s, %s, %s)'
        val = (_name, _clarification, _gender, _age, _phone_number)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM employ")
        employee = mycursor.fetchall()
        return render_template('viewemp.html', employee = employee)

@app.route('/row', methods=['GET', 'POST'])
def List():
    if request.method == 'GET':
        mycursor.execute("SELECT * FROM employ")
        employee = mycursor.fetchall()
        return render_template('viewemp.html', employee = employee)
        
@app.route('/row', methods=['GET', 'POST'])
def View():
    if request.method == 'GET':
        return render_template('viewemp.html')


@app.route('/employ')
def employ():
    return render_template("employstaff.html")

@app.route('/details/<int:id>')
def admin_details(id): 
    mycursor.execute(f'SELECT * FROM employees WHERE ID={id}')
    employees = mycursor.fetchone()
    return render_template('admin_details.html', employees = employees)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_customer(id):
    if request.method == 'GET':
        mycursor.execute(f'SELECT * FROM employee WHERE ID={id}')
        employee = mycursor.fetchone()
        return render_template('edit_employee.html', employee = employee)
    if request.method == 'POST':
        _FirstName = request.form['FirstName']
        _LastName = request.form['LastName']
        _department =request.form['department']
        _gender = request.form['gender']
        _email = request.form['email']
        sql = f'UPDATE employee SET FirstName = %s, LastName = %s, department = %s, gender = %s, email = %s WHERE ID = %s'
        val = (_FirstName, _LastName, _department, _email, _gender, id)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/edit')



@app.route('/register', methods = ['GET', 'POST'])
def registerpage():
    if request.method == 'GET':
        return render_template('empolyee.html')
    if request.method == 'POST':
        _FirstName = request.form['FirstName']
        _LastName = request.form['LastName']
        _department = request.form['department']
        _gender = request.form['gender']
        _email = request.form['email']
        sql = 'INSERT INTO employees (name,department, gender, email) VALUES (%s, %s, %s, %s)'
        val = (_FirstName,_department,_gender,_email)
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.execute(f'SELECT * FROM employees')
        employees = mycursor.fetchall()
        return render_template('admin_details.html', employees = employees, namee = _FirstName)             

     
       


        

  






# @app.route('/add', methods = ['GET', 'POST'])
# def employees():
#     if request.method == 'POST':
#        _name = request.form['name']
#        _department = request.form['department']
#        _email = request.form['email']
#        _salary = request.form['salary']
#        _salary = request.form['salary']
#        sql = f'INSERT INTO employee (name, department, email, salary) VALUES (%s, %s, %s, %s)'
#        val = (_name, _department, _email, _salary)
#        mycursor.execute(sql, val)
#        mydb.commit()
#     return render_template('post_form.html')



# @app.route('/emp', methods=['GET','POST']) 
# def employee():
#     if request.method == 'POST':
#         _first_name=request.form[first_name]
#         _last_name=request.form[last_name]
#         _department=request.form[department]
#         _gender= request.form[gender]
#         _email=request.form[email]
#         sql = (f'INSERT INTO employee(first_name, last_name, department, gender, email) VALUES(%s,%s,%s,%s)'
#         val = (_first_name, last_name, _department, _gender,email)
#         mycursor.execute(sql, val)
#         mydb.commit()
#         return render_template('employee.html')







# @app.route('/details/<int:id>')
# def admin_details(id): 
#     mycursor.execu te(f'SELECT * FROM employee WHERE ID={id}')
#     employee = mycursor.fetchone()
#     return render_template('admin_details.html', employee = employee)



# @app.route('/delete/<int:id>')
# def delete_employee(id):
#     sql = f'DELETE * FROM employee WHERE ID ={id}'
#     mycursor.execute(sql)
#     mydb.commit()
#     return redirect('/')

if __name__ == '__main__':
    app.run(debug=True )