##Diego Abelar Morales


try:
    infile = open("student_answers.txt","r")

    correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    stud_answers = []


    for answers in infile:
        stud_answers.append(answers.strip())

except FileNotFoundError as frf:
    print(frf)        



correct = 0 
inc_answers = []

if len(stud_answers) == len(correct_answers):
    for i in range(len(stud_answers)):    
        if stud_answers[i] == correct_answers[i]:
            correct +=1
        else:
            inc_answers.append(i + 1)
           
else:
    print("Lenght does not match")


      
print("Name of Examinee: Diego Abelar Morales")

print("Score:", (correct/20)*100,"%")

if correct >= 15:
    print("Congatulations, you passed the exam!")
else:
    print("Sorry, you did not pass the exam this time")
    

print("Number Correct: ",correct)


print("Questions Missed: ",inc_answers)


