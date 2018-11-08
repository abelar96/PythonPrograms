##quote = "a rose is a rose is a rose"
##
##newQuote =quote.replace("rose","daisy")
##print(newQuote)
##
##print(quote.find("rose"))
##
##print(quote[2])

##for i in range(0,len(quote)):
##    print(quote[i],end="-")

##print(quote[2:10:2])

##if quote.find("thorn") == -1:
##   print("Quote not found") 

dictionaryz = {}

listz= ["curly","larry","moe"]
listz2 = [40,60,80]

for i in range(len(listz)):
               dictionaryz[listz[i]] = listz2[i]
               print (dictionaryz)



keyValue = ""

while keyValue != "quit":
    keyValue = input("Please enter stooge name: -'quit to exit': ").strip().lower()
    if keyValue == "quit":
        break 
    print(keyValue+"'s"+" amount is:",dictionaryz.get(keyValue,"name not found")) 
    
