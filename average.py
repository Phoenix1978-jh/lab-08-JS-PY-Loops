##ask for a number 4 times: “Number please….”
##-calculate the average of those 4 numbers
#-remember to convert from a string to an int!
#say: “The average is x”, with x replaced by the actual average of the inputs.

num1 = int(input("Number please..."))
num2 = int(input("Another number please..."))
num3 = int(input("One more mumber please..."))
num4 = int(input("And the last number please..."))

listNums= [num1 , num2 , num3 , num4]
#4 inside range () is the number count that will be used to divide the sum of all numbers entered to get average
for x in range(4):
    avg= sum(listNums) / 4
print("The average is " + str(avg))
