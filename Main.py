import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import sched, time
import threading

class Civ:

    def __init__(self, sNumOfGoods, rNumOfGoods, nameOfGoods, population):
        self.sNumOfGoods = sNumOfGoods
        self.rNumOfGoods = rNumOfGoods
        self.nameOfGoods = nameOfGoods
        self.population = population

    def produce(self, productionOutput):
        self.sNumOfGoods += productionOutput
        print(f"Number of {self.nameOfGoods}: {self.sNumOfGoods}")
        time.sleep(1)


def main():
    print("Start")

    #Ask the user how many civs they want
    numCivs = int(input("How many civs do you want?: "))
    print("\n")
    civsList = [] #store the name and starting amount in a list

    for i in range(numCivs):
        y = i+1
        print(f"Civ {y}")
        name = input(f"What is the name of Civ {y}?: ")
        start = int(input(f"What is the starting amount of product of Civ {y}?: "))
        rate = int(input(f"What is the production start/rate of Civ {y}?: "))
        pop = int(input(f"What is the starting population of Civ {y}?: "))
        print("\n")
        n = Civ(start, rate, name, pop)
        civsList.append(n)

    #print(civsList)
    for i in civsList:
        print(f"Starting Amount: {i.sNumOfGoods}, Rate: {i.rNumOfGoods}, Name: {i.nameOfGoods}, Population: {i.population}")
        #print(i.sNumOfGoods, i.rNumOfGoods, i.nameOfGoods, i.population)

    try:
        while True:
            for i in range(len(civsList)):
                n = threading.Thread(target=civsList[i].produce(civsList[i].rNumOfGoods), args=(civsList[i].rNumOfGoods))

    except KeyboardInterrupt: #press CTRL+C
        pass

if __name__ == '__main__':
    main()
