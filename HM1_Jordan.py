# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 19:29:33 2023

@author: Taylor Jordan
"""

#Chapter 2 Question 6 Modify the futval. py program (Section 2. 7) so that the number of years
#for the investment is also a user input. Make sure to change the final
#message to reflect the correct number of years.

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

#Chapter 3 Question 5 The Konditorei coffee shop sells coffee at $10.50 a pound plus the cost
#of shipping. Each order ships for $0.86 per pound + $1.50 fixed cost for
#overhead. Write a program that calculates the cost of an order.

def main():
    print("This program calculates the cost of ordering coffee from Konditorei Coffee Shop!")
    print("Coffee is $10.50/lb plus Shipping Cost. Shipping is $0.86/lb plus $1.50 for Overhead Fees.")
    
    coffee_pounds = float(input("Enter How Many Pounds of Coffee Needed: "))
    
    total_cost = (coffee_pounds * 10.50) + (coffee_pounds * 0.86) + 1.5
    
    print(f"Your subtotal is: ${total_cost:.2f}")

main()

#Chapter 3 Question 6 Two points in a plane are specified using the coordinates (x1,y1) and
#(x2,y2). Write a program that calculates the slope of a line through two
#(non-vertical) points entered by the user.

def calculate_slope(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    if x2 - x1 == 0:
        return "Undefined"

    slope = (y2 - y1) / (x2 - x1)
    return slope

def get_point_input(point_name):
    x = int(input(f"Enter the x-coordinate of {point_name}: "))
    y = int(input(f"Enter the y-coordinate of {point_name}: "))
    return (x, y)


point1 = get_point_input("Point 1")
point2 = get_point_input("Point 2")

print(f"Slope of the line through {point1} and {point2} is:", calculate_slope(point1, point2))

#Chapter 5 Question 4 An acronym is a word formed by taking the first letters of the words in a
#phrase and making a word from them. For example, RAM is an acronym
#for "random access memory." Write a program that allows the user to
#type in a phrase and then outputs the acronym for that phrase. Note: The
#acronym should be all uppercase, even if the words in the phrase are not
#capitalized.

def acronym_generator(phrase):
    words = phrase.split()

    acronym = ''.join([word[0] for word in words]).upper()

    return acronym

phrase = input("Enter a phrase to generate an acronym: ")

print(f"An acronym for \"{phrase}\" is:", acronym_generator(phrase))

#Chapter 5 Question 10 Write a program that calculates the average word length in a sentence
#entered by the user.

def avg_word_length(sentence):
    words = sentence.split()
    total_words = len(words)
    
    total_chars = sum([len(word) for word in words])
    
    average = total_chars / total_words
    return average

sentence = input("Enter a sentence to calculate its average word length: ")

print(f"The average word length in the sentence is: {avg_word_length(sentence):.2f} characters.")

#This program converts a user entered number of minutes into hours and minutes
#Input should ask the user for the number of minutes as a whole number. Decimal
#portions are not allowed. If the user enters an invalid value such as 1.5 or
#"hello", displaying ValueError is sufficient for this exercise.
#The converted hours and minutes should be displayed as whole numbers. Decimal
#portions are not allowed

def hour_min(user_Minutes):
    h = user_Minutes // 60
    m = user_Minutes % 60
    return h, m

def convert_time():
    user_Minutes = int(input('Enter the number of minutes as a whole number: '))
    hours, minutes = hour_min(user_Minutes)
    print(f"{user_Minutes} minutes is equal to {hours} hour(s) and {minutes} minute(s)")

convert_time()
