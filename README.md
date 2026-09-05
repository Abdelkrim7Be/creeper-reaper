<div align="center">

# Creeper Reaper

Educational Python simulation of the historic Creeper virus and Reaper antivirus.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![psutil](https://img.shields.io/badge/psutil-process%20control-4B8BBE?style=for-the-badge)
![Education](https://img.shields.io/badge/purpose-educational-2EA44F?style=for-the-badge)
![Status](https://img.shields.io/badge/status-simulation-6F42C1?style=for-the-badge)

</div>

## Overview

Creeper Reaper is a small educational lab inspired by two early milestones in computer security history: the **Creeper** program and the **Reaper** cleanup program.

The project contains a simple Python script that prints the classic Creeper message and starts another copy of itself, plus a companion cleanup script that scans local processes and terminates matching Creeper simulation processes.

This is a learning project, not real malware, not an evasion tool, and not a production antivirus.

## Project Structure

| Path | Purpose |
| --- | --- |
| `creeper_virus.py` | Runs the Creeper simulation and starts another copy of the script. |
| `reaper_antivirus.py` | Searches for running Creeper simulation processes and terminates them. |
| `assets/image.png` | Screenshot/demo image used in this README. |
| `README.md` | Project documentation. |

## Demo

The Creeper simulation prints its message, waits briefly, and starts another copy of itself:

![Creeper simulation output](assets/image.png)

## Requirements

- Python 3.x
- `psutil`

Install the Python dependency:

```bash
pip install psutil
```

## Quick Start

Clone the repository:

```bash
git clone https://github.com/Abdelkrim7Be/creeper-reaper.git
cd creeper-reaper
```

Run the Creeper simulation in one terminal:

```bash
python creeper_virus.py
```

By default, the simulation stops after 3 replication generations. You can choose a smaller or larger limit:

```bash
python creeper_virus.py 1
```

Run Reaper in another terminal to stop the simulation:

```bash
python reaper_antivirus.py
```

On some systems, use `python3` instead of `python`:

```bash
python3 creeper_virus.py
python3 reaper_antivirus.py
```

## How It Works

### Creeper Simulation

`creeper_virus.py` defines a `CreeperVirus` class. When run, it:

1. Prints the message: `I’m the Creeper, catch me if you can!`
2. Waits for a random short delay.
3. Starts another copy of the same script until the generation limit is reached.

### Reaper Cleanup

`reaper_antivirus.py` defines a `ReaperProgram` class. When run, it:

1. Scans active processes with `psutil`.
2. Looks for command lines containing `creeper_virus.py`.
3. Terminates matching processes.
4. Prints cleanup progress in the terminal.

## Safety Notes

Run this only in a local test environment. The Creeper script can repeatedly start new Python processes until Reaper is run, so keep a terminal ready for cleanup.
The default generation limit keeps the simulation bounded, but it is still best to avoid high values.

If too many processes are created, stop the script manually from your terminal or run:

```bash
python reaper_antivirus.py
```

## Educational Scope

This repository is intended to demonstrate basic concepts:

- Process creation
- Simple script replication behavior
- Process scanning with `psutil`
- Historical context around early malware and cleanup tools

It does not include persistence, stealth, network spreading, credential access, exploitation, or destructive behavior.
