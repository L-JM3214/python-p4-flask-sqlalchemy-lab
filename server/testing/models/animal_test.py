from app import app
from server.models import db, Animal

class TestAnimal:

    def test_can_be_instantiated(self):
        a = Animal()
        assert a
        assert isinstance(a, Animal)

    def test_has_name_and_species(self):
        a = Animal(name='Phil', species='Rhinoceros')
        assert a.name == 'Phil'
        assert a.species == 'Rhinoceros'