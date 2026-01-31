# fuction that take list of score and calculate average, retuen average score
# fuction that take numerical grade and return symbol grade [A, B, C, D, E]
# fuvtion that take student name and list of score and display the average and letter symbol

def calculate_average(scores):
    return sum(scores) / len(scores)

def get_letter_grade(average):

    if average < 0 and average > 100:
        return "Error: Score can't be negative and cant be over 100 value!! ."

    elif 90 <= average <= 100:
        return "A"
    elif 70 <= average <= 89:
        return "B"
    elif 50 <= average <= 69:
        return "C"
    elif 30 <= average <= 49:
        return "D"
    elif 0 <= average <= 29:
        return "E"
    else:
        return "Error: Invalid value, please try again!!."


def display_report(student_name, scores):
    average = calculate_average(scores)
    grade = get_letter_grade(average)
    # grade = get_letter_grade(average)

    print(f"Student {student_name} has an average score of {average} and grade {grade}")

def main():

    student_name = input("Enter your name: ")
    user = int(input("Enter your score: "))
    
    scores = []
    
    while True:
        if user == -1:
            break
        else:
            scores.append(user)
            user = int(input("Enter your score: "))

    display_report(student_name, scores )


if __name__ == "__main__":
    main()

        





    