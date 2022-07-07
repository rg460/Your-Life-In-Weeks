# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# [https://waitbutwhy.com/2014/05/life-weeks.html](https://waitbutwhy.com/2014/05/life-weeks.html)

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old. 

# It will take your current age as the input and output a message with our time left in this format:

# > You have x days, y weeks, and z months left. 

# Where x, y and z are replaced with the actual calculated numbers. 

 

# **Warning** your output should match the Example Output format exactly, even the positions of the commas and full stops. 
# 🚨 Don't change the code below 👇
age = input("What is your current age?");
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# PLAN

# calcualte age inputed in days, weeks and months 
age_as_int = int(age);
# days
age_in_days = age_as_int * 365 
# weeks
age_in_weeks = age_as_int * 52
# months
age_in_months = age_as_int * 12 

# calculate 90 years in days , weeks and months 
# days
ninety_years_in_days = 90 * 365
# weeks
ninety_years_in_weeks = 90 * 52
# months
ninety_years_in_months = 90 * 12 

# calculate the difference in days weeks and months and store in variables 
# days
days_difference = ninety_years_in_days - age_in_days
# weeks
weeks_difference = ninety_years_in_weeks - age_in_weeks
# months
months_difference = ninety_years_in_months - age_in_months

# print days weeks months difference using f string 
print(f"You have {days_difference} , {weeks_difference} weeks and {months_difference} months left.")





 








