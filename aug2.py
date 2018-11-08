#Aug2

set1 = {"curly","larry","moe"}
stoogelist = ["curly","larry","moe"]

set2=set(stoogelist)

print(set2)
#
emptyDict = {}#empty dictionary
emptySet = set()  #emptySet

set1.add("shemp")



print("set1:",set1)

#=======



##s1 = set('abcdefg')

s1 = {'a','b','c','d','e','f','g'}

print("s1:",s1)


s2 = set('efghojklmnp')

s3union = s1 | s2   ##union (Combining both that are shared)

print("========= union", s3union)

lunion = list(s3union)

print(lunion)

lunion.sort()

print(lunion)

s3intersect = s1 & s2 ##intersection (Items shared by both)

print("intersect: ", s3intersect)

s3difference = s1 - s2    ##difference (all items in set 1, except the ones also in set2

print("difference: ", s3difference)

s3symmetric_difference = s1 ^ s2   ##symmetric difference (values of s1 & s2 that are different) 

print("symmetric difference: ", s3symmetric_difference)





print("========== Serialization =======")



import pickle #used for serialization


dictionaryz = {}

dictionaryz["curly"] = 40
print(dictionaryz)

listz = ["curly", "larry", "moe"]

listz1 = [40, 60, 80]

for i in range(len(listz)):
    dictionaryz[listz[i]] = listz1[i]
    
print('dictionaryz: ',dictionaryz) 


outfile = open('data.dat', 'wb')

pickle.dump(dictionaryz, outfile)

outfile.close()

print("pickling completed")

dictionaryz["shemp"] = 150
print('new dictionaryz: ',dictionaryz)

infile = open('data.dat', 'rb')

newdictionary = pickle.load(infile)

print("pickled dictionaryz: ", newdictionary)

      
