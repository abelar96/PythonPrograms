##Diego Abelar Morales

def distance(s, h):
    return s * h


speed = int(input("What is the speed of the vehicle in mph?: "))
hours = int(input("How many hours has it traveled: "))
print("Hours       Distanced Traveled")
print("------------------------------")
for time in range(1, 1 + hours):
    distance(speed, time)
    print(time, "          ", distance(speed, time))


print("Average mph: ", (speed * hours)/hours)
