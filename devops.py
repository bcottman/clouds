# !/usr/bin/env python
# -*- coding: utf-8 -*-
__coverage__ = 0.00
__author__ = "Bruce_H_Cottman"
__license__ = "MIT License"

""" A sandbox devops implemented in Python.
    Limitations: test only in environment of PyCharm.py
    Environment can vary by language, os, cpu, packages, 
    package versions....
 """

import subprocess as sp
import colorama
from colorama import Fore, Back, Style

colorama.init()
print(colorama.ansi.clear_screen())


def devops_step(serial_script_cmd:str ,nstep:int, return_code: int):
    """ execute devops step logic"""
    rc = -1 # next step return_code
    if return_code == 0:
        child = sp.Popen(serial_script_cmd, shell=True,
                         stdout=sp.PIPE,
                         stderr=sp.PIPE)
        stdout, stderr = child.communicate()
        rc = child.returncode
        print(Back.BLACK + Fore.GREEN+' \nExecuting devops step(', nstep, '): ', serial_script_cmd+ Fore.WHITE)
        print(Style.RESET_ALL)
        print("stdout: ", stdout.decode('utf-8'), "\n stderr: ", stderr.decode('utf-8'), Fore.WHITE)

        if rc == 0:
            print(Back.BLACK + Fore.GREEN+' yes! :Pass Go!!!' + Fore.WHITE)
            nstep += 1
        else:
            print(Back.BLACK + Fore.RED + ' Failed! ', serial_script_cmd, rc, Fore.WHITE)

    return nstep, rc



nstep = 1
return_code = 0
# black pep-8 formatting
serial_script_cmd = 'black -v tests'
nstep,rc = devops_step(serial_script_cmd, nstep, return_code )

######
import uuid

pid = 'branch-' + str(uuid.uuid4())  

serial_script_cmd = 'git checkout -b ' + pid
nstep, rc = devops_step(serial_script_cmd, nstep, return_code)

serial_script_cmd = 'git add -A'
nstep, rc = devops_step(serial_script_cmd, nstep, return_code)
# git commit -m'[message]'
serial_script_cmd = 'git commit -m "sandbox commit that passesd all local unit tests"'
nstep, rc = devops_step(serial_script_cmd, nstep, return_code)
# git push -u origin [branch-name]

serial_script_cmd = 'git config user.email "dr.bruce.cottman@gmail.com"'
nstep, rc = devops_step(serial_script_cmd, nstep, return_code)

#serial_script_cmd = 'git config user.name "bcottman"'
serial_script_cmd = 'git config --list'
nstep, rc = devops_step(serial_script_cmd, nstep, return_code)

serial_script_cmd = 'git push -u main ' + pid
nstep, rc = devops_step(serial_script_cmd, nstep, return_code)

#########

#pytest for tests
serial_script_cmd = 'pytest -v tests'
nstep, rc = devops_step(serial_script_cmd, nstep, return_code)

#coverage
serial_script_cmd = 'coverage run -m pytest tests'
nstep, rc = devops_step(serial_script_cmd, nstep, return_code)

serial_script_cmd = 'coverage report'
nstep, rc = devops_step(serial_script_cmd, nstep, return_code)


#mypy type checking
serial_script_cmd = 'mypy src'
nstep, rc = devops_step(serial_script_cmd, nstep, return_code)

#profile

#pylint
serial_script_cmd = 'pylint src'
nstep, rc = devops_step(serial_script_cmd, nstep, return_code)




