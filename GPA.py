# Function to calculate GPA
def calculate_gpa(total_grade_points, total_credits):
    gpa = total_grade_points / total_credits
    return gpa


# Function to determine grade points
def determine_grade_points(mark):
    if 90 <= mark <= 100:
        return 5.0
    elif 85 <= mark < 90:
        return 4.9
    elif 80 <= mark < 85:
        return 4.7
    elif 75 <= mark < 80:
        return 4.5
    elif 70 <= mark < 75:
        return 4.0
    elif 65 <= mark < 70:
        return 3.5
    elif 60 <= mark < 65:
        return 3.0
    elif 55 <= mark < 60:
        return 2.5
    elif 50 <= mark < 55:
        return 1.5
    elif 45 <= mark < 50:
        return 1.5
    elif 40 <= mark < 45:
        return 1.0
    elif 35 <= mark < 40:
        return 0.5
    else:
        return 0.0


# Function to determine pass or fail
def determine_pass(gpa, passing_gpa):
    if gpa >= passing_gpa:
        return "Pass"
    else:
        return "Fail"


# Main program
def main():
    passing_gpa = 2.5

    while True:
        total_courses = 5
        credits_per_course = 3
        total_credits = total_courses * credits_per_course

        # Personalize the interaction
        student_name = input("Enter your name: ")
        print("\nHello, {}! Let's calculate your GPA.".format(student_name))

        total_grade_points = 0
        course_names = []

        for i in range(total_courses):
            course_name = input("Enter name of course {}: ".format(i + 1))
            course_names.append(course_name)
            mark = float(input("Enter marks for {}: ".format(course_name)))
            grade_points = determine_grade_points(mark)
            total_grade_points += grade_points * credits_per_course

        # Calculate GPA
        gpa = calculate_gpa(total_grade_points, total_credits)

        # Determine pass or fail
        pass_status = determine_pass(gpa, passing_gpa)

        # Display GPA and pass/fail status to the student
        print("\n----- GPA Calculation Result -----")
        print("Student:", student_name)

        for i, course_name in enumerate(course_names):
            print("{}: {} - {:.2f} Grade Points".format(course_name, mark, determine_grade_points(mark)))

        print("\nGPA: {:.2f}".format(gpa))
        print("Pass Status:", pass_status)

        # Ask if the user wants to calculate GPA again
        repeat = input("\nDo you want to calculate GPA again? (yes/no): ")
        if repeat.lower() != "yes":
            print("Thank you for using the GPA calculator. Goodbye!")
            break


# Run the main program
if __name__ == "__main__":
    main()
