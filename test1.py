def horizontalLine(a):
    print("*"*a)

def twoVerticalLine(a, b):
    for i in range(b):
        print("*" + " "*a + "*")

def verticalLine(a, b):
    for i in range(a):
        print(" "*b + "*")



def number_0(num):
    horizontalLine(num)
    twoVerticalLine(num-2, num-2)
    horizontalLine(num)

def number_1(num):
    verticalLine(num, num)

def number_2(num):
    horizontalLine(num)
    verticalLine(num-4, num-1)
    horizontalLine(num)
    verticalLine(num-4, num-5)
    horizontalLine(num)

def number_3(num):
    horizontalLine(num)
    verticalLine(num-4, num-1)
    horizontalLine(num)
    verticalLine(num-4, num-1)
    horizontalLine(num)

def number_4(num):
    twoVerticalLine(num-2, num-3)
    horizontalLine(num)
    verticalLine(num-3, num-1)

def number_5(num):
    horizontalLine(num)
    verticalLine(num-4, num-5)
    horizontalLine(num)
    verticalLine(num-4, num-1)
    horizontalLine(num)

def number_6(num):
    verticalLine(num-3, num-5)
    horizontalLine(num)
    twoVerticalLine(num-2, num-4)
    horizontalLine(num)

def number_7(num):
    horizontalLine(num)
    verticalLine(num-1, num-1)

def number_8(num):
    horizontalLine(num)
    twoVerticalLine(num-2, num-4)
    horizontalLine(num)
    twoVerticalLine(num-2, num-4)
    horizontalLine(num)

def number_9(num):
    horizontalLine(num)
    twoVerticalLine(num-2, num-4)
    horizontalLine(num)
    verticalLine(num-4, num-1)
    horizontalLine(num)



def add(num):
    verticalLine(num-3, num-3)
    horizontalLine(num)
    verticalLine(num-3, num-3)

def subtract(num):
    horizontalLine(num)



def checkAnswer(a, b, c, d):
    if d == "+":
        if c == a+b:
            return(True)
        else:
            return(False)
    elif d == "-":
        if c == a-b:
            return(True)
        else:
            return(False)



import random
#choosing quantity of problem
print("How many problems would you like to attempt: ")
while True:
    quantity = int(input())
    if quantity > 0:
        break
    elif quantity <= 0:
        print("invalid number, try again")

#choosing digit of problem
print("How wide do you want your digits to be(5 ~ 10)?: ")
while True:
    digit = int(input())
    num = digit
    if digit >= 5:
        break
    elif digit < 5:
        print("invalid width, try again")

for i in range(quantity):
    j = random.randrange(0, 9)
    k = random.randrange(0, 9)
    f = random.randrange(0, 1)   # adding/ subtracting

    if j == 0:
        number_0(digit)
    elif j == 1:
        number_1(digit)
    elif j == 2:
        number_2(digit)
    elif j == 3:
        number_3(digit)
    elif j == 4:
        number_4(digit)
    elif j == 5:
        number_5(digit)
    elif j == 6:
        number_6(digit)
    elif j == 7:
        number_7(digit)
    elif j == 8:
        number_8(digit)
    elif j == 9:
        number_9(digit)
    print()

    if f == 0:
        add(digit)
    elif f == 1:
        subtract(digit)
    print()

    if k == 0:
        number_0(digit)
    elif k == 1:
        number_1(digit)
    elif k == 2:
        number_2(digit)
    elif k == 3:
        number_3(digit)
    elif k == 4:
        number_4(digit)
    elif k == 5:
        number_5(digit)
    elif k == 6:
        number_6(digit)
    elif k == 7:
        number_7(digit)
    elif k == 8:
        number_8(digit)
    elif k == 9:
        number_9(digit)
    print()

    temp = int(input("= "))
    if temp == j + k:
        print("correct!")
    elif temp != j + k:
        print("try again")
    elif temp == j - k:
        print("correct!")
    elif temp != j - k:
        print("try again")