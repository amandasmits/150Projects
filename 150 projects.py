from array import *
import random
import math
import csv
from tkinter import * 

# note, started at challenge 22 due to the first 22 being covered by intro to python class
#challenge 22
'''
print()
firstname = input("please enter your first name in all lower case")
lastname= input("please enter your last name in all lower case")
firstname=firstname.capitalize()
lastname=lastname.capitalize()
fullname=firstname+" "+lastname
print(fullname)
'''

#challenge 23
'''
print()
firstline=input("please type the first line of a nursery rhyme")
starting=int(input("please enter a starting number"))
ending = int(input("please enter an ending number"))
firstlineslice=firstline[starting:ending]
print(firstlineslice)
'''

#challenge 24
'''
print()
word=input("please enter a word")
word=word.upper()
print(word)
'''

#challenge 25
'''
print()
name=input("please enter your name: ")
if len(name)<5:
    lastname=input("please enter your last name: ")
    fullname=name+lastname
    print(fullname.upper())
else:
    print (name.lower())
'''

#challenge 26
'''
vowellist="aeiou"
word=input("please enter a word")
if word[0] in vowellist:
    word=word+"way"
else:
    word=word+word[0]
    word=word[1:]
    word=word+"ay"
print(word)
'''

#challenge 27
'''
number=float(input("please enter a number with a lot of decimal places: "))
print(number*2)
'''

#challenge 28
'''
number=float(input("please enter a number with a lot of decimal places: "))
print(round(number*2,2))
'''

#challenge 29
'''
number=int(input("please enter an integer over 500"))
root=math.sqrt(number)
print(round(root,2))
'''

#challenge 30
'''
print(round(math.pi,5))
'''

#challenge 31
'''
radius=float(input("please enter the radius of a circle"))
area=math.pi*(radius**2)
print (area)
'''

#challenge 32
'''
radius=float(input("please enter the radius of a cylinder"))
depth=float(input("please enter the depth of a cylinder"))
area=math.pi*(radius**2)
volume=area*depth
print(round(volume, 3))
'''

#challenge 33
'''
firstnum=int(input("please enter the first whole number: "))
secondnum=int(input("please enter the second whole number"))
wholenum=firstnum//secondnum
remainder=firstnum%secondnum
print(firstnum, "divided by", secondnum, "is", wholenum, "with a remainder of", remainder)
'''

#challenge 34
'''
value=int(input("1) Square\n2) Triangle\n\nEnter a number:"))
if value ==1:
    oneside=int(input("please enter the length of one of the sides"))
    print("area =", oneside*2)
elif value ==2:
    base=int(input("base: "))
    height=int(input("height: "))
    area=(base*height)/2
    print(area)
else:
    print("not a valid input, please try again")
'''

#challenge 35
'''
name=input("please enter your name:")
for i in range(3):
    print(name)
'''

#challenge 36
'''
name=input("please enter your name:")
times=int(input("how many times would you like it displayed? "))
for i in range(times):
    print(name)
'''

#challenge 37
'''
name=input("please enter your name:")
for i in name:
    print(i)
'''

#challenge 38
'''
name=input("please enter your name:")
times=int(input("how many times would you like it displayed? "))
for i in range(times):
    for char in name:
        print(char)
'''

#challenge 39
'''
number=int(input("please enter a number between 1 and 12"))
for i in range(1,number+1):
    print(number,"times", i ,"=", number*i)
'''

#challenge 40
'''
number=int(input("please enter a number below 50"))
for i in range(number):
    print(number-i)
'''
#challenge 41
'''
name=input("please enter your name: ")
number= int(input("please enter a number"))

if number<10:
    for i in range(number):
        print(name)
else:
    for i in range(3):
        print("try again too high")
'''

#challenge 42
'''
total =0
for i in range(5):
    number=int(input("please enter a number"))
    yesno=input("would you like this number added?(y/n)")
    if yesno=="y":
        total+=number
print(total)
'''

#challenge 43
'''
direction=input("what direction do you want to count in? ")

if direction == "up":
    topnumber=int(input("please enter the top number"))
    for i in range(topnumber):
        print(i+1)
elif direction == "down":
    num=int(input("please enter a number below 20: "))
    for i in range(20-num+1):
        print(20-i)
else:
    print("I don't understand")
'''

