
stooges = [ "curly","larry","moe",]
bankbal = [ 200,300,150,]

for indx in range (len(bankbal)):          
    print(stooges[indx],bankbal[indx])

print("---------------------------------------------")
stooges = stooges + ["shemp","curly jo"]

bankbal = bankbal + [400,1159]

print(stooges,bankbal)
##
##print("---------------------------------------------")
##stooges.append("frank")
##bankbal.append(50)
##
##print(stooges,bankbal)
##
##print("---------------------------------------------")
##
##stname = input("Please eneter a stooge name: ").strip()
##
##
##
##stindex = stooges.index(stname)
##print(stooges[stindex],bankbal[stindex])
##
##print("---------------------------------------------")
##
##backupstooges = stooges
##
##
##stoogesSorted = sorted(stooges)
##print(backupstooges,stoogesSorted)
##
##print("---------------------------------------------")
##
##del stooges[2]
##print(stooges)
##
##stooges.remove("larry")
##print(stooges)
##
##print("---------------------------------------------")
##
##print("High Bank Bal: ", max(bankbal))
##
##print("Min bank balance: ", min(bankbal))
##
##print("total bankbal is: ", sum(bankbal))
##
##print("---------------------------------------------")
##
##stooges.insert(4,"abelar")
##
##print(stooges[4])
##print(stooges)
##
##===========
##
##num_list= []
##x=0
##for i in range(11):
##    num_list.insert(i,i)
##
##print(num_list)
##    
##    
##
##for num in range(0,11,1):
##    num_list.append(num)
##
##print(num_list)    
##
##
##for num in range(11):
##    if num %2 !=0:
##        num_list.append(num)
##    
##
##num_list = [x for x in range (0,11,1)if x %2 !=0]  #Pyhton list comprehension feature
##print(num_list,format(sum(num_list),",.1f"))    
##    
##
##
##print(format(sum([x for x in range (0,11,1)if x %2 !=0]),",.1f"))
##
##
##========================================================================
##list1= [ "curly","larry","moe",]
##tuple1= tuple(list1)
##
##print(tuple1)
##
##
##list2= list(tuple1)
##
##for i in range(len(tuple1)):
##    print(tuple1[i])
##
##infile = open("schools.txt","r")
##
##
##
##colleges =[]
##
##
##for school in infile:
##    colleges.append(school.strip())
##    print ("Schools: ", school.strip())
##
##
##colleges.sort()
##
##sorted_colleges = sorted(colleges)
##
##print("Colleges :",colleges)
##print(sorted_colleges)
##
##
##

##=============================================

##
##stooges_data = [['curly',40,60],['larry',50,100],["moe",]
##

