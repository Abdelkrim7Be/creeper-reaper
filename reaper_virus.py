import os 
import sys

class ReaperAntivirus:
    def __init__(self):
        self.name = 'Reaper'
        self.virus_name = 'Creeper'
        
    def hunt_virus(self): 
        print(f"{self.name} is hunting the {self.virus_name} virus.")
        # Terminating all instances of the virus 
        os.system ("pkill -f 'python creeper_virus.py'")
        print("Virus terminated!")
        
if __name__ == "__main__":
    reaper = ReaperAntivirus()
    reaper.hunt_virus()