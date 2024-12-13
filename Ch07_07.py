def grade_driver_license_exam():
    correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'C', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    
    # Read student's answers from a file (student_answers.txt)
    with open('student_answers.txt', 'r') as file:
        student_answers = [line.strip() for line in file.readlines()]

    correct_count = 0
    incorrect_count = 0
    incorrect_questions = []
    
    # Compare the student's answers with the correct ones
    for i in range(20):
        if student_answers[i] == correct_answers[i]:
            correct_count += 1
        else:
            incorrect_count += 1
            incorrect_questions.append(i + 1)  # Adding 1 to make question number human-readable
    
    # Determine pass/fail
    if correct_count >= 15:
        print("The student passed the exam!")
    else:
        print("The student failed the exam.")
    
    # Display results
    print(f"Correct answers: {correct_count}")
    print(f"Incorrect answers: {incorrect_count}")
    print(f"Incorrect question numbers: {incorrect_questions}")

grade_driver_license_exam()