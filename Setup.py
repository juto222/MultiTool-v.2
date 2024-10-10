import sys
import os
from PYTHONNNN import main


print("Installation des modules pour mon tool:")

if os.name == 'nt':  
    os.startfile(main.py)
elif os.name == 'posix':  
    os.system(f'open {main.py}')  



if sys.platform.startswith("win"):
    os.system("python -m pip install -r requirements.txt")
    os.system("python main.py")

elif sys.platform.startswith("linux"):
    os.system("python3 -m pip3 install -r requirements.txt")
    os.system("python3 main.py")


if os.name == 'nt':  
    os.startfile(main.py)
elif os.name == 'posix':  
    os.system(f'open {main.py}') 

