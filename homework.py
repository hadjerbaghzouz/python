# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16VlKGtlnWOJgRnUwF5mfc-vN1HitQ6ap
"""

password="0123Ab"
data=""
i=0
while data != password and i<10:
    data =input("enter your password")
    i=i+1
if data==password:

      print ("logged in successfully")

else:
      print ("something went wrong")