from app import app, db, allowed_file
from flask import url_for, redirect, render_template, request, jsonify, session, flash
from werkzeug.utils import secure_filename
import os
from form import LoginForm
from methods import add_user, login_user, user_logged
from models import User, Stocks
import smtplib


@app.route('/', methods=['post', 'get'])
def home_page():
    form = LoginForm()
    if request.method == "GET":
        if user_logged():
            return redirect("/dashboard ")
        else:
            return render_template("index.html", form=form)
    else:
        if form.validate_on_submit():
            data = request.form.to_dict()
            user = User.query.filter_by(username=data['username'], password=data['password']).first()
            if user:
                flash(f'User has been successfully logged in', 'success')
                login_user(data['username'])
                return redirect("/dashboard")
            else:
                flash(f'Incorrect User/Password', 'danger')
                return redirect("/")
        else:
            return render_template("index.html", form=form)


@app.route("/dashboard")
def dashboard():
    if user_logged():

        return render_template("dashboard.html")
    else:
        return redirect("/")


@app.route("/users", methods=['post', 'get'])
def users():
    if request.method == "POST":
        print(request.form.to_dict())
    if user_logged():
        return render_template("users.html", users=User.query.filter_by())
    else:
        return redirect("/")


@app.route("/logout")
def logout():
    if user_logged():
        del session['username']
        del session['logged_in']
    return redirect("/")


@app.route("/adduser", methods=['get'])
def adduser():
    if user_logged():
        username = request.args.get("username")
        pwd = request.args.get("password")
        if request.args.get("action") == "update":
            selected_user = User.query.filter_by(id=request.args.get("id")).first()
            selected_user.username = username
            selected_user.password = pwd
            db.session.commit()
        elif request.args.get("action") == "delete":
            obj = User.query.filter_by(username=username).one()
            db.session.delete(obj)
            db.session.commit()
        else:
            user = User.query.filter_by(username=username).first()
            if user:
                flash(f'User already exist!', 'danger')
            else:
                flash(f"Sucessfully added user", "success")
                user = User(username, pwd)
                db.session.add(user)
                db.session.commit()
        return redirect("/users")

    else:
        return redirect("/")


@app.route("/stock_list")
def stock_list():
    if user_logged():
        return render_template("stock_list.html", products=Stocks.query.all())


@app.route("/add_product", methods=['post'])
def add_product():
    if user_logged():
        data = request.form.to_dict()
        if data['product_name'] and data['product_quantity']:
            stock = Stocks(data['product_name'], data['product_quantity'])
            db.session.add(stock)
            db.session.commit()
            flash(f"Sucessfully added product", "success")
        else:
            flash(f"Fill All The Details", "success")
        return redirect("/stock_list")
    else:

        return redirect("/")


db.create_all()
