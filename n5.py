d=int(input('so dong: '))
c=int(input('so cot): '))
for i in range (1,d+1):
    for j in range(1,c+1):
        if ((j==1 or j==c) and i!=d) or (i==d and(j>1 and j<c)):
            print("*",end="") 
        else:
            print(end=" ")
    print()
            
