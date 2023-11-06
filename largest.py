#!--ask for a number 4 times: “Number please….”
#using comparison operators and a conditional (in each iteration), determine the current largest number…
#remember to convert from a string to an int!
#say: “The largest number is x”-->
num1 = int(input("Number please..."))
num2 = int(input("Another number please..."))
num3 = int(input("One more mumber please..."))
num4 = int(input("And the last number please..."))
myArray = [num1,num2,num3,num4]
largestNum = 0

for x in myArray:
    if x > largestNum:
        largestNum = x
            
print("The largest number is " + str(largestNum))