print('*'*167)
print()
print('\t','\t','\t','\t','\t','\t','\t',' ','Calculator for Square Matrics')
print()
print('*'*167)
print()
print('Instructions for user: ')
print('\t','1. Put matrix of same order for Addition and Substraction')
print()
print('\t','2. Multiplication is only applied on square matrix')
print()
print('\t','3. Seperate values oe each row by space')
print()
n=int(input('enter no of row for the matrics: '))
print()
matrix=[]
for i in range(1,n+1):
    print('enter value of row',i,'matrix 1: ',end='')
    value=input()
    matrix1=value.split()
    matrix.append(matrix1)
for i in range(len(matrix)):    #use this to display list in matrics form
    for j in range(len(matrix[i])):
        print(matrix[i][j],end=' ')
    print()
print()
matrix2=[]
for j in range(1,n+1):
    print('enter value of row',j,'of matrix 2: ',end='')
    value2=input()
    matrix3=value2.split()
    matrix2.append(matrix3)
for k in range(len(matrix2)):    #use this to display list in matrics form
    for l in range(len(matrix2[i])):
        print(matrix2[k][l],end=' ')
    print()
print()
print('OPERATION MENU:','  1.Adition','  2.Substraction','  3.Multiplication','  4.Exit',sep='\n')
print()
count=0
while True:
    a=int(input('select any operation you want to perform: '))
    if a==1:
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                value3=int(matrix[m][n])+int(matrix2[m][n])
                print('\t',value3,end='   ')#for printing values in mtrix form
            print()
        count+=1
    elif a==2:#substraction
        for o in range(len(matrix)):
            for p in range(len(matrix[0])):
                value4=int(matrix[o][p]) - int(matrix2[o][p])
                print('\t',value4,end='   ')# for pring value in matrix form
            print()
        count+=1
    elif a==3:                   #multiplication
        x=matrix
        y=matrix2
        null3=[[0 for t in range(len(y[0]))]for u in range(len(x))]  #initilizing a null list
        if len(x)==len(x[0]):
            for q in range(len(x)): #use 3 nested loop and stored values in empty list
                for r in range(len(x[0])):
                    for s in range(len(y[0])):
                        null3[q][r] = null3[q][r]+(int(x[q][s])*int(y[s][r]))
            for v in range(len(x)):                      #remoce bars and display it in matrix form
                for w in range(len(x[0])):
                    print('\t',null3[v][w],end='   ')
                print()
        else:
            print('Multiplication cannot possible')
        count+=1
    elif a==4:
        print('Thankyou mam')
        break    # i use break statement only in 4 because i want user to press 4 if he want to exit otherwise it will keeps on showing input option 
    else:
        print('kindly select any 4 given options')#if user input value other then 0

