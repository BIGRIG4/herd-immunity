import random
random.seed(42)
from virus import Virus


class Person(object):

    def __init__(self, _id, is_vaccinated, infection=None):
        self._id = _id  # int
        self.is_alive = True  # boolean
        self.is_vaccinated = is_vaccinated  # boolean
        self.infection = infection  # Virus object or None

    def did_survive_infection(self):
        if self.infection:
            if random.random() > self.infection.mortality_rate:
                self.is_vaccinated = True
                self.infection = None
                return True
        self.is_alive = False
        return False

def test_vacc_person_instantiation():
    person = Person(1, True)

    assert person._id == 1
    assert person.is_alive is True
    assert person.is_vaccinated is True
    assert person.infection is None
def test_not_vacc_person_instantiation():
    person = Person(2, False)

    assert person._id == 2
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.infection is None

def test_sick_person_instantiation():
    virus = Virus("Dysentery", 0.7, 0.2)
    person = Person(3, False, virus)

    assert person._id == 3
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.infection is virus

def test_did_survive_infection():
    virus = Virus("Dysentery", 0.7, 0.2)
    person = Person(4, False, virus)

    survived = person.did_survive_infection()

if survived:
        assert person.is_alive is True
        assert person.is_vaccinated is True
        assert person.infection is None
    else:
        assert person.is_alive is False
        assert person.is_vaccinated is False
        assert person.infection is virus


if __name__ == '__main__':
    test_vacc_person_instantiation()
    test_not_vacc_person_instantiation()
    test_sick_person_instantiation()
    test_did_survive_infection()
