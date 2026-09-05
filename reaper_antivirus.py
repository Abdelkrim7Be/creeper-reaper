import psutil
from pathlib import Path


class ReaperProgram:
    def __init__(self):
        self.target_script = Path(__file__).with_name("creeper_virus.py").resolve()

    def hunt_virus(self):
        print("Reaper is scanning for Creeper virus...")
        terminated_count = 0

        for proc in psutil.process_iter(["pid", "name", "cmdline"]):
            try:
                cmdline = proc.info["cmdline"] or []
                if not self._is_creeper_process(cmdline):
                    continue

                print(f"Found Creeper virus process with PID {proc.pid}. Terminating...")
                proc.terminate()

                try:
                    proc.wait(timeout=3)
                except psutil.TimeoutExpired:
                    proc.kill()
                    proc.wait(timeout=3)

                terminated_count += 1
                print(f"Process {proc.pid} terminated.")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

        print(f"Creeper virus cleanup complete. Terminated {terminated_count} process(es).")

    def _is_creeper_process(self, cmdline):
        for argument in cmdline[1:]:
            try:
                if Path(argument).resolve() == self.target_script:
                    return True
            except OSError:
                continue

        return False

if __name__ == "__main__":
    reaper = ReaperProgram()
    reaper.hunt_virus()
