from flask import Flask, render_template, request,redirect
from dbm import mydb, mycursor

app = Flask(__name__)



if __name__ == '__main__':
    app.run()