import random

computer = random.randint(1, 100)
computer1 = random.randint(1, 50)
computer2 = random.randint(1, 100)

status = True
i = 1
j = 1

while status:
    user = int(input("Enter a number: "))

    if user > computer:
        print("HINT: Lower you search")
    elif user < computer:
        print("HINT: Higher your search")
    else:
        print("CORRECT ANSWER! Next step")
        status = False

while i<=7:
    user = int(input("Enter a number: "))

    if (i==7 and user!=computer1):
        print("YOU LOST!")
    elif user > computer1:
        print("HINT: Lower you search")
    elif user < computer1:
        print("HINT: Higher your search")
    else:
        print("CORRECT ANSWER! Next step")
        break 
    i+=1
        
while j<=7:
    user = int(input("Enter a number: "))

    if (j==7 and user!=computer2):
        print("YOU LOST!")
        break
    if user > computer2:
        print("HINT: Lower you search")
    elif user < computer2:
        print("HINT: Higher your search")
    else:
        print("YOU WON!!")
        break
    j+=1
