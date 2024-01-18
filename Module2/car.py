#Written by Tiago Perez

# This is a program to store new vehicle inventory and assist with monthly payments
# Create variable of your favorite car brand

favorite_car_brand = "Audi"

# Create list of 5 of their models from cheapest to most expensive

audi_models = ["Audi A3", "Audi Q3", "Audi A4", "Audi Q5", "Audi A8"]

# Append a 6th model to the list

audi_models.append("Audi Q7")

# Create list of 5 standard colors for all models

audi_colors = ["White", "Black", "Silver", "Blue", "Gray"]

# Replace your last color with a different color

audi_colors[-1] = "Red"

# Create variable of the current new year models

new_year_models = ["A6", "Q6", "Q8"]

# Create MSRP constant number (not string) of each of the models

MSRP_A3 = 35000.00
MSRP_Q3 = 40000.00
MSRP_A4 = 42000.00
MSRP_Q5 = 50000.00
MSRP_A8 = 80000.00

# Create a constant number (not string) for total months in 4yr, 5yr, and 6yr loans

MONTHS_IN_4_YEARS = 48
MONTHS_IN_5_YEARS = 60
MONTHS_IN_6_YEARS = 72

# Create a variable for the guest's name. Be courteous in your upcoming messages :)

guest_name = "Joe Smith"

# Create message variable (with f-string) welcoming customer to your new car store

welcome_message = f"Welcome to our new car store, {guest_name}! Take a look at our latest Audi models and find the perfect car for you"

# Create awesome banner with your brand/name/dealership, however you want to welcome customers

banner_message = f"\t\t\t{guest_name}\n\t\tWelcome to the Future of Cars\n\tDiscover Innovation, Luxury, and Performance!"

# Print awesome banner and welcome message

print(banner_message)

# Using title methods, print the number vehicles in alphabetical order, with the year and available colors.

sorted_models = sorted(audi_models)
print(sorted_models + audi_colors)

# Create a variable that calculates a monthly payment (no interest) for 5yr/60months for the first vehicle

msrp_first_vehicle = MSRP_A3

loan_duration_months = MONTHS_IN_5_YEARS
monthly_payment_no_interest = msrp_first_vehicle / loan_duration_months

# and print that in a nice, kind message. Don't be rude/pushy to the customer :)

print(f"Five months payment (No Interest) Audi A3 for just ${monthly_payment_no_interest}!")

# Do the same thing, but give them 4yr and 6yr options for the same vehicle

loan_duration_months = MONTHS_IN_4_YEARS
monthly_payment_no_interest = msrp_first_vehicle / loan_duration_months
print(f"Four months payment (No Interest) Audi A3 for just ${monthly_payment_no_interest}!")


loan_duration_months = MONTHS_IN_6_YEARS
monthly_payment_no_interest = msrp_first_vehicle / loan_duration_months
print(f"Six months payment (No Interest) Audi A3 for just ${monthly_payment_no_interest}!")

# Lastly, give them a 5yr option for each of the other vehicles, just to see if they are interested

loan_duration_months = MONTHS_IN_5_YEARS

msrp_second_vehicle = MSRP_Q3
monthly_payment_no_interest = msrp_second_vehicle / loan_duration_months
print(f"Five months payment (No Interest) Audi Q3 for just ${monthly_payment_no_interest}!")

msrp_third_vehicle = MSRP_A4
monthly_payment_no_interest = msrp_third_vehicle / loan_duration_months
print(f"Five months payment (No Interest) Audi A4 for just ${monthly_payment_no_interest}!")

msrp_fourth_vehicle = MSRP_Q5
monthly_payment_no_interest = msrp_fourth_vehicle / loan_duration_months
print(f"Five months payment (No Interest) Audi Q5 for just ${monthly_payment_no_interest}!")

msrp_fifth_vehicle = MSRP_A8
monthly_payment_no_interest = msrp_fifth_vehicle / loan_duration_months
print(f"Five months payment (No Interest) Audi Q8 for just ${monthly_payment_no_interest}!")

#Addition of the total price of the first and the last cars.

print(f"The total amount for both cars: Audi A3  and Audi A8 is ${MSRP_A3 + MSRP_A8}")

#Add a 10% off if the customer pays all the amount in one time in the latest car.

print(f"If you purchase the new Audi A8 in one payment, now is ${MSRP_A8/10} off")

#Print the final price with the discount of the last comment.

discount = MSRP_A8/10
print(f"Using the 10% discount, the new Audi A8 is now on ${MSRP_A8 - discount}")
