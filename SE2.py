#Second python program on my way to SE
#This is a program to ask user for full name and print it in reverse order with spaces in between each alphabets
#I have also created a my_funtion where i can send a string and return them backward



first_name = input("Enter first name:" )
#Taking users first name as input

Last_name = input("Enter Last name:" )
#Taking users Last name as input

SE = (first_name + Last_name)
#Assigning first name and last name to variable SE 

reversing = SE[: :-1]
#Using [::-1] slice to reverse the inputted name

print (" ".join(reversing))
#Using .join function to add the extra spaces in between the reveresed name

def my_fuction(x): #Creating a function to send string and print it in reverse
    return x [::-1]


function_test = my_fuction("Lets Use slicing string ':-1' as a function to give us a reverse sentence of this statement. ")

print (function_test)



