#for loop that goes through a range of numbers from 1-100
for i in range(1,101):
    #try block to start the loop and test for errors in the program
    try:
        #if and else statements that find multiples of 3, 5, or both 
        if(i%3==0 and i%5==0):
            print("FizzBuzz")
        elif(i%3==0):
            print("Fizz")
        elif(i%5==0):
            print("Buzz")
        #else in this instance will print numbers that aren't a multiple of 3, 5, or both
        else:
            print(i)
    #exception will display an error message if there's an error in the program
    except Exception as e:
        print (e)

