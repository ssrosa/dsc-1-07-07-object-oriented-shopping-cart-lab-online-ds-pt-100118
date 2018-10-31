class ShoppingCart:
	def __init__(self, _total = 0, _items = [], _employee_discount = None):
		self._total = _total
		self._items = _items
		self._employee_discount = _employee_discount

	def get_total(self): #This method works ok
		return self._total

	def set_total(self, amount): #This method works ok
		self._total = amount # (originally had this as += amount, but calling self.total += price
		# seems to send the updated total to this method already)

	total = property(get_total, set_total)

	def get_items(self):  
		return self._items

	def set_items(self, list_of_items): #PROBLEM: why is this method (along with add_item) assigning new list items to the 
	# whole class instead of to an individual instance?
		self._items = list_of_items
		return self.items

	items = property(get_items, set_items)

	def get_employee_discount(self): #This method works ok
		return self._employee_discount

	def set_employee_discount(self, amount): #This method works ok
		self._employee_discount = amount

	employee_discount = property(get_employee_discount, set_employee_discount)

	def add_item(self, name, price, quantity = 1): #PROBLEM: why is this method (along with set_items) assigning new list items to the 
	# whole class instead of to an individual instance?
		item = {'name': name, 'price': price, 'quantity': quantity}
		self._items.append(item)
		self.total += ((price * quantity))
		return self.total

	def list_all_prices(self):  # helper method for mean and median methods. Makes a list of all the prices
	# and lists prices multiply if their quantity is more than 1. This method works ok
		prices = []
#		prices = list(map(lambda item: item['price'] * item['quantity'], self.items))
		for item in self.items:   #for each item in the list of items
			for i in range(item['quantity']): # add the price to list prices as many times as the quantity
				prices.append(item['price'])
		return prices

	def mean_item_price(self): #This method works ok
		all_prices = self.list_all_prices()
		mean = sum(all_prices) / len(all_prices)
		return round(mean, 2)

	def median_item_price(self): #This method works ok
		all_prices = self.list_all_prices()
		median = None
		if len(all_prices) % 2 != 0: #if its odd, find the middle value
			median = all_prices[int(
									round(
											((len(all_prices) / 2) - 1), 0 # middle value, as an integer
										)
									)
								]
		elif len(all_prices) % 2 == 0: #if its even, find the mean of hte middle 2 values
			median = (all_prices[(int(len(all_prices) / 2) - 1)] +
						all_prices[(int(len(all_prices) / 2))]) / 2
		return median

	def apply_discount(self, discount = None): #This method works ok
		if not discount:
			print("Sorry, there is no discount to apply to your cart :(")
		elif discount:
			self.total *= 1.00 - discount
		return self.total

	def item_names(self): #This method works ok
		list_names = []
		for item in self.items:   #for each item in the list of items
			for i in range(item['quantity']): # add the name to list prices as many times as the quantity
				list_names.append(item['name'])
		return list_names

	def void_last_item(self): #This method works ok
		if not self.items:
			print("There are no items in your cart!")
		elif self.items:
			self.total -= self.items[-1]['price']
			self.items.pop()
		return self.total

