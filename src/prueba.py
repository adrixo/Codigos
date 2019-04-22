#!/usr/bin/python
from Codigo import *

triple_control = [['x','y','z'],'x','y','z','x+y','x+z','y+z']

TR = Codigo(2, generadora='generadora.txt', nombre="triple_control")
print(TR.matrizControl)
