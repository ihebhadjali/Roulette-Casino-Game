import os
from random import randrange
from math import ceil
from datetime import date
from datetime import time
from datetime import datetime
from tkinter import *
def DateFonc():
    Days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    Months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    TodayDate = datetime.today()
    print("{}\nDate : {} {} {},{}".format(TodayDate.strftime("Time : %I:%M %p"),Days[TodayDate.weekday()],Months[TodayDate.month],TodayDate.day,TodayDate.year))
print("WELCOME TO MY FIRST PYTHON GAME.\n#### El Casino ####\n")
DateFonc()
PlayerName = input("Write your Full Name Sir : ")
MyMoney=0
while MyMoney<1:
    MyMoney=input("How much money you have Mr.{} :\n> $".format(PlayerName))
    try:
        MyMoney=int(MyMoney)
        assert MyMoney>0
    except AssertionError:
        print("Your Money must be greater than 0.")
        MyMoney=0
        continue
    except TypeError:
        print("Error, Invalid type.")
        MyMoney=0
        continue
MoneyOfStart = MyMoney
while True:
    os.system("cls")
    DateFonc()
    print("\t__________________________\n\t\tNew Round\n\t__________________________\n\tMr.{}\n\tMy Money : ${}\n\t__________________________".format(PlayerName,MyMoney))
    MyNumber=50
    while ((MyNumber<0)or(MyNumber>49)):
        MyNumber=input("Give a number between 0 and 49 : \n> ")
        try:
            MyNumber=int(MyNumber)
            assert MyNumber>0
        except TypeError:
            print("Variable has an incompatible type.")
            MyNumber=50
            continue
        except AssertionError:
            print("The number must be greater than or equal to 0.")
            MyNumber=50
            continue
        else:
            print("Mr. {} Your number is \"{}\" .".format(PlayerName,MyNumber))
    RoundNumber = randrange(50)
    RoundMoney=0
    while ((RoundMoney>MyMoney)or(RoundMoney==0)):
        RoundMoney=input("How much cash will you pay on this round!?\n> $")
        try:
            RoundMoney=int(RoundMoney)
            assert RoundMoney>0
            if RoundMoney>MyMoney:
                raise ValueError("The money you have is not enough.")
        except AssertionError:
            print("Error.")
            RoundMoney=0
            continue
        except TypeError:
            print("Variable has an incompatible type.")
            RoundMoney=0
            continue
        except ValueError:
            RoundMoney=0
            continue
    print("The Number is : {}".format(RoundNumber))
    MyMoney-=RoundMoney
    if RoundNumber==MyNumber:
        MyMoney+=(3*RoundMoney)
        print("You win ${}".format(2*RoundMoney))
    elif RoundNumber%2==MyNumber%2:
        MyMoney+=ceil(RoundMoney/2)
        print("You lost ${}".format(RoundMoney-ceil(RoundMoney/2)))
    else:
        print("You lost ${}".format(RoundMoney))
    if MyMoney==0:
        print("You lost all your money Mr.{}".format(PlayerName))
        fen1 = Tk()
        tex1 = Label(fen1, text='Thanks you for giving me all your money very easily ;P', fg='green')
        tex1.pack()
        bou1 = Button(fen1, text='Exit', command = fen1.destroy)
        bou1.pack()
        fen1.mainloop()
        break
    ask=0
    while ((ask!=1)and(ask!=2)):
        ask = int(input("Do you want to try again?\n\t1 : Try Again\n\t2 : Exit\n>"))
        if ((ask!=1)and(ask!=2)):
            print("Error.")
    if ask==2:
        if MoneyOfStart>MyMoney:
            fen1 = Tk()
            tex1 = Label(fen1, text='Thanks you for giving me your money very easily ;P', fg='green')
            tex1.pack()
            bou1 = Button(fen1, text='Exit', command = fen1.destroy)
            bou1.pack()
            fen1.mainloop()
        else:
            fen1 = Tk()
            tex1 = Label(fen1, text='Thank you for participating in my game.', fg='green')
            tex1.pack()
            bou1 = Button(fen1, text='Exit', command = fen1.destroy)
            bou1.pack()
            fen1.mainloop()
        break
    elif ask==1:
        os.system("cls")
