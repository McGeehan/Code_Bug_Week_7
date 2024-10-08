#CODE BUG WEEK 7

def greet(name): #set up function to accept a name withe the name parameter
    print("Hello, " + name + "!")
    
def add_numbers(a, b): #set up function for number addition
    return a + b

#MAIN stuff and variables
name = input("Enter your name: ") #accept the name as a string
greet(name) #call the greet function

num1 = int(input("Enter the first number: ")) #accepting numbers convert to integer
num2 = int(input("Enter the second number: "))#accepting numbers convert to integer

result = add_numbers(num1, num2) #set variable result to the add_numbers func
print("The sum is: " + str(result)) #either convert back to string
print("The sum is: " , result) # or use the Rocco method with comma
