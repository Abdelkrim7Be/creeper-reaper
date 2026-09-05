import time
import random
import subprocess
import sys
from pathlib import Path


class CreeperVirus:
    def __init__(self, max_generations=3):
        self.name = "Creeper"
        self.message = "I’m the Creeper, catch me if you can!"
        self.max_generations = max_generations

    def infect(self):
        print(self.message)
        time.sleep(random.randint(2, 5))
        self.replicate()

    def replicate(self):
        if self.max_generations <= 0:
            print("Replication limit reached.")
            return

        print("Replicating...")
        time.sleep(random.randint(1, 3))
        subprocess.Popen([
            sys.executable,
            str(Path(__file__).resolve()),
            str(self.max_generations - 1),
        ])


def get_generation_limit():
    if len(sys.argv) == 1:
        return 3

    try:
        return max(0, int(sys.argv[1]))
    except ValueError:
        raise SystemExit("Invalid generation limit. Please provide a non-negative integer.")


if __name__ == "__main__":
    generations = get_generation_limit()
    creeper = CreeperVirus(max_generations=generations)
    creeper.infect()
