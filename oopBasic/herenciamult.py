# -*- coding: utf-8 -*-
"""herenciamult.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/133k6sEHuL8ruI1faRwSuTTdMK5E9R6r4
"""

class A:
  def fun1(self):
   print("the is function 1")

class B:
  def fun2(self):
    print("the is function 2")

class c(A,B):
  def fun3(self):
    print("the is function 3")

obj=c()

obj.fun3()