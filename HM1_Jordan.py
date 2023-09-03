# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 17:35:08 2023

@author: Taylor
"""

#Chapter 2, Programming Exercise 6

def main():
    print("This program calculates the future value")
    print("of your anticipated investment length.")
    
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    investment = eval(input("Enter the investment length: "))
    

    for i in range(investment):
        principal = principal * (1 + apr)

    print("The value in",investment,"years is:", principal)

main()