
#print out 1 to 100 …with the following exceptions:
#for multiples of three, print out “Fizz” instead of the number
#for multiples of five, print out “Buzz” instead of the number
#for multiples of both three and five print “FizzBuzz”-->

#JS>>  for(var i=0; i <= 100; i++){
            #if(i % 5 === 0 && i % 3 === 0)
for x in range (1,100+1,1):
    if x % 3 == 0:
       print("fuzz")

    elif x % 5 == 0:
        print("buzz")

    elif x % 5 == 0 and x % 3 == 0:
        print("fuzzbuzz")

    else:
        print(x)