#challenge 44
'''
guests=int(input("how many guests would you like to invite? "))
if guests<10:
    for i in range(guests):
        name=input("please enter the name: ")
        print(name, "has been invited")
else:
    print("too many people")
'''
#challenge 45
'''
total=0
while total<=50:
    tobeadded=int(input("enter the number you would like added"))
    total+=tobeadded
print("your total is:", total)
'''
#challenge 46
'''
num=0
while num<5:
    num=int(input("please enter number"))
print("the last number you entered was:", num)
'''

#challenge 47
'''
cont=True
num1=int(input("please enter a number"))
num2=int(input("please enter another number"))

num3=num1+num2
while cont==True:
    yesno=input("would you like another number?")
    if yesno=="y":
        num4=int(input("enter another number"))
        num3+=num4
    else:
        break
print(num3)
'''
 
#challenge 48
'''
ask=True
counter=0
while ask==True:
    name=input("enter the name of someone you want to invite: ")
    print(name, "has been invited")
    counter+=1
    yesno=input("would you like to invite someone else?")
    if yesno== "n":
        ask=False
print(counter)
'''

#challenge 49
'''
compnum=50
num=int(input("please enter a number"))
counter=0
while num != compnum:
    if num >compnum:
        print("guess is too high")
        num=int(input("please enter a number"))
        counter+=1
    else:
        print("guess is too low")
        num=int(input("please enter a number"))
        counter+=1

print("well done, you took", counter, "attempts")
'''

#challenge 50
'''
num=int(input("please enter anumber between 10 and 20"))
while num not in range(10,20):
    if num<10:
        print("num not in range, try again")
        num=int(input("please enter anumber between 10 and 20"))
    else:
        if num>20:
            print("num not in range, try again")
            num=int(input("please enter anumber between 10 and 20"))
print("thank you")
'''

#challenge 51
'''
for i in range(10):
    print("There are", 10-i, "green bottles on the wall,", 10-i, "green bottles, and if 1 green bottle should accidentally fall...")
    guess=int(input("how many bottles are left on the wall?"))
    while guess!= 10-i-1:
        print("no try again")
        guess=int(input("how many bottles are left on the wall?"))
print("There are no more bottles on the wall")
'''

#challenge 52
'''
num=random.randint(1,100)
print(num)
'''

#challenge 53
'''
fruit=random.choice(["apple", "banana", "peach", "raspberry", "melon"])
print(fruit)
'''

#challenge 54
'''
computerchoice=random.choice(["h", "t"])
choice=input("h or t")
if choice==computerchoice:
    print("you win")
else:
    print("bad luck")
print("the computer chose", computerchoice)
'''

#challenge 55
'''
computerchoice=random.choice([1,2,3,4,5])
choice=int(input("please enter a number between 1 and 5"))
if choice == computerchoice:
    print("well done")
else:
    if choice>computerchoice:
        print("too high")
    else:
        print("too low")
    newchoice=int(input("please enter a number between 1 and 5"))
if newchoice==computerchoice:
    print("correct")
else:
    print("you lose")
'''

#challenge 56
'''
num=random.randint(1,10)
guess=int(input("guess a number between 1 and 10"))
while guess!=num:
    print("try again")
    guess=int(input("guess a number between 1 and 10"))
print("correct")
'''

#challenge 57
'''
num=random.randint(1,10)
guess=int(input("guess a number between 1 and 10"))
while guess!=num:
    if guess>num:
        print("too high, try again")
    else:
        print("too low, try again")
    guess=int(input("guess a number between 1 and 10"))
print("correct")
'''

#challenge 58
'''
correct=0
for i in range(5):
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    print("what is",num1,'+',num2)
    guess=int(input(": "))
    if (num1+num2)==guess:
        correct+=1
print("you got", correct, "out of 5")
'''

