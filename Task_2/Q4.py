list1 = [2,3,4,5,6,7,8,9]
list2 = [4,9,16,25,36,49,64,81]
set_list=[]
for p in range(len( list1)):
    set_list.append( tuple( [list1[p], list2[p]] ))
set_list = set( set_list)
print(set_list)
