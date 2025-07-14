# adoption_site.py
import os
from forms import AddForm, DelForm, AddOwner
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = "my$ECRETkey"

############### SQL DATABASE ###############
base_dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

###############     MODELS    ###############
class Puppy(db.Model):
    __tablename__ = "puppies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    #one to one relationship
    # Puppy.owner attribute, and Owner.puppy attribute
    ## rufus = Puppy('rufus')
    ## jose = Owner('Jose', 'rufus.id')
    ## from Puppy model, print(rufus.owner.name)
    ## from Owner model, print(jose.puppy.name)
    owner = db.relationship('Owner', backref="puppy", uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner}."
        else:
            return f"Puppy name is {self.name} and has no owner yet."
    
class Owner(db.Model):
    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey("puppies.id"))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id
    
    def __repr__(self):
        return f"{self.name}"

############### VIEW FUNCTIONS ###############
@app.route('/')
def index():
    return render_template("home.html")

@app.route('/owner', methods=["GET", "POST"])
def add_owner():
    form = AddOwner()

    if form.validate_on_submit():
        name =form.name.data
        puppy_id = form.puppy_id.data
        new_owner = Owner(name, puppy_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_puppy'))
    return render_template("owner.html", form=form)

@app.route('/add', methods=["GET", "POST"])
def add_puppy():
    
    form = AddForm()
    if form.validate_on_submit():

        name = form.name.data
        new_puppy = Puppy(name)
        db.session.add(new_puppy)
        db.session.commit()

        return redirect(url_for('list_puppy'))
    return render_template('add.html', form=form)

@app.route('/list')
def list_puppy():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@app.route('/delete', methods=["GET", "POST"])
def delete_puppy():
    form = DelForm()

    if form.validate_on_submit():
        
        id = form.id.data
        delete_puppy = Puppy.query.get(id)
        db.session.delete(delete_puppy)
        db.session.commit()

        return redirect(url_for('list_puppy'))
    return render_template('delete.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)