#challenge 59
'''
colour=random.choice(["blue", "green", "purple", "pink", "orange"])
guess=input("pick either blue, green, purple, pink, or orange")
if guess == colour:
    print(guess)
while guess!= colour:
    if colour == "blue":
        print("you look BLUE with sadness")
    elif colour == "green":
        print("trees sure are nice and GREEN this year")
    elif colour == "purple":
        print("skittles that are PURPLE definitely exist")
    elif colour == "pink":
        print("someone with PINK hair has hair that is pink")
    else:
        print("if the sky isn't blue it's prolly cuz it's ORANGE")
    guess=input("pick either blue, green, purple, pink, or orange")
print("you got it! (which is not that impressive because we gave you the answer but whatever")
'''

#challenge 69
'''
countries=("canada", "america", "england", "portugal", "france")
print(countries)
choice=input("please enter one of the countries in this list: ")
print(countries.index(choice))
'''

#challenge 70
'''
countries=("canada", "america", "england", "portugal", "france")
print(countries)
choice=input("please enter one of the countries in this list: ")
print(countries.index(choice))
choice=int(input("please enter a number"))
print(countries[choice])
'''

#challenge 71
'''
sports=["volleyball", "tennis"]
print(sports)
toadd=input("please enter a sport to add to the list")
sports.append(toadd)
sports.sort()
print(sports)
'''
#challenge 72
'''
subjects=["math", "english", "gym", "history", "geography", "drama"]
todelete=input("which subject is your least favourite")
subjects.remove(todelete)
print(subjects)
'''

#challenge 73
'''
ind=1
fooddict={}

toadd=input("please enter a favourite food")
fooddict[1]= toadd

toadd=input("please enter a favourite food")
fooddict[2]= toadd

toadd=input("please enter a favourite food")
fooddict[3]= toadd

toadd=input("please enter a favourite food")
fooddict[4]= toadd

print(fooddict)
toremove=int(input("please enter which food you would like to remove"))
del fooddict[toremove]
print(sorted(fooddict.values()))
'''

#challenge 74
'''
colourlist = ["blue", "red", "purple", "orange", "green", "cyan", "yellow", "grey", "brown", "blue"]
startingindex = int(input("please enter the first number between 0 and 4"))
endingindex = int(input("please enter the second number between 5 and 9"))
print(colourlist[startingindex:endingindex])
'''

#challenge 75
'''
numlist= ["000", "111", "222"]
for i in range((len(numlist))):
    print (numlist[i])

num = (input("please enter a 3 digit number"))
if num in numlist:
    for i in range(len(numlist)):
        if numlist[i] == num:
            print(i)
else:
    print("not in the list")
'''

#challenge 76
'''
name1 = input("please enter the first name you would like")
name2 = input("please enter the second name")
name3 = input("please enter the third name")
names = [name1, name2, name3]

cont = input("would you like to enter more names (y/n)")
if cont == "y":
    while cont == "y":
        newname = input("another name")
        names.append(newname)
        cont = input("would you like to enter more names (y/n)")
    print(len(names))
else: 
    print(len(names))
'''

#challenge 77
'''
name1 = input("please enter the first name you would like")
name2 = input("please enter the second name")
name3 = input("please enter the third name")
names = [name1, name2, name3]

cont = input("would you like to enter more names (y/n)")
if cont == "y":
    while cont == "y":
        newname = input("another name")
        names.append(newname)
        cont = input("would you like to enter more names (y/n)")
    print(len(names))
else: 
    print(names)
    chosenname = input("please enter a name on this list")
    nameindex = int(names.index(chosenname))
    print (names.index(chosenname))
    stillinvited= input('would you still like this person to come to the party')
    if stillinvited == "no":
        names.remove(chosenname)
    print(names)
'''

#challenge 78
'''
tvlist = ["himym", "greys", "letterkenny", "yellowstone"]

for i in tvlist:
    print (i)

newshow= input("please enter another show")
position = int(input("what position in the list would you like it inserted into"))
tvlist.insert(position, newshow)

for i in tvlist:
    print (i)
'''

#challenge 79
'''
nums = []
num1 = int(input("please enter a number"))
nums.append(num1)
print(nums)
num2 = int(input("please enter a number"))
nums.append(num2)
print(nums)
num3 = int(input("please enter a number"))
nums.append(num3)
print(nums)

last = input("do you still want the last number you entered")
if last == "no":
    nums.remove(num3)
print(nums)
'''

