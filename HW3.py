#Programmer: Diego Abelar Morales

def calc_average(sc1, sc2, sc3):
    return (sc1+sc2+sc3)/3

def determine_grade(score):
        if score >= 90:
           return "A"
        elif score >= 80:
             return "B"
        elif score >= 70:
            return "C"
        elif score >=60:
             return "D"
        else:
             return "F"


score1 = float(input("Enter Test score 1: "))
score2 = float(input("Enter Test score 2: "))
score3 = float(input("Enter Test score 3: "))


print("Score          Letter Grade")
print("-----------------------------")
print(score1,"         ",determine_grade(score1))
print(score2,"         ",determine_grade(score2))
print(score3,"         ",determine_grade(score3))
print("Average Test Score is:", format(calc_average(score1,score2,score3),",.1f"))
print("This program was written by: Diego Abelar Morales ")
