words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day')
wordsNew = words.replace('day','month')
print wordsNew

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[len(y)-1]

z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
#print z
newList = z[0:len(z)/2]
#print newList
newList2 = z[len(z)/2-1:len(z)-1]
#print newList2 
newList2[0] = newList
print newList2