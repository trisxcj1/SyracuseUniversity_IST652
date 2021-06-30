# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message; otherwise, print a grade based on the given table.
score = float(input("Enter Score: "))

if (score > 1.0):
    print("The entered score is too high. Keep score between 0.0 and 1.0")
    
elif (score <= 1.0) and (score >= 0.9):
    print("Grade: A")

elif (score < 0.9) and (score >= 0.8):
    print("Grade: B")

elif (score < 0.8) and (score >= 0.7):
    print("Grade: C")

elif (score < 0.7) and (score >= 0.6):
    print("Grade: D")

elif (score < 0.6) and (score >= 0.0):
    print("Grade: F")
    
else:
    print("The entered score is too low. Keep score between 0.0 and 1.0")
