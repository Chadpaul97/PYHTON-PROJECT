from flask_app import app
from flask import render_template,flash,redirect,request,session
from flask_app.models.user import User

# ***************
#    Account Page
# ***************
@app.route("/account")
def account():
    # if "user_id" not in session:
    #     flash("Must be logged in!")
    #     return redirect("/")
    return render_template("account.html")


# ***************
#    Balance Page
# ***************
@app.route("/balance")
def balance():
    # if "user_id" not in session:
    #     flash("Must be logged in!")
    #     return redirect("/")
    return render_template("balance.html")


# ***************
#    Persoal Info
# ***************
@app.route("/changeinfo")
def changeinfo():
    # if "user_id" not in session:
    #     flash("Must be logged in!")
    #     return redirect("/")
    return render_template("changeinfo.html")


# ***************
#   Contact Page
# ***************
@app.route("/contact")
def contact():
    # if "user_id" not in session:
    #     flash("Must be logged in!")
    #     return redirect("/")
    return render_template("contact.html")