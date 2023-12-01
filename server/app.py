# app.py
from flask import Flask, render_template
from flask_migrate import Migrate
from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

def get_animal_info(animal_id):
    if animal_id == 1:
        return Animal(name="Lion", species="Panthera leo")
    else:
        return None

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = get_animal_info(id)
    return render_template('animal.html', animal=animal)

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)
    return render_template('zookeeper.html', zookeeper=zookeeper)

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)
    return render_template('enclosure.html', enclosure=enclosure)

@app.route('/animal-route/<int:id>')
def animal_route(id):
    animal = get_animal_info(id)

    if animal:
        return f'''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Animal Info</title>
            </head>
            <body>
                <ul>
                    <li>Name: {animal.name}</li>
                    <li>Species: {animal.species}</li>
                </ul>
            </body>
            </html>
        '''
    else:
        return "Animal not found", 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)