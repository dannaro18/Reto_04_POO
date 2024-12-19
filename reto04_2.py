class MenuItem:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_price(self):
        return self._price
    
    def set_price(self, price):
        self._price = price
    
    def calculate_total_price(self):
        return self._price

class Beverage(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self._size = size

    def get_size(self):
        return self._size
    
    def set_size(self, size):
        self._size = size

    def calculate_total_price(self):
        price_multiplier = {"Small": 1, "Medium": 1.2, "Large": 1.5}
        return self._price * price_multiplier.get(self._size, 1)

class Appetizer(MenuItem):
    def __init__(self, name, price, portion_size):
        super().__init__(name, price)
        self._portion_size = portion_size

    def get_portion_size(self):
        return self._portion_size
    
    def set_portion_size(self, portion_size):
        self._portion_size = portion_size

    def calculate_total_price(self):
        portion_multiplier = {"Single": 1, "Double": 2}
        return self._price * portion_multiplier.get(self._portion_size, 1)

class MainCourse(MenuItem):
    def __init__(self, name, price, portion_size):
        super().__init__(name, price)
        self._portion_size = portion_size

    def get_portion_size(self):
        return self._portion_size
    
    def set_portion_size(self, portion_size):
        self._portion_size = portion_size

    def calculate_total_price(self):
        price_multiplier = {"Small": 1, "Regular": 1.5, "Large": 2}
        return self._price * price_multiplier.get(self._portion_size, 1)

class Order:
    def __init__(self):
        self._items = []  
        self._has_main_course = False

    def get_items(self):
        return self._items
    
    def set_items(self, items):
        self._items = items
    
    def add_items(self, items):
        for item in items:
            if isinstance(item, MenuItem): 
                self._items.append(item)
                if isinstance(item, MainCourse):  
                    self._has_main_course = True
    
    def calculate_total_bill(self):
        total = sum(item.calculate_total_price() for item in self._items)
        if self._has_main_course:
            total = sum(item.calculate_total_price() * (0.9 if isinstance(item, Beverage) else 1) for item in self._items)
        return total

    def apply_discount(self):
        total = self.calculate_total_bill()
        if len(self._items) > 5:
            total *= 0.9  # 10% discount
        return total


class Payment:
    def __init__(self, amount, payment_method):
        self._amount = amount  
        self._payment_method = payment_method  

    def get_amount(self):
        return self._amount
    
    def set_amount(self, amount):
        self._amount = amount
    
    def get_payment_method(self):
        return self._payment_method
    
    def set_payment_method(self, payment_method):
        self._payment_method = payment_method

    def process_payment(self):
        print(f"Procesando pago de ${self._amount:.2f} con {self._payment_method}...")
        return f"Pago de ${self._amount:.2f} procesado exitosamente con {self._payment_method}"