print("***Welcome to Group 11 BMI Calculator****\n")
print("*******************************")
print("*******************************\n")
#definining a function
def bodymassindex(height, weight):              
#returning BMI rounded off to two decimals
    return round((weight / height**2),2)

print("Greetings Sir/Madam. Whats your name?")
person_name=input("")
gender = input("Enter your gender (M/F): ").upper()
h = float(input("Enter your height in meters: "))
w = float(input("Enter your weight in kg: "))



#call a function
bmi = bodymassindex(h, w)

# Calculate body fat percentage based on gender
if gender == "M":
    body_fat_percentage = (1.20 * bmi) + (0.23 * 20) - 16.2
else:
    body_fat_percentage = (1.20 * bmi) + (0.23 * 20) - 5.4


if bmi <= 18.5:
    bmi_category ="underweight"
elif 18.5 < bmi <= 24.9:
    bmi_category = "Normal weight"
elif 25 < bmi <= 29.29:
    bmi_category = "overweight"
else:
    bmi_category = "obese"

# Categorize body fat percentage using if statements
if gender == "M":
    if body_fat_percentage < 8:
        body_fat_category = "Essential Fat"
    elif 8 <= body_fat_percentage < 25:
        body_fat_category = "Fit"
    elif 25 <= body_fat_percentage < 30:
        body_fat_category = "Acceptable"
    else:
        body_fat_category = "Obese"
else:
    if body_fat_percentage < 20:
        body_fat_category = "Essential Fat"
    elif 20 <= body_fat_percentage < 32:
        body_fat_category = "Fit"
    elif 32 <= body_fat_percentage < 37:
        body_fat_category = "Acceptable"
    else:
        body_fat_category = "Obese"
# Print the calculated BMI, BMI category, body fat percentage, and body fat category
print(f"Your BMI is: {bmi:.2f}")
print(f"You are categorized as: {bmi_category}")
print(f"Your estimated body fat percentage is: {body_fat_percentage:.2f}%")
print(f"You are categorized by body fat as: {body_fat_category}")
print("Thank for using  the BMI calculator.")