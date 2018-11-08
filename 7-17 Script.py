##infile = open('schools.txt','r')
##school = infile.readline().strip()
##print(school)
##school = infile.readline().strip()
##print(school)
##school = infile.readline().strip()
##print(school)
##school = infile.readline().strip()
##print(school)
##              
####=========

infile = open('schools.txt','r')

##for i in range (0,4,1):
##    school = infile.readline().strip()
##    print(school)

##for school in infile:
##    print(school.strip())
##
##

##school = "hi"
##while not school =="":
##    school = infile.readline().strip()
##    print(school)


count = 0



##for school in infile:
##   print(school.strip())
##   count += 1
##print("there are ",count," number of schools")
##



##school = infile.readline().strip()
##while  not school =="":
##    print(school)
##    school = infile.readline().strip()
##    count += 1
##
##    
##print("there are ",count," number of schools")
##
##
infile2 = open('amounts.txt','r')



##for line in infile2:
##    print(line.strip())
##    count += 1
##
##print("There is ", count, " number of amounts")
##

total = 0

for line in infile2:
    num = float(line.strip())
    total += num
    print(num)
    count += 1

    
avg = total/count
print("Total is: ", total)
print( "Average is: ",format(avg,",.1f"))
print("There is ", count, " number of amounts")














