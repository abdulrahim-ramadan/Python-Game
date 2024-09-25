##even = / 2    ---> زوجي
##odd != / 2    ---> فردي

print('Welcome In The Even_odd Game')
print('Please Enetr ANuber ... And Iwill Tell You if it Even or odd')   # code 1
print('If Yor Wanna close The Geme Enetr x ') 


while True:    #loop
    
    number = input('Enter A Number :')

    # code لي غلاق العبة
    if number == 'x':
        print('closing The Game')
        print('Thanks ...')
        
        break # loop لي يقاف 
    
    #even number % 2 = 0

    # try تاكيدالرقم


    try:
        number = int (number)

        if number % 2 == 0 :
            print(' Even Number ')
            
        else:
            print('odd Number')
    except ValueError:
        print('Please Enetr A Valid Number')



    print('-----------------------------')     

        
