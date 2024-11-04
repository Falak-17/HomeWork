#1. Creating a List
"""#Exercise: Create a list of 5 of your favorite fruits. Print the list"""
fruits=["apple","banana","mango","watermelon","strawberry"]     #creating a list of fruits
print(fruits)                                                   #printing the list

print()              #printing a blank line to seperate the code of the exercises in the output 

#2. Accessing Elements
"""#Exercise: Given the list colors = ['red', 'blue', 'green', 'yellow', 'purple'], print the first, third, and last color in the list."""
colors=["red","blue","green","yellow","purple"]                 #creating a list of colors
print("First element:", colors[0])                              #printing first element
print("Third element:", colors[2])                              #printing third element
print("Last element:", colors[-1])                              #printing last element

print()              #printing a blank line to seperate the code of the exercises in the output 

#3. Modifying a List
"""#Exercise: Create a list numbers with values [10, 20, 30, 40, 50]. Change the second item to 25 and add 60 to the end of the list. Print the modified list."""
numbers=[10,20,30,40,50]                                        #creating a list of numbers
numbers[1]=25                                                   #changing the second item in the list
numbers.append(60)                                              #adding a number at the end of the list
print(numbers)                                                  #printing the list

print()              #printing a blank line to seperate the code of the exercises in the output 

#4. List Slicing
"""#Exercise: Using the list names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma'], create a new list subset containing only the first three names. Print subset."""
names=["Alice","Bob", "Charlie", "David", "Emma"]               #creating a list of names
subnet=names[:3]                                                #creating the new subnet list 
print(subnet)                                                   #printing the new list

print()              #printing a blank line to seperate the code of the exercises in the output 

#5. Looping through a List
"""#Exercise: Create a list of numbers from 1 to 10 and use a loop to print each number squared."""
numbers=list(range(1, 11))                                      #creating a list of numbers from 1 to 10
for value in numbers:                                           #using for loop
    print(value**2)                                             #printing square of numbers from 1 to 10

print()              #printing a blank line to seperate the code of the exercises in the output

#6. List Methods: Append and Extend
"""#Exercise: Create an empty list called shopping_cart. Add the items 'milk', 'bread', and 'eggs' to it using the .append() method. Then use .extend() to add ['butter', 'cheese'] to the list. Print the final list."""
shopping_cart=[]                                                #creating an empty shopping cart
shopping_cart.append("milk")                                    #adding items in the cart
shopping_cart.append("bread")                                   #adding items in the cart
shopping_cart.append("eggs")                                    #adding items in the cart
extra_ingredients=["butter","cheese"]                           #creating new list of items
shopping_cart.extend(extra_ingredients)                         #extending the shopping cart by adding new list
print(shopping_cart)                                            #printing the final list

print()              #printing a blank line to seperate the code of the exercises in the output

#7. Finding Maximum and Minimum in a List
"""#Exercise: Write a program to find the maximum and minimum values in the list numbers = [45, 22, 88, 56, 92, 33]"""
values=[45, 22, 88, 56, 92, 33]                                 #creating list of values
print("Maximum age:", max(values))                              #printing maximum value
print("Minimum age:", min(values))                              #printing manimum value

print()              #printing a blank line to seperate the code of the exercises in the output

#8. Counting Occurrences
"""#Exercise: Given the list letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd'], count how many times the letter 'a' appears in the list."""
letters =["a","b","a","c","b","a","d"]                          #creating list of values
count_a=letters.count("a")                                      #counting the occurence of 'a'
print("Count of a:", count_a)                                   #printing number of times 'a' occured in the list

print()              #printing a blank line to seperate the code of the exercises in the output

#9. List Comprehension
"""#Exercise: Use list comprehension to create a new list containing the squares of all even numbers from 0 to 10. Print the resulting list."""
squares_of_even_numbers=[x**2 for x in range(11) if x % 2 == 0] #using for loop and if statement
print(squares_of_even_numbers)                                  #printing square of even numbers

print()              #printing a blank line to seperate the code of the exercises in the output

#10. Removing Duplicates
"""#Exercise: Given the list nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7], write a program to remove duplicates and print the unique elements only."""
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]                           #creating list of numbers
unique_nums=list(set(nums))                                     #removing duplicates by converting to a set
print(unique_nums)                                              #printing unique numbers only