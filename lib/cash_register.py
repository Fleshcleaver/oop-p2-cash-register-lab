#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self._discount = None
        self.discount = discount  # Use property setter for validation
        self.total = 0
        self.items = []
        self.previous_transactions = []
    
    @property
    def discount(self):
        return self._discount
    
    @discount.setter
    def discount(self, value):
        # Ensure discount is an integer
        if not isinstance(value, int):
            print("Not valid discount")
            self._discount = 0
        # Ensure discount is between 0-100 inclusive
        elif value < 0 or value > 100:
            print("Not valid discount")
            self._discount = 0
        else:
            self._discount = value
    
    def add_item(self, title, price, quantity=1):
        # Add price to total
        self.total += price * quantity
        
        # Add item to the items array (once for each quantity)
        for _ in range(quantity):
            self.items.append(title)
        
        # Add an object to previous_transactions with item, price, and quantity
        transaction = {
            'item': title,
            'price': price,
            'quantity': quantity
        }
        self.previous_transactions.append(transaction)
    
    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            # Apply discount as percentage off from total
            self.total = self.total * (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
    
    def void_last_transaction(self):
        # Check if there are any transactions
        if not self.previous_transactions:
            return
        
        # Remove the last transaction from the array
        last_transaction = self.previous_transactions.pop()
        
        # Ensure price reflects correctly
        transaction_total = last_transaction['price'] * last_transaction['quantity']
        self.total -= transaction_total
        
        # Ensure items reflects correctly (remove the items added in that transaction)
        for _ in range(last_transaction['quantity']):
            if last_transaction['item'] in self.items:
                self.items.remove(last_transaction['item'])