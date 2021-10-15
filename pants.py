class Pants:
    def __init__(self, color, waist_size, length, price):
        self.color = color
        self.size = waist_size
        self.length = length
        self.price = price

    def change_price(self, new_price):
    	self.price = new_price

    def discount(self, discount):
    	return self.price * (1-discount)


# another class
class SalesPerson:
    def __init__(self, first_name, last_name, employee_id, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id= employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self, pants_object):
    	self.pants_sold.append(pants_object) 

    def display_sales(self):
    	for pants in self.pants_sold:
            print('color: {}, waist_size: {}, length: {}, price: {}'\
                .format(pants.color, pants.waist_size, pants.length, pants.price))
    
    def calculate_sales(self):
    	total = 0
    	for pants in self.pants_sold:
        	total += pants.price
        	self.total_sales = total
        	return total

    def calculate_commission(self, percentage):
    	sales_total = self.calculate_sales()
    	return sales_total * percentage 






