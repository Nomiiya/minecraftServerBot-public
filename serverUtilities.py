import multiprocessing
import os, sys, subprocess
import wmi
import signal
from subprocess import STARTF_USESTDHANDLES, Popen, PIPE
from pathlib import Path #Pathing
from datetime import datetime

#Generic def
def check_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)

def get_processes():
    f = wmi.WMI()
    for process in f.Win32_Process():
        if process.name == "java.exe":
            #print(f"{process.ProcessId:<10} {process.Name}")
            #subprocess.Popen.communicate
            kill_console(process.ProcessId)
    #subprocess.Popen(##ADD batch file for server here####)

def kill_console(PID):
    os.kill(PID, signal.SIGTERM)

#Server def
def server_restart(): #Restarts the server
    get_processes()
