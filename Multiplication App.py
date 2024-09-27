print('welcome In Multiplication App')
print('Please Enetr The First Number And The Last Number of The Multiplication Table')

start = int(input('Enter The First Number of The Table'))
end = int(input('Enter The last Number The Table'))



#for x in range(1,13): # range الرقام

for x in range(start,end+1):
    for y in range (1,13):
   # print(x ,y)
        print(x ,'x', y , '=' , x*y)
        
    print('------------------------') # يجب ان يكون في مواز for




#Example 3 :

#for x in range (1,13) :
    #for i in range (1, 13):
       # print (i, "x",x,"=",i*x)
    #print ('_____________________________')


   
    
