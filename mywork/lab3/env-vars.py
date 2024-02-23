#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
import os

os.environ["FAV_COLOR"] = input('What is your favorite color? ')
os.environ["NAME"] = input('What is your name? ')
os.environ["GRAD"] = input('Are you graduating this year? ')

print(os.getenv("FAV_COLOR"))
print(os.getenv("NAME"))
print(os.getenv("GRAD"))