from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app.forms import LoginForm, Publication
from flask import request
from flask import flash, abort, redirect, url_for
import requests
"""
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
"""

template_dir = '../templates/startbootstrap-sb-admin-2-gh-pages'
static_dir = '../static'
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SECRET_KEY'] = 'you-will-never-guess'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.name


class Pub(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    purpose = db.Column(db.String(80), primary_key=True)
    Amount = db.Column(db.Integer, unique=True, nullable=False)
    Months = db.Column(db.Integer, unique=True, nullable=False)
    Description = db.Column(db.String(128), primary_key=True)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


url = ['https://source.unsplash.com/user/erondu/60x60',
       'https://source.unsplash.com/user/erondu/60x60',
       "https://source.unsplash.com/QAB-WJcbgJk/60x60"
       ]
img_url = ["https://img-4.linternaute.com/YxAwx7GUfKAu7ms2zNwXkPcZUOI=/1240x/smart/6b9870fa5bb54774b766182151196ad7/ccmcms-linternaute/10663522.jpg",
           "https://previews.123rf.com/images/bialasiewicz/bialasiewicz1511/bialasiewicz151101543/48220500-image-de-vieille-femme-malade-couch%C3%A9-dans-son-lit-d-h%C3%B4pital.jpg",
           "https://www.wgu.edu/content/dam/web-sites/blog-newsroom/blog/images/national/2020/march/homeless-resources.jpg"]
users = ["Chiheb", "Taher", "Valerie"]
descriptions = [
    "I had an accident and my car broke down and I don't have enough money to fix it.I'll be grateful if anyone helped me",
    "My mother is suffering from rare disease I need money to buy the necessary medicines and to provide the necessary treatments to help her",
    "I need money to provide my payment rent to keep my place. I'll be grateful if anyone can help me and I'm ready for hight rate APR"]
durations = ["4 Months", "6 Months", "3 Months"]
Amounts = ["2000 $", "4000$", "1500 $"]
pubs = []
for i in range(3):
    pubs.append({"url": url[i], "des": descriptions[i],
                 "name": users[i], "dur": durations[i], "amount": Amounts[i],
                 "img_url": img_url[i]})


@app.route('/')
def index2():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index2'))
    return render_template('login.html', form=form)


@app.route('/apply', methods=['GET', 'POST'])
def apply():
    form = Publication()
    print(request.method)
    if form.validate_on_submit():
        """
        Pub = Publication(request.form, user_id=)
        db.session.add(Pub)
        db.session.commit()
        """
        return redirect(url_for('get_user', name='offers'))
    return render_template('apply.html', form=form)


page_list = ["base", "offers", "buttons", "cards", "apply",
             "charts", "forgot-password", "index", "login", "register", "Sidebar", "tables", "utilities-animation", "utilities-border", "utilities-color", "utilities-other"]


@app.route('/<name>')
def get_user(name):
    if(name == "offers"):
        return render_template("offers.html", pubs=pubs)
    if(name in page_list):
        return render_template(name+".html")
    else:
        return render_template("404.html")


@app.route('/data', methods=['GET', 'POST'])
def get_data():
    data = request.data
    print(data)
    return data


"""
@app.route('/<name>/<email>')
def index(name, email):

    user = User(email=email, name=name)
    db.session.add(user)
    db.session.commit()
    # db.session.add(user)
    # db.session.commit()
    # if(not(email)and(not(name))):
    #    return '<h1> Home page!</h1>'
    return '<h1> {}</h1>'.format(user.email)
"""

if(__name__ == "__main__"):
    app.run(debug=True)
