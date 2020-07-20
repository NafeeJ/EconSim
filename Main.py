import numpy as np
import matplotlib.pyplot as plt
import sched, time
import threading

class Civ:

    def __init__(self, numOfGoods, nameOfGoods):
        self.numOfGoods = numOfGoods
        self.nameOfGoods = nameOfGoods

    def produce(self, productionOutput, productionInterval):
        self.numOfGoods += productionOutput
        print("Number of " + self.nameOfGoods + ": " , self.numOfGoods)
        time.sleep(productionInterval)


def main():
    print("Start")
    wood = 0
    berries = 0
    c1 = Civ(wood, "wood")
    c2 = Civ(berries, "berries")

    try:
        while True:

            c1Thread = threading.Thread(target=c1.produce(1, 2), args=(1, 2))
            c2Thread = threading.Thread(target=c2.produce(2, 3), args=(2, 3))

            c1Thread.start()
            c2Thread.start()

    except KeyboardInterrupt: #press CTRL+C
        pass

if __name__ == '__main__':
    main()
