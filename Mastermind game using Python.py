import random
n=int(input("enter 4 digit number:"))
ctr=0
num=random.randrange(1000,10000)
print(num)
if(n==num):
    print("Great")
    print("You guessed the number in just 1 try!")
    print("You're a Mastermind!!!")
else:
    ctr=0
    while n!=num:
        count=0
        n=str(n)
        num=str(num)
        correct=[]
        for i in range(0,4):
            if n[i]==num[i]:
                count+=1
                correct.append(n[i])
            else:
                continue
        if count>0:
            print("Not quit the number.But you did get",count,"digits correct")
            print("These  numbers are correct in your input",' '.join(correct))

        else:
            print("None of the numbers are correct")
        n=int(input("Enter your next choice: "))
        ctr += 1
    if n==num:
        print("You've become a Mastermind!")
        print("it took you only",ctr,"tries.")