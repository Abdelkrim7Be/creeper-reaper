import psutil
import os

class ReaperProgram:
    def __init__(self):
        self.target_script = "creeper_virus.py"

    def hunt_virus(self):
        print("Reaper is scanning for Creeper virus...")

        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                cmdline = proc.info['cmdline']
                if cmdline and self.target_script in " ".join(cmdline):
                    print(f"Found Creeper virus process with PID {proc.pid}. Terminating...")
                    proc.terminate()
                    proc.wait()
                    print(f"Process {proc.pid} terminated.")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

        print("Creeper virus cleanup complete.")

if __name__ == "__main__":
    reaper = ReaperProgram()
    reaper.hunt_virus()
