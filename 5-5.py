

    
    number=int(input('Введіть необхідну сумму від 10 до 20000, кратну 10:'))
    if number<1 or number>20000 or number /10!=number//10:
             print('Помилка вводу суми')
    else :
             digits=[]
#Отримання тисяч
    thousands=number // 1000
    digits.append(thousands*1000)
#Отримання coтень                      
    hundreds=(number-thousands*1000)//100
    digits.append(hundreds*100)
#Отримання десятків
    tens=(number-thousands*1000-hundreds*100)//10
    digits.append(tens*10)
#Отримання одиниць
    ones=(number-thousands*1000-hundreds*100-tens*10)
    digits.append(ones)
    print(digits)
                    
    thousands=list([2000, 1000])                
    for thousand in thousands:
           q=digits[0]//thousand
           if q>10 and q%2!=0: q=q-2
           print('Купюр номіналом', thousand, 'грн:', q)
           digits[0] =   digits[0]-thousand*q
                    
    hundreds=list([100, 200, 500])                
    for  hundred in  hundreds:
           q=digits[1]// hundred
           if q>10 and q%2!=0: q=q-2
           print('Купюр номіналом',  hundred, 'грн:', q)
           digits[1] =   digits[1]-hundred*q
                    
    tens=list([10, 20, 50])                
    for  ten in  tens:
           q=digits[2]// ten
           if q>10 and q%2!=0: q=q-2
           print('Купюр номіналом',  ten, 'грн:', q)
           digits[2] =   digits[2]-ten*q
    
    
