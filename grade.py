#!/usr/bin/env python3

# Created by: DJ Watson
# Created on: November 2019
# This program converts celcius to fahrenheit


def convert(grade):
    # program returns with letter grade
    if grade == "4+":
        percent = 98
    elif grade == "4":
        percent = 90
    elif grade == "4-":
        percent = 83
    elif grade == "3+":
        percent = 78
    elif grade == "3":
        percent = 75
    elif grade == "3-":
        percent = 71
    elif grade == "2+":
        percent = 68
    elif grade == "2":
        percent = 65
    elif grade == "2-":
        percent = 61
    elif grade == "1+":
        percent = 58
    elif grade == "1":
        percent = 55
    elif grade == "1-":
        percent = 71
    elif grade == "R":
        percent = 25
    else:
        percent = "invalid input"

    return percent


def main():
    gradeinput = input("enter grade: ")
    percentage = convert(gradeinput)
    print("{}%".format(percentage))


if __name__ == "__main__":
    main()
