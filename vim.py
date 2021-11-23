import threading
import os

command = "msg * vim.exe"

def main():
    for i in range(0,35):
        t = threading.Thread(target=funct, args=(f"10.1.1.{i}",))
        t.start()


def funct(ip):
    os.system(f"wmic /node:{ip} process call create \"cmd.exe /c {command}\"")


main()
