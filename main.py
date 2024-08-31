grade_scale = {
    "A+": 4.3, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D": 1.0,
    "F": 0.0
}
courses_volume = int(input("Enter how many courses you are taking: "))
courses_grades= []
courses_credits_earned = []

#next variables are to help calculating the formula of GPA
term_sum_grades_credits = 0
term_credits_total = 0
current_cgpa = float(input("Your CGPA: "))
current_credits_total = int(input("Attempted Hours"))
current_sum_grades_credits = current_cgpa * current_credits_total


for i in range(courses_volume):
    courses_grades.append(input(f"grade for course number {i+1}: "))
    courses_credits_earned.append(int(input(f"credit hours for course number {i + 1}: ")))
    term_sum_grades_credits += courses_credits_earned[i] * grade_scale[courses_grades[i]]
    term_credits_total += courses_credits_earned[i]


term_gpa_result = float(term_sum_grades_credits / term_credits_total)
print(f"your GPA for this terms is: {term_gpa_result:.2f}")

current_cgpa = (term_sum_grades_credits + current_sum_grades_credits) / (current_credits_total + term_credits_total)
print(f"CGPA = {current_cgpa:.2f}")