num=input("Enter Number:")
num=int( num)
for i in range(1,num+1):
    if i%5==0 and i%3==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)