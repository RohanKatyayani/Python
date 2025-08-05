# Day - 1
# Core Python + Logic building Fundamentals

print("Let's try and code Python everyday!") #Just a simple print statement that prints anything there is in the quotations.

name = input("What is your name? ") #Takes input from the user
age = int(input("How old are you? ")) #Changes the datatype of the input
year = 2025 + (100 - age) #Declare a variable and give it any value

print("Welcome", name + "! you are", age, "years old", "and you will turn 100 in the year", year )
print(type(age)) #Print to know the datatype of any variable

repeat = int(input("How many times should I print this message? \n"))
for i in range(repeat):
    ''' 
    
    This is a for loop, loops are the heart of automation. The for loop runs for n number of times until the
    condition is true or satisfied.
       
    This specific loop will run the loop n number of times as inputted by the user. 
    "for i" means for that for the amount of times the loop will run as entered by the user, 
    i is just a standing variable to represent the number of times which can be replaced with anything
    as it's just a place holder. 
    Traditionally (i = index)  try using _ instead of i if you don't care about the variable.  
     
    '''
    print(name + "You'll turn 100 in the year", year)

# Let's write a logic now.
number = int(input("Enter a number: - ")) # This will allow the user to enter a number.
try:
    '''
    
    The try block will give an attempt to execute the code inside it. If the code runs,
    well and good! If not, instead of throwing errors which the user won't understand,
    it will give a statement which we print inside the except block so that the user
    will understand what mistake they made while entering the required inputs.   
     
    '''
    if number % 2 == 0:
        '''
    
        An "if" - "else" is a conditional statement which is used in logic quite often.
        it's as simple as it sounds, if the block of code in "if" is true, it will be executed.
        "else" it will be skipped and the block of code in else will be executed. 
     
        '''
        print(number, "is a Even number.")
    else:
        '''
        
        else will execute only if, "if" doesn't satisfy. For eg: if the number entered by the
        user is 15 which is not divisible by 2 hence doesn't satisfy our criteria for "if" will 
        jump straight into else and execute else and print that the number is an Odd number.
        As we know if a number os not even it will be odd.    
        
        '''
        print(number, "is an Odd number.")
except:
    '''
    
    The except block will be executed if and only if the try block has failed to satisfy the 
    requirement of the code. For eg: when the user enters a special character or any alphabet
    which is not classified as a number this specific block will be executed in order to make
    sure that the user who has nothing to do with programming doesn't fall into errors which
    they won't understand and instead get a simple english statement to understand what they
    did wrong which is coded below by us.    
    
    '''
    print("Sorry, this is not a valid number!")


# Alright! Now let's use everything we've learned today and build a Calculator but before that,
# we will ask the user if they want to use a calculator or not and put the entire code in an if
# else block!

calc = input("Would you like to use a Calculator? (y/n): - ").lower()
# .lower() is an inbuilt python function which converts any user input into lower case for us to make
# it easier for the program to understand what it is.

if calc == "y":
    print("Simple Calculator!")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Choose an operation (+, -, *, /): ")

    if op == "+":
        print(a + b)
    elif op == "-":
        '''
        
        elif is used when there are more than two conditions which can be true in the following
        program just like this one has 4 conditions, + - * / and any of these 4 can be true which
        is why we elif = else if to make it as alternate choices. 
         
        '''
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        if b != 0:
            print(a / b)
        else:
            print("Cannot divide by zero!")
    else:
        print("Invalid operation!")

elif calc == "n":
    print("No worries, Have a great day!")

else:
    print("Invalid Input!")

# AWESOME! Day 1 is a BOOM! Let's keep this going and We will be coding like we dream in no time!