import sys
import os
from MultiTool-v.2 import main


print("Installation des modules pour mon tool:")

if os.name == 'nt':  
    os.startfile(main.py)
elif os.name == 'posix':  
    os.system(f'open {main.py}')  


