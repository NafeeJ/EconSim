import numpy as np
import matplotlib.pyplot as plt
import sched, time
import threading

class Civ:

    def __init__(self, item):
        self.item = 0

    @property
    def produce(self):
        self.item += 1

def background():
    wood = 0
    berries = 0
    c1 = Civ(wood)
    c2 = Civ(berries)




def main():
    print("Start")
    """wood = 0
    berries = 0
    c1 = Civ(wood)
    c2 = Civ(berries)"""

    try:
        while True:
            c1.produce
            c2.produce

            print(c1.item)
            print(c2.item)

            time.sleep(3)
    except KeyboardInterrupt: #press CTRL+C
        pass


"""        c1.produce
        c2.produce

        print(c1.item)
        print(c2.item)"""

if __name__ == '__main__':
    main()
