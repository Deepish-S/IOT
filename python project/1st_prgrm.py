# i am learning pyhton
'''this is 1st lune in multi line comment
this is 2nd lune in multi line comment
this is 3rd lune in multi line comment
'''

#1. list the set of keywords usinf syntax
import keyword
print("This is the list of keywords :" )
for i in keyword.kwlist:
    print(i)
print("----------------------------------------------")

#2. input a vaiable greetings and print the same
greetings = input("enter your name : ")
print(f"hello {greetings} how you doing today")

print("----------------------------------------------")

#3.write a list the rules of identifiers and give examples
rule_list = """1. the name dosen't start with numbers \n 
2. the name cant contain spaces in  between \n
3. the 1st char in the name can be from A to Z or a to z or underscore '_'\n
 4. keywrds are not allowed and identifier can be of any length \n
 5. special keywords are not allowed\n
 6. every identifier should be unique"""

print(rule_list)
print("----------------------------------------------")

print("These are some examples :")
variable_1 = "hello world"
variable_2 = 23
variable_3 = 2.0
variable_4 = True
print(variable_1,variable_2,variable_3,variable_4)

print("\nvariable type for the variables ")
print(type(variable_1))
print(type(variable_2))
print(type(variable_3))
print(type(variable_4))