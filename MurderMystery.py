"""
MurderMystery

Description: A murder mystery game. Can you guess who the murderer is or will you get killed? 
"""
import random 
what=input("Would you like to choose names or instantly play?: (choose, play) ")
guesses=0
if what=="choose":
    people=[]
    name=""
    while name!="done":
        name=input("Enter one name at a time or done to finish the list of people ")
        if name=="done":
            break
        people.append(name)
    if len(people)<1 and name=="done":
        people=["trevor", "nikhil", "cejay", "ken"]
    index=len(people)-1
    rand=random.randint(0,index)
    dracula=random.randint(0,10)
    if dracula==5:
        people.append("dracula")
        murderer="dracula"
    else:
        murderer=people[rand]
    print("")
    while len(people)>1:
        print(people)
        print("")
        guess=input("Who is the murderer? ")
        print("")
        if guess==murderer:
            guesses+=1
            print("CAUGHT! The murderer was " + murderer + "!")
            print("It took you " + str(guesses) + " guesses")
            print("")
            break
        else:
            print("Innocent!")
            people.remove(guess)
            guesses+=1
        print("")
    if len(people)==1:
        print("You didn't guess in time, the murderer has KILLED you!")
        print("The murderer was " + murderer)
    elif len(people)==2: 
        print("That was close, the murderer almost got you!")
elif what=="play":
    rand=random.randint(0,1)
    if rand==0:
        names=["alfa", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliet", "kilo", "lima", "mike", "november", "oscar", "papa", "quebec", "romeo", "sierra", "tango", "uniform", "victor", "whiskey", "xray", "yankee", "zulu"]
    elif rand==1:
        names=["alexander","benjamin","christopher","daniel","ethan","fernando","gabriel","henry","isaac","jacob","kevin","liam","mason","noah","owen","parker","quinn","ryan","samuel","tyler","uriel","vincent","william","xavier","yahir","zachary"]
    index=len(names)-1
    person=random.randint(0,index)
    murderer=names[person]
    print("")
    while len(names)>1:
        print(names)
        print("")
        guess=input("Who is the murderer? ")
        print("")
        if guess==murderer:
            guesses+=1
            print("CAUGHT! The murderer was " + murderer + "!")
            print("It took you " + str(guesses) + " guesses")
            print("")
            break
        else:
            print("Innocent!")
            names.remove(guess)
            guesses+=1
        print("")
    if len(names)==1:
        print("You didn't guess in time, the murderer has KILLED you!")
        print("The murderer was " + murderer)
    elif len(names)>1 and len(names)<5: 
        print("That was close, the murderer almost got you!")
    elif len(names)>21 and len(names)<=26:
        print("Wow! You are fast!")
        