#challenge 80
'''
firstname = input("please enter your first name")
print(len(firstname))
surname = input("please enter your surname")
print(len(surname))

fullname = firstname + " " + surname
print(len(fullname))
'''

#challenge 81
'''
subject = input("please enter your favourite school subject")
newstring = ""
for i in subject:
    newstring+=i
    newstring+="-"
print(newstring)
'''

#challenge 82
'''
poemline = "this is a line from a poem"
startingpoint= int(input("starting point"))
endpoint = int(input("end point"))

section = poemline[int(startingpoint): int(endpoint)]
print(section)
'''

#challenge 83
'''
word = input("uppercase word: ")
while word.isupper() == False:
    print("please try again") 
    word = input("uppercase word: ")
'''

#challenge 84
'''
postcode = input("please type your postal code")
print (postcode[0].upper())
print(postcode[1].upper())
'''

#challenge 85
'''
name = input("name")
vowels = "AEIOUaeiou"
counter =0
for i in name:
    if i in vowels:
        counter+=1
print(counter)
'''

#challenge 86
'''
pass1 = input("please enter password")
pass2 = input("enter it again")

if pass1==pass2:
    print("thank you ")
elif pass1.upper() == pass2.upper():
    print("they must be same case")
else:
    print("incorrect")
'''

#challenge 87
'''
word = input("put in a word")
indexvar = len(word)-1
for i in word:
    print (word[indexvar])
    indexvar-=1
'''

'''
#challenge 88
num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
num3 = int(input("enter a number"))
num4 = int(input("enter a number"))
nums = array('i', [num1,num2,num3,num4])

nums = sorted(nums)
nums.reverse()
print(nums)
'''

'''
#challenge 89
num1 = random.randint(0,10000)
num2 = random.randint(0,10000)
num3 = random.randint(0,10000)
num4 = random.randint(0,10000)
num5 = random.randint(0,10000)

nums = array('i',[num1, num2, num3, num4, num5])
for i in range(len(nums)):
    print(nums[i])
'''

'''
#challenge90
numsaved =0
savedarray = array('i')
while numsaved < 5:
    currint = int(input("please enter a number"))
    if 10<=currint <=20:
        savedarray.append(currint)
        numsaved+=1
    else:
        print("outside of the range")

print("thank you")

for i in range(len(savedarray)):
    print(savedarray[i])
'''

'''
#challenge 91
newarray = array('i', [12, 12, 20, 20, 20])
print(newarray)
checking = int(input("please enter the number you would like to count in the list"))
print("that number appears", newarray.count(checking), "times")
'''

'''
#challenge 92
firstarray = array('i', [])
for i in range(3):
    newnum = int(input("enter an int"))
    firstarray.append(newnum)

secondarray = array('i', [])
for i in range(5):
    newnum = random.randint(0, 10000)
    secondarray.append(newnum)

for i in range(len(secondarray)):
    firstarray.append(secondarray[i])

firstarray = sorted(firstarray)
for i in range(len(firstarray)):
    print(firstarray[i])
'''

'''
#challenge 93
num1=int(input("please enter a number"))
num2=int(input("please enter a number"))
num3=int(input("please enter a number"))
num4=int(input("please enter a number"))
num5=int(input("please enter a number"))
nums = array('i', [num1,num2,num3,num4,num5])
nums = sorted(nums)
print(nums)
remove=int(input("please pick a number to remove"))
nums.remove(remove)
secondarray = array('i', [remove])
'''

'''
#challenge 94
displayarray = array('i', [3,7,2,16,8])
print(displayarray)
correct = False
while correct==False:
    tocheck = int(input("please enter a number to check"))
    for i in range(len(displayarray)):
        if (displayarray[i]==tocheck):   
            correct=True
            print("you did it")
            print(i)
            break
    else:
        print("please try again")
'''

'''
#challenge 95
floatarray = array('f', [10.13, 10.32, 8.64, 5.36, 9.22])
correct = False

while correct ==False:
    num = int(input("please enter a number between 2 and 5"))
    if (2<=num<=5):
        correct=True
        for i in range(len(floatarray)):
            print(round((floatarray[i] / num),2) )

    else:
        print("try again")
'''

