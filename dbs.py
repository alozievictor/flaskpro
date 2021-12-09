
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",  
    database = "payroll",
    user = "root",
    password = ""
)

mycursor = mydb.cursor(dictionary = True) 
  
mycursor.execute(
    """CREATE TABLE IF NOT EXISTS admin(
        ID INT NOT NULL AUTO_INCREMENT, 
        name VARCHAR(100),
        department VARCHAR(255),
        email VARCHAR(225),
        salary INT ,
        PRIMARY KEY (ID)
  )
    """
)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS employees(
        ID INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(100) NOT NULL,
        department VARCHAR(100) NOT NULL,
        gender VARCHAR(20),
        email VARCHAR(100),
        UNIQUE (email),
        PRIMARY KEY (ID)
  );
  """
)
mycursor.execute(
    """CREATE TABLE IF NOT EXISTS employ(
        ID INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(100),
        clarification VARCHAR(100),
        gender VARCHAR(30),
        age INT,
        phone_number INT,
        PRIMARY KEY(ID)
    )
    """
)
# mycursor.execute(
#     """CREATE TABLE IF NOT EXISTS department(
#         ID INT NOT NULL AUTO_INCREMENT,
#         name VARCHAR(100) NOT NULL,
#         salary_range INT,
#         position VARCHAR(100),
#         PRIMARY KEY(ID)
#     );
#    """
# )

# mycursor.execute(
#     """CREATE TABLE IF NOT EXISTS salaries(
#         ID INT NOT NULL AUTO_INCREMENT,
#         first_name VARCHAR(100) NOT NULL,
#         last_name VARCHAR(100) NOT NULL,
#         department VARCHAR(100) NOT NULL,
#         anuall_salary INT,
#         monthly_salary INT,
#         position VARCHAR(100),
#         PRIMARY KEY(ID)
#     );
#     """
# )

# mycursor.execute(
#     """CREATE TABLE IF NOT EXISTS leaves(
#         ID INT NOT NULL AUTO_INCREMENT,
#         first_name VARCHAR(100) NOT NULL,
#         last_name VARCHAR(100) NOT NULL,
#         department VARCHAR(100),
#         reason VARCHAR(200) NOT NULL,
#         date VARCHAR(30) NOT NULL,
#         resumption VARCHAR(30) NOT NULL,
#         PRIMARY KEY(ID)
#     )
#     """
# )

# mycursor.execute(
#     """CREATE TABLE IF NOT EXISTS payroll(
#         ID INT NOT NULL AUTO_INCREMENT,
#         first_name VARCHAR(100) NOT NULL,
#         last_name VARCHAR(100) NOT NULL,
#         department VARCHAR(100) NOT NULL, 
#         monthly_salary INT,
#         account_name VARCHAR(50) NOT NULL, 
#         account_number INT,
#         PRIMARY KEY(ID)
#     );
#     """
# )