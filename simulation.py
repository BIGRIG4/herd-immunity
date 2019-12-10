import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus
import os


class Simulation(object):
    def __init__ (self, pop_size, vacc_percentage, virus, initial_infected):
        self.population = []
        self.pop_size = pop_size
        self.next_person_id = 0
        self.virus = virus
        self.initial_infected = initial_infected
        self.total_infected = 0
        self.current_infected = 0
        self.vacc_percentage = vacc_percentage
        self.total_dead = 0
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, pop_size, vacc_percentage, initial_infected)
        self.newly_infected = []
        self.newly_dead = []


        self.logger = Logger(self.file_name)
        self.population = self._create_population(initial_infected)
        self.simulation = Simulation(pop_size, vacc_percentage, virus, initial_infected)


def _create_population(self, initial_infected):

        population = []
        self.current_infected = 0
        vaccinated = 0
        id = 0

    while len(population) != pop_size:
            if self.initial_infected != self.current_infected:
                population = Person(id, is_vaccinated = False, infection = virus) #infected
                self.current_infected+=1
                id+=1
        else:
                if random.random() < self.vacc_percentage:
                    population.append(Person(id, is_vaccinated=True)) #vaccinated / unaffected
                    vaccinated+=1
                    id+=1
                else:
                    population.append(Person(id, is_vaccinated=False)) #infected / sick
                    self.current_infected+=1
                    id+=1
                return population


    def _simulation_should_continue(self):
        if self.current_infected == 0 or vacc_percentage < 1:
            return True
        else:
            return False


    def run(self):

        time_step_number = 0
        should_continue = self._simulation_should_continue()

        while should_continue:
            self.time_step()
            should_continue = self._simulation_should_continue()
            time_step_number +=1
            self.logger.log_time_step(time_step_number, self.newly_infected, self.newly_dead, self.total_infected, self.total_dead)
            print('The simulation has ended after {time_step_number} turns.'.format(time_step_number))
            pass

    def time_step(self):
        interaction = 0
        while interaction < 100:
            for person in self.population:
                if person.is_alive == True and person.is_infected == True:
                    random_person = random.choice(self.population)
                    interacting=True
                    while interacting:
                        self.simulation.interaction(person, random_person)
                        interaction+=1
                        interacting=False
                    random_person = random.choice(self.population)

        self._infect_newly_infected()
    def interaction(self, person, random_person):
        assert person.is_alive == True
        assert random_person.is_alive == True

        random_person_sick = False
        if random_person.is_infected is None:
            random_person_sick = False
        else:
            random_person_sick = True

        if random_person.is_vaccinated == True:
            self.logger.log_interaction(self, person, random_person, random_person_sick, random_person.is_vaccinated)
            return None
        elif random_person.is_infected == True:
            self.logger.log_interaction(self, person, random_person, random_person_sick, random_person.is_vaccinated)
            return None
        elif random_person.is_infected and random_person.is_vaccinated == False:
            rand_num = random.randint(0,1)
            if rand_num <= repro_rate:
                self.newly_infected.append(random_person._id)
                self.logger.log_interaction(self, person, random_person, random_person_sick, random_person.is_vaccinated)

def _infect_newly_infected(self):
        for person in self.newly_infected:
            person.infect(self.virus)


if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name = str(params[0])
    repro_rate = float(params[1])
    mortality_rate = float(params[2])
    pop_size = int(params[3])
    vacc_percentage = float(params[4])

if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(virus_name, repro_rate, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage,  virus, initial_infected)
    sim.run()
