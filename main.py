# ------------------------- [ Main Project File | Coding: utf-8 ] ------------------------- #
# Project: FastPort                                                                         #
# File: main.py                                                                             #
# Python Version: 3.10.2 - Tested: 3.10.2 - All others are untested.                        #
# The libraries should get installed among the integrated libraries: None                   #
# ----------------------------------------- [ ! ] ----------------------------------------- #
# This code doesn't have any errors. if you got an error, check syntax and python version.  #
# ----------------------------------------- [ ! ] ----------------------------------------- #
# Author: nihadenes - <nihadenesvideo@gmail.com>                                            #
# Links: <https://github.com/nihadenes>                                                     #
# Date: 3/4/2022                                                                            #
# License: MIT                                                                              #
# --------------------------------------- [ Enjoy ] --------------------------------------- #

import threading, socket, os


def scanport(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        if s.connect_ex((target, port)) == 0:
            portlist.append(port)
            print(f"Port {port} is open." + "\t")

        print(f"Current port: {port}" + "\t", end="\r")
        s.close()

    except:
        pass


if __name__ == "__main__":
    portlist, target, finish = [], "google.com", 0

    threads = [threading.Thread(target=scanport, kwargs={'port': i}) for i in range(1, 65535+1)]
    [t.start() for t in threads]
    [t.join() for t in threads]

    input(sorted(portlist))
