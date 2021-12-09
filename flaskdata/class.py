import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    database = "transportation",
    user = "root",
    password = ""
)

mycursor = mydb.cursor()

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS  registration(
        name VARCHAR(50) NOT NULL,
        email  VARCHAR(100) NOT NULL,
        password VARCHAR(50) NOT NULL,
        UNIQUE (password)
    )
    """
)
mycursor.execute(
   """CREATE TABLE IF NOT EXISTS admin(
        price INT,
        shedules VARCHAR(50),
        drivers INT,
        routes VARCHAR(50),
        seats INT  
     );
   """
)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTs passenger(
        ID INT NOT NULL,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        phone_number INT NOT NULL,
        email VARCHAR(100) NOT NULL,
        destination VARCHAR(100) NOT NULL,
        PRIMARY KEY (ID)
   )
   """
)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS  routes(
        shedules VARCHAR(100),
        seat INT,
        price INT,
        time INT
    )
   """
)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS booking(
        ID INT NOT NULL,
        name VARCHAR(50) NOT NULL,
        seat INT,
        payment INT DEFAULT 10000,
        routes VARCHAR(100),
        PRIMARY KEY (ID)
    )
   """
)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS  receipt(
        ID INT NOT NULL,
        name VARCHAR(50),
        payment INT, 
        seat_no INT, 
        PRIMARY KEY (ID)
   )
   """
)