'''
#challenge 96
newlist = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
'''

'''
#challenge 97
newlist = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
row = int(input("please pick a row"))
col = int(input("please pick a column"))

print(newlist[row][col])
'''

'''
#challenge 98
newlist = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
row = int(input("please pick a row"))
print(newlist[row])
newvalue = int(input("please enter a new value"))
newlist[row].append(newvalue)
print(newlist[row])
'''

'''
#challenge 99
newlist = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
row = int(input("please pick a row"))
print(newlist[row])
col = int(input("which column of that row do you want displayed"))
print(newlist[row][col])
change = input("would you like to change the value (y/n)")
if change == "y":
    new = int(input("please enter what you would like to change it to"))
    newlist[row][col] = new
print(newlist[row])
'''

'''
#challenge 100
newdictionary = {"John": {"N": 3056, "S":8463, "E":8441, "W":2694},"Tom":{"N": 4832, "S":6786, "E":4737, "W":3612}, "Anne":{"N": 5239, "S":4802, "E":5820, "W":1859}, "Fiona":{"N": 3904, "S":3645, "E":8821, "W":2451}}
'''

'''
#challenge 101
newdictionary = {"John": {"N": 3056, "S":8463, "E":8441, "W":2694},"Tom":{"N": 4832, "S":6786, "E":4737, "W":3612}, "Anne":{"N": 5239, "S":4802, "E":5820, "W":1859}, "Fiona":{"N": 3904, "S":3645, "E":8821, "W":2451}}
name = input("please enter a name")
region = input("please enter a region")
print(newdictionary[name][region])
'''

'''
#challenge 102
name1 = input("please enter a name")
age1 = input("please enter their age")
shoe1 = input("please enter their shoe size")

name2 = input("please enter a name")
age2 = input("please enter their age")
shoe2 = input("please enter their shoe size")

name3 = input("please enter a name")
age3 = input("please enter their age")
shoe3 = input("please enter their shoe size")

name4 = input("please enter a name")
age4 = input("please enter their age")
shoe4 = input("please enter their shoe size")

nameageshoe = {name1:{"age":age1, "shoe":shoe1}, name2:{"age":age2, "shoe":shoe2}, name3:{"age":age3, "shoe":shoe3}, name4:{"age":age4, "shoe":shoe4}}

inputname = input("please enter a name")
print(nameageshoe[inputname])
'''

'''
#challenge 103
name1 = input("please enter a name")
age1 = input("please enter their age")
shoe1 = input("please enter their shoe size")

name2 = input("please enter a name")
age2 = input("please enter their age")
shoe2 = input("please enter their shoe size")

name3 = input("please enter a name")
age3 = input("please enter their age")
shoe3 = input("please enter their shoe size")

name4 = input("please enter a name")
age4 = input("please enter their age")
shoe4 = input("please enter their shoe size")

nameageshoe = {name1:{"age":age1, "shoe":shoe1}, name2:{"age":age2, "shoe":shoe2}, name3:{"age":age3, "shoe":shoe3}, name4:{"age":age4, "shoe":shoe4}}

for name in nameageshoe:
    print((name), nameageshoe[name]["age"])
'''

'''
#challenge 104
name1 = input("please enter a name")
age1 = input("please enter their age")
shoe1 = input("please enter their shoe size")

name2 = input("please enter a name")
age2 = input("please enter their age")
shoe2 = input("please enter their shoe size")

name3 = input("please enter a name")
age3 = input("please enter their age")
shoe3 = input("please enter their shoe size")

name4 = input("please enter a name")
age4 = input("please enter their age")
shoe4 = input("please enter their shoe size")

nameageshoe = {name1:{"age":age1, "shoe":shoe1}, name2:{"age":age2, "shoe":shoe2}, name3:{"age":age3, "shoe":shoe3}, name4:{"age":age4, "shoe":shoe4}}

toremove = input("please enter the name you would like removed")
del nameageshoe[toremove]

for name in nameageshoe:
    print ((name),nameageshoe[name])
'''

'''
#challenge 105
file = open("numbers.txt", "w")
file.write("1,2,3,4,5")
file.close()
'''

