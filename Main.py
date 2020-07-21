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
        print(f"Number of {self.nameOfGoods}: {self.numOfGoods}")
        #print("Number of " + self.nameOfGoods + ": ",self.numOfGoods)
        time.sleep(productionInterval)


def main():
    print("Start")
    wood = 0
    berries = 0
    c1 = Civ(wood, "wood")
    c2 = Civ(berries, "berries")

    output1 = int(input(f"Enter production output for {c1.nameOfGoods}: "))
    output2 = int(input(f"Enter production output for {c2.nameOfGoods}: "))

    try:
        while True:

            c1Thread = threading.Thread(target=c1.produce(output1, 2), args=(output1, 2))
            c2Thread = threading.Thread(target=c2.produce(output2, 3), args=(output2, 3))

            c1Thread.start()
            c2Thread.start()

    except KeyboardInterrupt: #press CTRL+C
        pass

if __name__ == '__main__':
    main()
