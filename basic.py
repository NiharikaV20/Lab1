# -*- coding: utf-8 -*-
"""basic

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12xbdPscdGoWizPAkR7GQAUVsl2Ty702_
"""

def calculator(a,b):
  ask=input("which operation do you want to perform?")
  if ask=="add":
    return a+b
  elif ask=="sub":
    return a-b
  elif ask=="mul":
    return a*b
  elif ask=="div":
    return a/b
  else:
    return "enter add,sub,mul or div as an answer,please."

