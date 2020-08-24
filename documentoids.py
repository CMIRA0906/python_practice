
#gender=0

#random_num=random.randint(1800, 2020)
#if(random_num >= 1900 and random_num <= 1999):
#    gender=random.randint(1, 2)
#elif(random_num >= 1800 and random_num <= 1899):
#    gender=random.randint(3, 4)
#elif(random_num >= 2000 and random_num <= 2099):
#    gender=random.randint(5, 6)

#print(gender, random_num)


v1=[6,0,0,0,3,0,3,5,0,5,3,3]
v2=[2,7,9,1,4,6,3,5,8,2,7,9]

lista_multi = []
for a,b in zip(v1, v2):
    lista_multi.append(a*b)
    print(lista_multi)

suma=sum(lista_multi)
print(suma % 11)

