print('Welcome to the tip calculator')

bill = float(input('Enter the bill for the service: '))
tip = int(input('How many percnet of tip you want to give: '))
split = int(input('How many persons are there: '))


total = (bill + (tip/100)) 
pricePerson = total / split

print(f'The total price of the service is {total} and each person have to pay {pricePerson}')