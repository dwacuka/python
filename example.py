from pants import Pants 
from pants import SalesPerson
pant_one = Pants('red', 8, 27, 9.28) #Inistaciate an object of class Pants
print(pant_one.color)
print(pant_one.size)
print(pant_one.length)
print(pant_one.price)

pant_one.change_price(67.50) # Call Method change price
print(pant_one.price)

print(pant_one.discount(.1)) # Call method discount()

salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)
print(salesperson.first_name,salesperson.last_name, salesperson.employee_id,salesperson.salary )
salesperson.sell_pants(pant_one)

salesperson.pants_sold[0] == pant_one.color
print(salesperson.pants_sold)

print(part_one.price)
