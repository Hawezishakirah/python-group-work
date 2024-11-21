#1.create a class called Car with attributes brand and color.Instantiate an object of the car class and print its attributes
class Car:
    def __init__(self,brand,color):
        
        self.brand = brand
        self.color = color

car = Car("mitsubish", "black")
print(car.brand)
print(car.color)

        
#2.add a method called start_engine to the prints a message saying the engine of the car has started.create an instance of car and call the method.
class Car:
    def __init__(self,brand,color):
        
        self.brand = brand
        self.color = color

    def start_engine(self):
        print(f"The engine of the {self.color} {self.brand} has started.")

car = Car("mitsubish", "black")
car.start_engine()
     
#3.create a class called BankAccount with attributes account_number and balance. Add methods to:
#Deposit an amount.
#Withdraw an amount(only if sufficient balance exists)
#Print the account balance.
class Car:
    def __init__(self,brand,color):
        
        self.brand = brand
        self.color = color

    def start_engine(self):
        print(f"The engine of the {self.color} {self.brand} has started.")

car = Car("Toyota", "Red")
car.start_engine()
# Advanced: Create a class called BankAccount with attributes account_number and balance. Add methods to:
# Deposit an amount.
# Withdraw an amount (only if sufficient balance exists).
# Print the account balance.
class BankAccount:
    def __init__(self,account_number,balance=0):
        
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def display_balance(self):
        print(f"Account balance: {self.balance}")

account = BankAccount(12345)
account.deposit(500)
account.withdraw(200)
account.display_balance()

# Challenge: Implement a class called Library that manages a collection of books. Each book has a title, author, and available status. The Library class should have methods to:
# Add a book to the library.
# Remove a book from the library.
# Check if a book is available by title.
# Borrow a book (mark it as unavailable if it’s available).
# Return a book (mark it as available again if it was borrowed).
class Library:
    def __init__(self):
       
        self.books = []

    def add_book(self, title, author):
        self.books.append({'title': title, 'author': author, 'available': True})

    def remove_book(self, title):
        self.books = [book for book in self.books if book['title'] != title]

    def is_available(self, title):
        for book in self.books:
            if book['title'] == title:
                return book['available']
        return False

    def borrow_book(self, title):
        for book in self.books:
            if book['title'] == title and book['available']:
                book['available'] = False
                return f"You've borrowed {title}."
        return f"{title} is not available."

    def return_book(self, title):
        for book in self.books:
            if book['title'] == title:
                book['available'] = True
                return f"You've returned {title}."
        return f"{title} not found in the library."

library = Library()
library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")
print(library.borrow_book("1984"))
print(library.is_available("1984"))
library.return_book("1984")




