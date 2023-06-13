# modules
"""
import important_functions

ans = important_functions.factorial(9)
print(ans)
"""
"""
import important_functions as imp

print(imp.average(10,20,30,50))
"""
"""
from important_functions import palindrome

print(palindrome("Ahmedabad"))
"""
"""
from important_functions import palindrome, average, absoluteSum

print(average(10, 15))
print(absoluteSum(-10, 15))
"""
"""
from important_functions import palindrome as pal, average, absoluteSum as aSum

print(pal("Malayalam"))
"""
"""
from important_functions import *

print(factorial(7))
"""

# import speech_recognition as sr
# import numpy as np
# import pandas as pd

# Wrong way
"""
import myPackage

myPackage.myModule.myFunc()
"""

# from myPackage import myModule
# myModule.myFunc()

# from myPackage import myModule as mm
# mm.myFunc()

# from myPackage.myModule import myFunc
# myFunc()

# myPackage -> subPackage -> subModule -> subFunc()

# from myPackage.subPackage import subModule as sm
# sm.subFunc()

# from myPackage.subPackage.subModule import subFunc
# subFunc()

# from myPackage.subPackage.subModule import subFunc as sf
# sf()


# Some useful built-in modules of Python
