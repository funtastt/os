#!/usr/bin/env python3
import os
import sys
import time
import random

def minion():
    try:
        sleep_time = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Invalid argument S")
        os._exit(1)

    pid = os.getpid()
    ppid = os.getppid()
    print(f"Minion[{pid}]: created. Parent PID {ppid}")
    time.sleep(sleep_time)
    exit_status = random.randint(0, 1)
    print(f"Child[{pid}]: before terminated. Parent PID {ppid}. Exit status {exit_status}")
    os._exit(exit_status)

if __name__ == "__main__":
    minion()