import random
import os
import re

""" The getQA proc is used to pull a question from the 'q&a.txt' file, which 
has around 1000 questions with choices and answers.
It sets the variables for question, choices and right answer.
"""
def getQA():
    global answer
    global question
    global choices
    
    # Generating random question number
    file1=open("q&a.txt","r+")
    qnum=random.randint(1,1012)
    qnum=format(qnum,"04")
    lines=file1.readlines()
    qna=""
    question=""
    answer=""
    choices=[]
    
    # Obtaining a question/answer block
    for i,line in enumerate(lines):
        if qnum in line:
            question=question+line
            for j in range(i,i+10):
                qna=qna+lines[j]
                if "Answer:" in lines[j]:
                    answer=lines[j]
                    break
    
    # Extracting the question, choices and answer
    match=re.match("  (#[\d]*) (.*\n.*)",qna)
    question=match.group(2)
    qna1=qna.split("\n")
    for line in qna1:
        if " *" in line:
            matchc=re.match("( \*)(.*)",line)
            choices.append(matchc.group(2))
    match1=re.match("Answer: (.*)",answer)
    answer=match1.group(1)
    

""" The askQ proc is used to ask the question that was generated in getQA().
It obtains the user's answer and performs appropriate action.
"""
def askQ(rec):
    global money
    global flagA
    global flagB
    while money<1000000:
        if rec:
            os.system("cls")
            getQA()
            print("You current safe money is : $"+str(money)+"\n")
            # Print the question and the available choices.
            print(question)
            for i in range(1,5):
                print(str(i)+". "+str(choices[i-1]))
            print("\n")
            if not flagA:
                print("A. Audience Poll")
            if not flagB:
                print("B. 50-50")
            print("Q. Quit the game")
        
        # Obtain the answer and perform required action.
        ans=input("\nEnter your choice : ")
        if ans=="1" or ans=="2" or ans=="3" or ans=="4":
            if answer==choices[int(ans)-1]:
                print("Right answer")
                money=money+100000
                input("Hit Enter to continue")
                askQ(1)
            else:
                print("Sorry, that was wrong. Thank you for playing.")
                print("You have won $"+str(money))
                input("")
                exit()
        elif ans=="A":
            askAudience(answer)
            askQ(0)
        elif ans=="B":
            fiftyFifty(choices.index(answer))
            askQ(0)
        elif ans=="Q":
            print("Thanks for playing.")
            print("You have won $"+str(money))
            input("")
            exit()
        else:
            print("Please choose a correct option")
            askQ(0)


""" The askAudience proc is used to simulate the Ask Audience option.
It displays more poll numbers for the correct answer.
"""
def askAudience(answer):
    global flagA
    percent=[]
    for i,ch in enumerate(choices):
        if ch==answer:
            percent.append(65)
        else:
            percent.append(12)
    print("\nThe answers from the audience were as follows:")
    for i in range(0,4):
        print(str(i+1)+": "+choices[i]+" : "+str(percent[i]))
    print("\nChoose wisely")
    flagA=1


""" The fiftyFifty proc is used to simulate the 50-50 option.
It keeps the right answer and another random option.
"""
def fiftyFifty(answer):
    global flagB
    altCh=random.randint(0,3)
    while altCh==answer:
        altCh=random.randint(0,3)
    print("The remaining choices are:"+str(answer)+str(altCh))
    for i in range(0,4):
        if i==answer or i==altCh:
            print(str(i+1)+": "+choices[i])
    print("\nChoose wisely")
    flagB=1


""" The initGame proc is used to display the opening screen of the game.
It shows the Game's motive and other instructions.
"""
def initGame():
    global money
    global flagA
    global flagB
    flagA=0
    flagB=0
    money=0
    print("Welcome to 'Who wants to be a Millionaire'")    
    print("You have to answer 10 questions to win a million dollars")
    print("Each question that you get right, earns you a $100,000")
    print("You have 2 lifelines to help your self, in case of a tough question")
    print("A. Audience Poll \t\t B. 50-50")
    input("\n\nHit Enter to start the game")
    os.system("cls")


# Main program starts here

initGame()
askQ(1)
if money==1000000:
    print("Congrats!! You're a millionaire now.")