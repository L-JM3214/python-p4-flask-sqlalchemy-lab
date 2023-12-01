import re
from app import app, db
from server.models import Animal, Enclosure, Zookeeper

class TestApp:

    with app.app_context():
        a_1 = Animal()
        a_2 = Animal()
        e = Enclosure()
        z = Zookeeper()
        e.animals = [a_1, a_2]
        z.animals = [a_1, a_2]
        db.session.add_all([a_1, a_2, e, z])
        db.session.commit()

    def test_animal_route(self):
        response = app.test_client().get('/animal/1')
        assert(response.status_code == 200)

    def test_animal_route_has_attrs(self):
        name_li = re.compile(r'<li>Name: .+</li>')
        species_li = re.compile(r'<li>Species: .+</li>')

        response = app.test_client().get('/animal/1')

        assert len(name_li.findall(response.data.decode())) == 1
        assert len(species_li.findall(response.data.decode())) == 1

    def test_animal_route_has_many_to_one_attrs(self):
        zookeeper_li = re.compile(r'<li>Zookeeper: .+</li>')
        enclosure_li = re.compile(r'<li>Enclosure: .+</li>')

        response = app.test_client().get('/animal/1')

        assert len(zookeeper_li.findall(response.data.decode())) == 1
        assert len(enclosure_li.findall(response.data.decode())) == 1

    def test_zookeeper_route(self):
        response = app.test_client().get('/zookeeper/1')
        assert(response.status_code == 200)

    def test_zookeeper_route_has_attrs(self):
        name_li = re.compile(r'<li>Name: .+</li>')
        birthday_li = re.compile(r'<li>Birthday: .+</li>')

        response = app.test_client().get('/zookeeper/1')

        assert len(name_li.findall(response.data.decode())) == 1
        assert len(birthday_li.findall(response.data.decode())) == 1

    def test_zookeeper_route_has_one_to_many_attr(self):
        animal_li = re.compile(r'<li>Animal: .+</li>')

        id = 1
        response = app.test_client().get(f'/zookeeper/{id}')
        assert len(animal_li.findall(response.data.decode()))

    def test_enclosure_route(self):
        response = app.test_client().get('/enclosure/1')
        assert(response.status_code == 200)

    def test_enclosure_route_has_attrs(self):
        environment_li = re.compile(r'<li>Environment: .+</li>')
        open_li = re.compile(r'<li>Open to Visitors: .+</li>')

        response = app.test_client().get('/enclosure/1')

        assert len(environment_li.findall(response.data.decode())) == 1
        assert len(open_li.findall(response.data.decode())) == 1

    def test_enclosure_route_has_one_to_many_attr(self):
        animal_li = re.compile(r'<li>Animal: .+</li>')

        id = 1
        response = app.test_client().get(f'/enclosure/{id}')
        assert len(animal_li.findall(response.data.decode()))