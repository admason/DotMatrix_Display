## Dot matrix number display 
 
num = int(input('Enter number: '))
elem = input('Enter symbol style: ')
cols=7
#elem = '#'
d=int(5)
for k in range(cols):
    row = [cols*[' '] for line in range(cols)] 


if num ==1:
    for i in range(cols):
        if ptrn[i] == '1':
            row[i][cols-1]=elem #fills column 7
#####################################################
if num ==2:   #
    for i in range(cols):
            row[1][cols-1]=row[2][cols-1]\
            =row[4][0]=row[5][0]=elem #fills column 7
    for j in range(cols):
            row[0][j]=row[3][j]=row[6][j]=elem  
#######################################################           
if num ==3:
    for i in range(cols):
            row[i][cols-1]=elem #fills column 7
    for j in range(cols):
            row[0][j]=row[3][j]=row[6][j]=elem             
######################################################
if num ==7:
    for i in range(cols):
            row[i][cols-1]=elem #fills column 7
    for j in range(cols):
            row[0][j]=elem
######################################################   
else:
    print(f"\nNumber {num} not constructed yet.")
    

    
lines = ["" for lin in range(cols)]
for lin in range(cols):
    lines[lin] += "".join(row[lin])+''
for lin in lines:
    print(lin)
    
