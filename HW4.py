infile = open("student_answers.txt","r")

correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
stud_answers = []
for answers in infile:
    stud_answers.append(answers.strip())
    print("Answers :",answers.strip())

student_answers = infile.readlines()
print("Readlines:",student_answers)
print(stud_answers)    

correct = 0

inc_list = []

if len(stud_answers) == len(correct_answers):
    for i in range(len(stud_answers)):    
        if stud_answers[i] == correct_answers[i]:
            correct +=1
         
else:
    print("Lenght does not match")

qu
qestionMissed = []

if len(stud_answers) == len(correct_answers):
    for i in range(len(stud_answers)):
        if stud_answers[i] != correct_answers[i]:
            MissedQuestion = stud_answers.index()
            questionMissed.append(MissedQuestion)

print("Questions Missed :" ,questionMissed)   
        
print("num correct: ", correct)
