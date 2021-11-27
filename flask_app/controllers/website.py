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


# *******************
#   New Product Page
# *******************
@app.route("/newproducts")
def newproducts():
    # if "user_id" not in session:
    #     flash("Must be logged in!")
    #     return redirect("/")
    return render_template("newproducts.html")

# *******************
#   Clearence Page
# *******************
@app.route("/clearence")
def clearence():
    # if "user_id" not in session:
    #     flash("Must be logged in!")
    #     return redirect("/")
    return render_template("clearence.html")

# *******************
#   Hot Deals Page
# *******************
@app.route("/hotdeals")
def hotdeals():
    # if "user_id" not in session:
    #     flash("Must be logged in!")
    #     return redirect("/")
    return render_template("hotdeals.html")



# *******************
#   Holiday Page
# *******************
@app.route("/holiday")
def holiday():
    # if "user_id" not in session:
    #     flash("Must be logged in!")
    #     return redirect("/")
    return render_template("holiday.html")

# *****************
#    Purchased Page
# *****************
@app.route("/purchased")
def purchased():
    # if "user_id" not in session:
    #     flash("Must be logged in!")
    #     return redirect("/")
    return render_template("purchased.html")
