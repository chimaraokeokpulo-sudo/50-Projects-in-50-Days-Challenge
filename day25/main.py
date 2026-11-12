#BOOLEANS A data type with only 2 possible values
#True or False in Python or true or false in Js

is_registered = True
has_paid = False

print(type(has_paid))
#Comparison Opertors produces Boolean results.

#>, <, >=, <=, ===(Js), !==(Js), ==(Equality in Python... Loose equality in Js)
#!= (Inequality in Python... Loose inequality in Js)

age = 17
is_adult = age >= 18
print(is_adult)

#LOGICAL OPERATORS --- They combine conditions.
# /AND/ OR / NOT
age = 20
has_paid = True

if age >= 18 and has_paid:
    print("Access granted...")
else:
    print("Access denied")

    #*****************************
age_text = "20"

age_number = int(age_text)

print(age_number)
print(type(age_text))

# TYPE COERSION

