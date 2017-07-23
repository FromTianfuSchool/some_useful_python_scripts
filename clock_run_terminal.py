# try to implement a schedule event which opens musicbox at specific time

import time, sched, os, datetime

RUN_TIME = (2017, 7, 8, 9, 55, 0, 189, 5, 0)
def scheduler_event():
    s = sched.scheduler(time.time, time.sleep)
    s.enter(0, 1, open_terminal, ())
    s.run()
def which_time_todo():
    return int(time.time()) == (time.mktime(RUN_TIME))
def open_terminal():
    # os.system('musicbox')
    # os.system('cd /home/lebron|pwd')
    os.chdir('/usr/bin')
    os.system('pwd')
    os.system('gnome-terminal')

while True:
    if which_time_todo():
        scheduler_event()
        break
