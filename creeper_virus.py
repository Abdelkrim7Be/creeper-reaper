import time
import os
import random
import sys

class CreeperVirus:
    def __init__(self):
        self.name = "Creeper"
        self.message = "I’m the Creeper, catch me if you can!"

    def infect(self):
        # Spreading
        print(self.message)
        time.sleep(random.randint(2, 5))
        # Replicating
        self.replicate()

    def replicate(self):
        # Self-replication
        print("Replicating...")
        time.sleep(random.randint(1, 3))
        os.system(f'python {sys.argv[0]}')

if __name__ == "__main__":
    creeper = CreeperVirus()
    creeper.infect()
