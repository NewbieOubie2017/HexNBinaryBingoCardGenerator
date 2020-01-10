import random
from random import randint
import turtle
from turtle import Screen
from turtle import *

def main():
    numberOfCards, choiceOfText, numberAdjust, freeSquareYesNo, number, name = getData()
    
    for i in range(numberOfCards):
        turtle.reset()
        listA = []
        listA = creatData(choiceOfText, number)
        listB = scrambleData(listA)
        drawBingoCard()
        inputData(listB, freeSquareYesNo)
        fileName =  name + str(i + 1) + '.ps'
        print('Your card image is named %s !' % fileName)
        cv = turtle.getcanvas()
        cv.postscript(file=fileName, colormode='color')


def getData():
    try:
        numberOfCards = int(input('How many Bingo cards do you need? '))
    except BaseException:
        pass
    try:
        choiceOfText = int(input('Do you want binary (1), hexadecimal (2) or both numbers (3) on the cards? '))
    except BaseException:
        pass         
    try:
        freeSquareYesNo = input('Do you want a free square in the center of the card? y or n ')
        if freeSquareYesNo[0] in 'Yy':
            numberAdjust = -1                    
            pass
        else:
            freeSquareYesNo = 'n'
            numberAdjust = 0
    except BaseException:
        pass
    numberS = 25 + numberAdjust   
    try:
        number = int(input('Enter the number of choices for the Bingo card\n at least {} not more than 256 '.format(numberS)))
    except BaseException:
        pass
    name = input("Type the file name you want to give to these card(s): ")

    return numberOfCards, choiceOfText, numberAdjust, freeSquareYesNo, number, name


# set up bingo square

def drawBingoCard():
    screen = Screen()
    screen.screensize(1200,1200)


    # Draw large off-white square
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-500, -500)
    color('#000000', '#e4e4ff')
    begin_fill()
    turtle.pendown()
    forward(1000)
    left(90)
    forward(1000)
    left(90)
    forward(1000)
    left(90)
    forward(1000)
    end_fill()
    turtle.penup()


    #draw vertical lines
    turtle.goto(-300, 500)
    turtle.pendown()
    turtle.goto(-300, -500)
    turtle.penup()

    turtle.goto(-100, 500)
    turtle.pendown()
    turtle.goto(-100, -500)
    turtle.penup()

    turtle.goto(100, 500)
    turtle.pendown()
    turtle.goto(100, -500)
    turtle.penup()

    turtle.goto(300, 500)
    turtle.pendown()
    turtle.goto(300, -500)
    turtle.penup()

    # draw horizonal lines
    turtle.goto(-500, -300)
    turtle.pendown()
    turtle.goto(500, -300)
    turtle.penup()

    turtle.goto(-500, -100)
    turtle.pendown()
    turtle.goto(500, -100)
    turtle.penup()

    turtle.goto(-500, 100)
    turtle.pendown()
    turtle.goto(500, 100)
    turtle.penup()

    turtle.goto(-500, 300)
    turtle.pendown()
    turtle.goto(500, 300)
    turtle.penup()

def creatData(choiceOfText, number):
    listPossibles = []

    # Create list of text for Bingo Cards
    if choiceOfText == 1:
        for i in range(number):
            text = bin(i)          
            listPossibles.append(text)
    elif choiceOfText == 2:
        for i in range(number):
            text = hex(i)          
            listPossibles.append(text)
    else:
        for i in range(0, number):
            text = hex(i)          
            listPossibles.append(text)
            text = bin(i)          
            listPossibles.append(text)
    return listPossibles

def scrambleData(listA):
    listA = listA
    listScrambled = []
    # Randomize the list of entries
    numberIterations = len(listA)
    lengthList = numberIterations
    for a in range(numberIterations):
        item = randint(0, lengthList -1)
        listScrambled.append(listA.pop(item))
        lengthList -=1
    return listScrambled

#Input data in squares

def inputData(listScrambled, freeSquareYesNo):
    counter = 0
    startX = -400
    startY = -430
    textXY = ''
    for i in range(5):
        for k in range(5):
            textXY = listScrambled[counter]
            turtle.penup()
            turtle.goto(startX, startY)
            if i == 2 and k ==2 and freeSquareYesNo[0] in 'Yy':
                turtle.goto(0, 0)
                turtle.write('Free', move=False, align="center", font=("New Times Roman", 40, "normal"))
                turtle.penup()
                turtle.goto(0, -60)
                turtle.pendown()
                turtle.write('Space', move=False, align="center", font=("New Times Roman", 40, "normal"))
            else:
                turtle.pendown()
                if len(textXY) > 4:
                    turtle.write(textXY, move=False, align="center", font=("New Times Roman", 24, "normal"))
                else:
                    turtle.write(textXY, move=False, align="center", font=("New Times Roman", 48, "normal"))
            startX += 200
            counter +=1
        startY += 200
        startX = -400
    return 'none'

main()


