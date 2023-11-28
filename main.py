import random
score=0
lives=3
for n in range(1,11):
    if lives==0:
        print("Game over")
        break

    print(f"Question {n}")
    t=random.randint(1,4)
    if t==1:
        x=random.randint(1,12)
        y=random.randint(1,12)
        print(f"What is {x} + {y}")
        useranwser=int(input("?:"))
        if useranwser==x+y:
            score+=1
            print(f"correct your score:{score}")
        else:
            lives-=1
            print(f"wrong your have {lives} left")
    elif t==2:
        x=random.randint(1,12)
        y=random.randint(1,12)
        print(f"What is {x} - {y}")
        useranwser=int(input("?:"))
        if useranwser==x-y:
            score+=1
            print(f"correct your score:{score}")
        else:
            lives-=1
            print(f"wrong your have {lives} left")
    elif t==3:
        x=random.randint(1,12)
        y=random.randint(1,12)
        print(f"What is {x} * {y}")
        useranwser=int(input("?:"))
        if useranwser==x*y:
            score+=1
            print(f"correct your score:{score}")
        else:
            lives-=1
            print(f"wrong your have {lives} left")
    else:
        P=random.randint(1,12)
        Q=random.randint(1,12)
        x=P*Q
        y=P
        print(f"What is {x} / {y}")
        useranwser=int(input("?:"))
        if useranwser==x/y:
            score+=1
            print(f"correct your score:{score}")
        else:
            lives-=1
            print(f"wrong your have {lives} left")
if lives!=0:
    print("you win")
    print(f"you score is {score}")