'''
#challenge106
file = open("names.txt", "w")
file.write("claire\n")
file.write("amanda\n")
file.write("patrick\n")
file.write("tammy\n")
file.write("ryker\n")
file.close()
'''

'''
#challenge107
readablefile = open("names.txt", "r")
print(readablefile.read())
'''

'''
#challenge108
newfile = open("names.txt", "a")
newfile.write("opa")
newfile.close()
newfile = open("names.txt", "r")
print(newfile.read())
'''

'''
#challenge109
print("1) Create a new file")
print("2) Display the file")
print("3) Add a new item to the file")
choice = input("pick an option")

if (choice == "1"):
    subject = input("please enter a school subject")
    subject += ".txt"
    subjectfile = open(subject, "w")
    subjectfile.close()
elif (choice == "2"):
    subject = input("please enter a school subject")
    subject += ".txt"
    readsubject = open(subject, "r")
    print(readsubject.read())
elif (choice == "3"):
    subject = input("please enter a school subject")
    subject += ".txt"
    subjectfile = open(subject, "w")
    subjectfile.close()
    readsubject = open((subject), "r")
    print(readsubject.read())
else:
    print("not a valid input")
'''
'''
#challenge110
newfile = open("names.txt", "r")
print(newfile.readlines())
toaddarray = newfile.readlines()
for i in toaddarray:
    print(i)
inputname = input("please enter name")
if inputname in toaddarray:
    toaddarray.remove(inputname)
brandnewfile = open("names2.txt", "w")
for i in range(len(toaddarray)):
    brandnewfile.write(toaddarray[i])
'''


'''
#challenge 111
file = open("Books.csv", "w")
newline = "Book, Author, Year Released\n"
file.write(str(newline))
newline = "To Kill A Mockingbird, Harper Lee, 1960\n"
file.write(str(newline))
newline = "A Brief History of Time, Stephen Hawking, 1988\n"
file.write(str(newline))
newline = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
file.write(str(newline))
newline = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
file.write(str(newline))
newline = "Pride and Prejudice, Jane Austen, 1813\n"
file.write(str(newline))
file.close()
'''

#challenge 112
'''
file = open("Books.csv", "a")
newline = input("please enter a record to add")
newline +="\n"
file.write(str(newline))
file.close()
'''

#challenge 113
'''
file = open("Books.csv", "a")
numberoflines = int(input("how many new records would you like to add"))
for i in range(numberoflines):
    newline = input("please enter a record to add")
    newline +="\n"
    file.write(str(newline))    

file.close()
'''
'''
#challenge 114
start = int(input("please enter the starting year"))
end = int(input("please enter the final year"))

file = list(csv.reader(open("Books.csv", "r")))
listmode = []
for row in file:
    listmode.append(row)

for i in range(len(listmode)):
    if ((int(listmode[i][2]) <= end) and  (int(listmode[i][2])>= start)):
        print(listmode[i])
'''

#challenge 115
'''
file = list(csv.reader(open("Books.csv", "r")))
listmode = []
for row in file:
    listmode.append(row)

for i in range(len(listmode)):
    print(listmode[i], i+1)
'''

#challenge 116
'''
file = open("Books.csv", "w")
newline = "Book, Author, Year Released\n"
file.write(str(newline))
newline = "To Kill A Mockingbird, Harper Lee, 1960\n"
file.write(str(newline))
newline = "A Brief History of Time, Stephen Hawking, 1988\n"
file.write(str(newline))
newline = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
file.write(str(newline))
newline = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
file.write(str(newline))
newline = "Pride and Prejudice, Jane Austen, 1813\n"
file.write(str(newline))
file.close()

file = list(csv.reader(open("Books.csv", "r")))
listmode = []
for row in file:
    listmode.append(row)

print(listmode)
rowtochange = int(input("please enter which row you would like changed"))
newinfo = input("please enter what new info you would like in that row")
listmode[rowtochange]= newinfo

rowtodelete = int(input("please enter the row you would like to delete"))
listmode.remove(listmode[rowtodelete])

file = open("Books.csv", "w")
for row in listmode:
    file.write(str(row))
'''

