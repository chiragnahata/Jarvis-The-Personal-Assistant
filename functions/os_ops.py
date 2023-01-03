import os
import subprocess as sp

paths = {
    'notepad': "C:\\Chirag Nahata\\Program Files\\Notepad\\notepad.exe",
    'calculator': "C:\\Chirag Nahata\\Windows\\System32\\calc.exe",
    'discord': "C:\\Users\\Chirag Nahata\\AppData\\Local\\Discord\\app-0.0.300\\Discord.exe",
    'camera' : 'start microsoft.windows.camera:',
    'cmd' : 'start cmd'
}


def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])


def open_cmd():
    os.system('start cmd')


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.Popen(paths['calculator'])
