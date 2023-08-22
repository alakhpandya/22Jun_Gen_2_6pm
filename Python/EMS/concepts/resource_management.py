# f = open("ourBatch.csv", "r+")
# f.close()
"""
with open("ourBatch.csv", "r+") as f:       # same as f = open("ourBatch.csv", "a+")
    print(f.readline())
    print(f.readline())
# print(f.closed)
"""
# Next class: with block mechanism through ContextManager

"""
class Example():
    
    def __enter__(self):
        print("Enter method called")

    def __exit__(self, a ,b, c):
        print("Exit method called")

# e1 = Example()
print("Welcome to our program!")
with Example() as e1:
    print("with block started")
print("See you soon again!")
"""
"""
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    pass
"""
class ContextManager():
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        self.fp = open(self.name, self.mode)
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.fp.close()
        # print(exc_type)
        # print(exc_value)
        # print(traceback)

# name = input("File name with full path: ")
# mode = input("Mode: ")
name = "ourBatch.csv"
mode = "r+"

# a = ContextManager(name, mode)
with ContextManager(name, mode) as a:
    print(a.fp.read())
    print(a.fp.closed)
print(a.fp.closed)