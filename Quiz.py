a=input("Do you want to play this Quiz (Yes/No) \n")

if a=="yes":
    print("Start game")
else:
    print("End program")

print("Q1. Which Programing language is good?")
a=print("Python")
b=print("C++")
c=print("Java")
choose=input("Answer : ")
if choose=="a":
    print("Correct answer")
    t=(0+10)
    print(t)
else:
    print("Wrong")
    t=(0-10)
    print(t)

print("Q2. Who is the world richest man and net worth?")
a=print("Mukesh Ambani")
b=print("Elon Musk")
c=print("Virat kholi")
choose=input("Answer : ")
if choose=="b":
    print("Correct answer")
    t=(t+10)
    print(t)
else:
    print("Wrong")
    t=(t-10)
    print(t)

print("Q3. How many players in cricket team ?")
a=print("11")
b=print("15")
c=print("16")
choose=input("Answer : ")
if choose=="b":
    print("Correct answer")
    t=(t+10)
    print(t)
else:
    print("Wrong")
    t=(t-10)
    print(t)

print("Q4. Who is our first prime minister ?")
a=print("Pt. Jawarlal Nehru")
b=print("Mahatama Gandhi")
c=print("Nerender Modi")
choose=input("Answer : ")
if choose=="a":
    print("Correct answer")
    t=(t+10)
    print(t)
else:
    print("Wrong")
    t=(t-10)
    print(t)

print("Q5. World best software campany name?")
a=print("Gogle")
b=print("Adobe")
c=print("Microsoft")
choose=input("Answer : ")
if choose=="c":
    print("Correct answer")
    t=(t+10)
    print(t)
else:
    print("Wrong")
    t=(t-10)
    print(t)
    
print("your Total scroce : ",t)
