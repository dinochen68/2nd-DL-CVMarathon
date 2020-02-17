def star(num):
        for num in range(num):
            print('*'*(num+1))
            if num<=5:
                print('\n')


a = int(input('Enter * number:'))    
print(star(a))




def fab(num):
        if num == 1:
                return 1
        elif num == 2:
                return 2
        else:
                return fab(num-1)*num

b = int(input('Enter fab number :'))
print(fab(b))        






t = int(input('Enter temperature:'))
if t > 28:
        print('Air conditioner allowed')

elif t < 16:

        print('Heater is allowed')
else:
        print('Weather is comfortable')



        

        
                
                

        


