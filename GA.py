import numpy as np
from copy import deepcopy
import random


class Gene:
    def __init__(self, students: list, assistents: list, room: int, timeslot: int) -> None:
        self.students = students
        self.assistents = assistents
        self.room = room
        self.timeslot = timeslot


class Chromosome:
    def __init__(self, schedules: list[Gene]) -> None:
        self.schedules = schedules
        self.fitness = None
        self.roomClashed = None
        self.timeslotClashed = None
        self.studentNotAssigned = None
        self.AssistentClashed = None

    def findRoomClashed(self):
        sche = deepcopy(self.schedules)
        room_counts = {}

        for cohort in sche:
            room_number = cohort.room
            room_counts[room_number] = room_counts.get(room_number, 0) + 1

        # Check for clashes and count how many rooms have clashes
        room_clashes = sum(
            count - 1 for count in room_counts.values() if count > 1)

        self.roomClashed = room_clashes

        return room_clashes
    
    def checkRoomAvailibity(self,roomsAvail):
        pass

    def findTimeSlotClashed(self):
        pass
    
    def findAssistantClashed(self):
        pass
    
    def checkAssistantAvailbility(self):
        pass
    
    def findAssistantClashed(self):
        pass
    def checkStudentAvailbility(self):
        pass
        
    def setFitnessScore(self):
        self.fitness = fitnessFunction(self)


class GA:
    def __init__(self, students: list, assistens: list, rooms: list, timeslots: list, rooms_capacity: list) -> None:
        self.students = students
        self.assistens = assistens
        self.rooms = rooms
        self.rooms_capacities = rooms_capacity
        self.timeslots = timeslots
        self.cohorts = [0, 1, 2, 3, 4, 5]

    def __generateIndividual(self) -> Chromosome:
        cohortSchedules = []
        all_students = deepcopy(self.students)
        all_assistens = deepcopy(self.assistens)
        rooms = deepcopy(self.rooms)
        rooms_capacities = deepcopy(self.rooms_capacities)
        timeslots = deepcopy(self.timeslots)

        for cohort in self.cohorts:
            # Random room
            room = random.choice(rooms)
            room_capacity = rooms_capacities[rooms.index(room)]
            rooms.remove(room)

            timeslot = random.choice(timeslots)
            timeslots.remove(timeslot)

            assistens = random.sample(all_assistens, 2)
            for item in assistens:
                all_assistens.remove(item)

            if len(all_students) > room_capacity:
                students = random.sample(all_students, room_capacity)
                for item in students:
                    all_students.remove(item)
            else:
                students = all_students
            
            newGene = Gene(students, assistens, room, timeslot)

            cohortSchedules.append(newGene)

        chromosome = Chromosome(cohortSchedules)

        return chromosome

    def generatePopulation(self, size) -> list[Chromosome]:
        population = []

        for i in range(size):
            individual = self.__generateIndividual()

            population.append(individual)

        return population

    def fitnessScore(self, population):
        score = []
        pass


def fitnessFunction(chromosome: Chromosome):
    fitness_score = 0

    roomCrash = chromosome.findRoomClashed()
    fitness_score += (roomCrash/2)*5
    
    classAvail = chromosome.checkRoomAvailibity()
    fitness_score += (classAvail/2)*5

    return fitness_score
