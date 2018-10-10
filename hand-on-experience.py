import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
a = math.pi
b = math.pi


print (int (a))
print(float(b))



# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0,100)

if(i<50):
    print (i)
elif(i>50):
    print (i)


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange','strawberry','banana'])

if (picked_fruit == "orange"):
    print ("the color of the fruit", (picked_fruit), "is Yellow")
elif (picked_fruit == "strawberry"):
    print("the color of the fruit",(picked_fruit),"is Red")
elif(picked_fruit == "banana"):
    print("the color of the fruit", (picked_fruit), "is Yellow")

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.

def multiplies(num1, num2):
    ans = num1 * num2
    return ans

print("12*96=", multiplies(12, 96))
print("48*17=", multiplies(48, 17))
print("196523*87323=", multiplies(196523, 87323))
