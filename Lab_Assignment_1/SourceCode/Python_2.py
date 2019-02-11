#1.Program to convert list tuples into dictionary
#function to convert the tuple into dictionary
def Convert(tup,di):
    for a,b in tup:
        di.setdefault(a,[]).append(b)
    return di
#here taking static input list of tuples
tups=[('John',('Physics',80)),('Daniel',('Science',90)),('John',('Science',95)),
      ('Mark',('Maths',100)),('Daniel',('History',75)),('Mark',('Social',95))]
#sorting out the tuple before converting into dictionary
tups.sort(key=lambda elem:elem[1])

dictionary={}
dictionary=Convert(tups,dictionary)
print(dictionary)
#print(sorted(dictionary.items(),key= lambda kv:(kv[0][1])))



