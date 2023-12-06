from data import students_data, assistants_data, rooms_data, timeslots_data
from GA import GA


def main():
    rooms, rooms_capacity = rooms_data()
    timeslots = timeslots_data()
    students = students_data()
    assistants = assistants_data()

    newGenetic = GA(students, assistants, rooms, timeslots, rooms_capacity)

    newPopulatin = newGenetic.generatePopulation(size=10)

    fitness = []
    for chromosome in newPopulatin:
        print(chromosome.findRoomClashed())
        
        for sche in chromosome.schedules:
            print(sche.room)
      
    
if __name__ == "__main__":
    main()