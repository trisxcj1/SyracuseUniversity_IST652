# Write a sequence of statements to prompt a user for hours and rate per hour, printing each one, and then to compute gross pay as (hours * rate).
hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = float(hours * rate)
print("Pay: " + str(pay))