'''
#challenge 117
name = input("please enter name")
file = open("mathcsv.csv", "w")
writestring =  name + "\n"
file.write(writestring)

def ask():
    addorsubtract = random.randint(0,1)
    element1 = random.randint(1,1000)
    element2 = random.randint(1,1000)

    
    if addorsubtract ==1:
        realans = element1 + element2
        print(element1, "+", element2)
        ans = input()
        element1 = str(element1)
        element2 = str(element2)
        writestring= element1 + ",+," + element2 + "," + ans + "\n"
        file.write(writestring)
    else:
        realans = element1 - element2
        print(element1, "-", element2)
        ans = input()
        element1 = str(element1)
        element2 = str(element2)    
        writestring= element1 + ",+,"+ element2+ ","+ ans+ "\n"
        file.write(writestring)

for i in range(2):
    ask()
file.close()
'''      

'''
#challenge 118
def savenum():
    num = int(input("enter a number"))
    return num

def count():
    num = savenum()
    for i in range(num+1):
        print(i)
count()
'''


#challenge 119
'''
def pickLowAndHigh():
    low = int(input("please pick a low number"))
    high = int(input("please pick a high number"))
    comp_num = random.randint(low,high)
    return comp_num

def instruction():
    guess = int(input("I'm thinking of a number... (please enter your guess)"))
    return guess

def check(number, guess):
    if number == guess:
        print("yay you got it!")

    while number != guess:
        if (number<guess):
            print("too high, try again")
        else:
            print("too low, try again")
        guess = int(input("Enter your new guess"))

    print("you finally did it!")

number = pickLowAndHigh()
guess = instruction()
check(number,guess)
'''

#challenge 120
'''
print("1) Addition")
print("2) Subtraction")
answer = input("Enter 1 or 2: ")

def one():
    num1 = random.randint(5,20)
    num2 = random.randint(5,20)
    print("please add " + str(num1) + "+" + str(num2))
    ans = int(input("Answer: "))
    return ans, (num1+num2)
def two():
    num1 = random.randint(25,50)
    num2 = random.randint(1,25)
    print("please subtract" + str(num1) + "-" + str(num2))
    ans = int(input("Answer: "))
    return ans, (num1-num2)

def correct(given, correct):
    if (given == correct):
        return True
    return False


if (answer =="1"):
    answers = one()
    if correct(answers[0], answers[1]) == True:
        print("Correct!")
    else: 
        print("Incorrect, the answer is ", answers[1])

elif (answer == "2"):
    answers = two()
    if correct(answers[0], answers[1]) == True:
        print("Correct!")
    else: 
        print("Incorrect, the answer is ", answers[1])

else:
    print("that's not an option, sorry!")
'''
#challenge 121
'''
condition = True
namelist = []

def addname():
    newname = input("Please enter the name you want to add")
    namelist.append(newname)
    return

def changename():
    index = int(input("Please enter the index of the list you would like to change"))
    newname = input("Please enter the name you want to change it to")
    namelist[index] = newname
    return

def removename():
    nametoremove = (input("Please enter the name you would like deleted"))
    namelist.remove(nametoremove)

while condition == True:
    print(namelist)
    print("1) Add a name")
    print("2) Change a name")
    print("3) Delete a name")
    print("4) End the program")
    choice = int(input("Please pick an option"))

    if choice == 1:
        addname()
    elif choice == 2:
        changename()
    elif choice == 3:
        removename()
    elif choice ==4:
        condition = False
        print("Goodbye!")
    else:
        print("invalid option, try again")
'''

#challenge 122
'''
condition = True

while condition == True:
    print("1) Add to file")
    print("2) View all records")
    print("3) Quit program")
    choice = int(input("Enter the number of your selection:"))

    if choice ==1:
        file = open("salaries.csv", "a")
        name = input("Please enter the name")
        salary = input("Please enter the salary")
        writestring = name + "," + salary + ","
        file.write(writestring)
        file.close()
        writestring = ""
    elif choice == 2:
        file = list(csv.reader(open("salaries.csv", "r")))
        listmode = []
        for row in file:
            listmode.append(row)
        print(listmode)
    elif choice == 3:
        condition = False
        print("Goodbye")
    else:
        print("Not a valid option, please try again!")
'''

#challenge 123


