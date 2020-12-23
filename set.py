# program to learn numerical set

'''
numerical_set={1,2,3,4,4,2}
print(numerical_set)
numerical_set.add(5)
print(numerical_set)
length=numerical_set.__len__()
print(length)
numerical_set.discard(2)
print(numerical_set)
'''
numerical_set0={1,2,3,4,5}
numerical_set1={5,6,7,8,9}
'''
unity=numerical_set0.union(numerical_set1)
print(unity)
intersection=numerical_set0.intersection(numerical_set1)
print(intersection)
difference=numerical_set0.difference(numerical_set1)
print(difference)
simetric_difference=numerical_set0.symmetric_difference(numerical_set1)
print(simetric_difference)
'''
print(numerical_set0.issubset(numerical_set1))
a=int(input())
if a>1:
    print('ok')
else:
    print('not')