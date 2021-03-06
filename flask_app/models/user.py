from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.phonenumber = data["phonenumber"]
        self.address = data["address"]
        self.balance = data["balance"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

# ***********************
#         ADD USER
# ***********************
    @classmethod
    def add_user(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,phonenumber,address,balance,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(phonenumber)s,%(address)s,%(balance)s,%(password)s)"
        return connectToMySQL("python_project").query_db(query,data)

# ***********************
#  Get Email for Login
# ***********************
    @classmethod
    def user_email(cls,data):
        query = "SELECT * FROM users WHERE email=%(email)s"
        user_db = connectToMySQL("python_project").query_db(query,data)
        if len(user_db) < 1:
            return False
        return cls(user_db[0])

    @classmethod
    def user_name(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        user_db = connectToMySQL("python_project").query_db(query,data)
        if len(user_db) < 1:
            return False
        return cls(user_db[0])

# *****************************
#   Validate User Registration
# *****************************

    @staticmethod
    def validate_form(textinput):
        email_reg = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if len(textinput["first_name"]) < 1:
            flash("First name required!")
            is_valid = False
        if len(textinput["last_name"]) < 1:
            is_valid= False
            flash("Last name required!")
            is_valid = False
        if not email_reg.match(textinput['email']):
            is_valid = False 
            flash("Invalid email address")
            is_valid = False
        if len(textinput['phonenumber']) < 12:
            is_valid = False 
            flash("Invalid Phone Number")
        if len(textinput["address"]) < 6: 
            flash("Address needs to be at least 6 characters")
            is_valid = False
        if textinput["balance"] == '':
            flash("Need to Put Balance")
            is_valid = False
        else: 
            if float(textinput["balance"]) < 1:
                print(textinput["balance"])
                flash("Balance needs to be at least 1 Dollar")
                is_valid = False
        if len(textinput["password"]) < 8: 
            flash("Password needs to be at least 8 characters")
            is_valid = False
        if textinput["password"] != textinput["confirm_password"]:
            flash("Passwords do not match!")
            is_valid = False
        return is_valid

# *****************************
#   Validate User Login
# *****************************

    @staticmethod
    def validate_user_login(user):
        email_reg = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if not email_reg.match(user["email"]):
            flash("Invalid Email/Password")
            is_valid = False
        if len(user["password"]) < 8 :
            flash("Invalid Email/Password")
            is_valid = False
        return is_valid