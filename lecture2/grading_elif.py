# Variables to represent the grade thresholds
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# Get a test score from the user.
score = int(input('Enter your test score: '))

# Determine the grade.
#important start from the top to the bottom, so from the best to the worse solution/grade
if score >= A_score:
    print('Your grade is A')
elif score >= B_score:
    print('Your grade is B')
elif score >= C_score:
    print('Your grade is C')
elif score >= D_score:
    print('Your grade is D')
else:
    print('Your grade is F')

match score:
    case int(score) if score >=A_score:
        print('Your grade is A')
    case int(score) if score >=B_score:
        print('Your grade is B')
    case int(score) if score >=C_score:
        print('Your grade is C')
    case int(score) if score >=D_score:
        print('Your grade is D')
    case int(score) if score < D_score:
        print('Your grade is E')

