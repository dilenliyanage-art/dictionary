dict_1 = {'what':2, 'is':2, 'that':2}
print("the oringinal dictionary was"+ str(dict_1))
k = 2
reset = 0
for key in dict_1:
    if dict_1[key] == k:
     reset = reset + 1
print("frequency of two is: "+ str(reset))