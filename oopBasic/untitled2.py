# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-PjZXzr9bbDiELjUEb6jSZ1X4CCpvUjl
"""

class person:
  def __init__(self,fname,flast):
    self.__finame=fname
    self.__lastname=flast
  

  def printname(self):
    return self.__finame +" "+ self.__lastname

class Student(person):
 def __init__(self,fname,flast,year):
  super().__init__(fname,flast)
  self.__graduationyear=year

  def welcome(self):
     print("Welcome " + self.printname()+ "to the class of ", self.__graduationyear)

p=person("Jonh","agui")

print(p.printname())

s =Student("gg","gg",3)

s.welcome()