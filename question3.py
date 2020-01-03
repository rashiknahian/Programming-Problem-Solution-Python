#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the use

#Take input from user
print("Enter a number")
num = int(input())

#Check wheather it is odd or even
if (num%2==0):
    print("%d is a Even Number"%num)
elif(num%2==1):
    print("%d is a Odd Number"%num)
else:
    print("Invalid Input")