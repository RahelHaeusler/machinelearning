# calculation of the calories for the treadmill

# Constant
calories_per_minute = 4.2

print("Minutes\t\tCalories burned")
print("=====================")

# Calculate the calories burned
for minutes in range(10, 30, 5):
    calories = calories_per_minute * minutes
    print(minutes, "\t\t\t", calories)
