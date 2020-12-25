# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 11:16:22 2020

@author: Kieru
"""

"""
fizzbuzz the sololearn
"""
def solo():
    try: 
        n=input("EKA  MBANA KADHAA or 'q' without the quotes to quit!: ")    
        print("Mbana yako ni " + str(n))
        if str(n).lower() =="q":#Converts your input to lower case and checks for quit request
            print("Wazi bazu nimequit. Kimoja!!")
        elif int(n)%3 == 0 and int(n)%5 == 0:
             print("SoloFizz is divisible by 3 yielding " + str(int(n)/3))
             print(" and ")
             print("LearnBuzz is divisible by 5 yielding  " + str(int(n)/5))     
             solo()
        elif int(n)%3==0: #This means if n is divizible by 3 with no remainder.
            print("SoloFizz is divisible by 3 yielding " + str(int(n)/3))
            solo()
        elif int(n)%5 == 0 :
            print("LearnBuzz is divisible by 5 yielding  " + str(int(n)/5))     
            solo()
        else :
            print("!SoloFizzLearnBuzz! is neither divizible by 3 nor is it by 5 Perfectly.(without leaving a remainder thatr is)")
            solo()
    except(ValueError,TypeError):
        print("Error please try again .")
        solo()
solo()
