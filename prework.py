#Question 1:
#Write a function to print "hello_USERNAME!" USERNAME is the input of the                                          function. The first line of the code has been defined as below.

#function w/o return statement
def hello_name(username):
    """Print greeting upon receiving user input"""
    print("hello_" + username.upper() + "!")

hello_name("Sharmain")

#function w/return statement

def hello_name(username):
    """Print greeting upon receiving user input"""
    username = "hello_" + username.upper() + "!"
    return username

print(hello_name("Shar"))


#Question 2:
#Write a python function, first_odds that prints the odd numbers from 1-100                                                and returns nothing.

def first_odds():
    """Print odd numbers 1-100"""
    for num in range(1,100):
        if num % 2 == 1:
            print(num)

first_odds()


#Question 3:
#Please write a Python function, max_num_in_list to return the max number of a                                          given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """Return the max number of a given list"""
#The max() function returns the item with the highest value, or the item with                                             the highest value in an iterable
    maximum_num = max(a_list)
    return maximum_num

a_list = [27,45,92,87,30,67,51]
print(max_num_in_list(a_list))


#Question 4:
#Write a function to return if the given year is a leap year. A leap year is                                         divisible by 4, but not divisible by 100, unless it is also divisible by 400.                                            The return should be boolean Type (true/false).

def is_leap_year(a_year):
    '''
    Return True or False depending on a given year 
    '''
    if a_year % 4 == 0 and a_year % 100 != 0:
        return True
    elif a_year % 400 == 0:
        return True
    else:
        return False
print(is_leap_year(2015))
# It was difficult trying to figure out which year is a leap year to write my                                     conditional statements. The following website defined a leap year in a way that                                            I could understand:                                                                                                  https://bjc.edc.org/Sept2015/bjc-r/cur/programming/3.5-T1PP/projects/checking-for-leap-years.html?topic=nyc_bjc%2F2-conditionals-abstraction.topic&course=bjc4nyc_2015-2016.html&novideo&noassignment#:~:text=(We%20aren't%20making%20this,(not%20divisible%20by%204).  


#Question 5:
#Write a function to check to see if all numbers in list are consecutive numbers.                                        For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not                                         consecutive numbers. The return should be boolean Type.


   
# The sort function sorts the list so its in consecutive order. Once the list is                                       sorted THEN you can check to see if the original list is in order/matches the                                          sorted list

def is_consecutive(a_list):
    """Return true if all numbers in list are consecutive otherwise false """
    pointer = a_list[0]
    for num in a_list:
        if pointer == num:
            pointer += 1
        else:
            return False
    return True
    
a_list = [2,3,4,5,6,7]
print(is_consecutive(a_list)) 