#!/usr/bin/env python3
import os
import sys
import random
import time


def gru():
    try:
        n = int(sys.argv[1])
        if n <= 0:
            print("N должно быть больше 0", file=sys.stderr)
            sys.exit(1)
    except (IndexError, ValueError):
        print("Неверный аргумент N", file=sys.stderr)
        sys.exit(1)

    pid = os.getpid()
    children = []
    failed_count = 0

    for i in range(n):
        child_pid = os.fork()
        if child_pid == 0:  # Дочерний процесс
            random_num = random.randint(5, 10)
            os.execve("./minion", ["./minion", str(random_num)], os.environ)
            sys.exit(1)  # Не должен достичь этой строки, если execve успешен
        else:  # Родительский процесс
            print(f"Gru[{pid}]: process created. PID {child_pid}", file=sys.stdout)

    while children:
        child_pid, status = os.wait()
        status_code = os.WEXITSTATUS(status)
        print(f"Gru[{pid}]: process terminated. PID {child_pid}. Exit status {status_code}", file=sys.stdout)
        children.remove(child_pid)
        if status_code != 0:
            failed_count += 1
            new_child_pid = os.fork()
            if new_child_pid == 0:
                random_num = random.randint(5, 10)
                os.execve("./minion", ["./minion", str(random_num)], os.environ)
                sys.exit(1)
            else:
                children.append(new_child_pid)
                print(f"Gru[{pid}]: process created. PID {new_child_pid}", file=sys.stdout)

    sys.exit(0)


if __name__ == "__main__":
    gru()
