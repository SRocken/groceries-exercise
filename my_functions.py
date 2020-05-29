if __name__ == "__main__":

    print("--------------------")
    print("CUSTOM FUNCTIONS EXERCISE...")

# TODO: define temperature conversion function here
#--------------------
#THE CELSIUS TEMP IS: 0 DEGREES
#THE FAHRENHEIT EQUIVALENT IS: 32.0 DEGREES

def celsius_to_fahrenheit(c):
    return(c * (9/5) + 32)
print("--------------------")
c = 14
print("THE CELSIUS TEMP IS:", c, "DEGREES")
f = celsius_to_fahrenheit(c)
print("THE FAHRENHEIT EQUIVALENT IS:", f, "DEGREES")

# TODO: define gradebook function here
#--------------------
#THE NUMERIC SCORE IS: 87.5
#THE LETTER-GRADE EQUIVALENT IS: B+

def numeric_to_letter_grade(number):
    if number < 60:
        return "F"
    elif number < 70:
        return "D"
    elif number < 80:
        return "C"
    elif number < 90:
        return "B"
    else:
        return "A"        

print("--------------------")
score = input("Please input a numeric grade (from 0 to 100): ")
score = float(score)
print("THE NUMERIC SCORE IS:", score)
grade = numeric_to_letter_grade(score)
print("THE LETTER-GRADE EQUIVALENT IS:", grade)




