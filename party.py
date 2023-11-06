#Write a program that acts for user input… and counts down from that number to exactly 1. After it counts down to 1, it says “PARTY TIME!!!”.

#if the number that is input is less than 1, then say “PARTY NOW!!!”-->
userNum = int(input("How long till the party? "))

for x in range(userNum,0,-1):
    print(x)
if userNum < 1:
    print("Party Now!!")
elif x == 1:
    print("Party time!!")


#for(var i = userNum; i > 0; i= i - 1)

