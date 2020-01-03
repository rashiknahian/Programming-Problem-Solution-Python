#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.


#input name from user
print("Kindly provide us your name")
name = input()

#input age from user
print("kindly provide us your age")
age   =     int(input())

#input year from user
print("Todays Year")
year    =   int(input())

birth_year = year - age
year_100 = birth_year + 100

print("Mr./Ms. %s will be 100 years old on %d"%(name,year_100))