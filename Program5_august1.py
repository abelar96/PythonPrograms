##dictionaryz = {}
##
##listz= ["curly","larry","moe"]
##listz2 = [40,60,80]
##
##for i in range(len(listz)):
##               dictionaryz[listz[i]] = listz2[i]
##               print (dictionaryz)
##
##
##
##keyValue = ""
##
##while keyValue != "quit":
##    keyValue = input("Please enter stooge name: -'quit to exit': ").strip().lower()
##
##    if keyValue == "quit":
##        break
##        
##    print(keyValue)
##    print(keyValue+"'s"+" amount is:",dictionaryz.get(keyValue,"name not found"))
##
##print("That is all")


county_info ={}

infile = open('county2.txt','r')


for line in infile:
        county_list = line.strip().split(',')
        ##print(county_list)
        county_info[county_list[0]] = county_list[1]
        ##print(line.strip())


county_name = ""

while county_name !="Quit":
    county_name = input("Please enter county name - 'quit' to exit: ").strip().title() 
    if county_name == "Quit":
            break
    print(county_info.get(county_name,"County not found"))


print("That is all")

    

