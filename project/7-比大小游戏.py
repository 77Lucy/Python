import random

point1=random.randrange(1,7)
point2=random.randrange(1,7)
point3=random.randrange(1,7)

a_list=[point1,point2,point3]
print(a_list)

if sum(a_list)<=11:
    print('big')
else:
    print('small')
