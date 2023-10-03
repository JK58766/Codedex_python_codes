import random

Q = input("Make a Question for our Magic8 Ball: ")

num = random.randint(0, 8)

phrase = [("Yes - definitely."), ("It is decidedly so."),
            ("Without a doubt."), ("Reply hazy, try again."), 
            ("Ask again later."), ("Better not tell you now."),
            ("My sources say no."), ("Outlook not so good."), 
            ("Very doubtful.")]

for num  in range(1):
    print("Magic 8 Ball: ", phrase[num])