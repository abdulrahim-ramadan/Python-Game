print('This Game will Take  Several Numbers And Print The Average of Them')

count =int(input('how Many Numbers would  You Like To Sum : '))    # user عداد لفات .مثال 5لفات

current_count = 0   #متغير قمته بي صفر
summ = 0



while current_count < count :
    number = float(input('Enter The Number : '))
    summ += number
    #print(current_count)
    current_count += 1

#print(summ)
    
print('summ of all Numbers = ' , summ)
print ('Average of all Numbers = ' summ/count) #مجموع /العداد



#print(type(summ))     # معرفة لقيمة
