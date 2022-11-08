import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "OcU",
    version = "1.1",
    description = "Ocu - Аналитика и автоматизация",
    author = "WebNet OcU",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
