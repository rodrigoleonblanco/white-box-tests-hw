# -*- coding: utf-8 -*-

"""
White-box code examples.
"""
import re

# 7777777777777777777777777777777
def verify_age(age):
    """
    Determines whether a person is eligible for a certain service based on their age.
    """
    if 18 <= age <= 65:
        return "Eligible"

    return "Not Eligible"


# 111111111111111111111111111111111111111
def validate_credit_card(card_number):
    """
    Validates credit card numbers.
    """
    if 13 <= len(card_number) <= 16 and card_number.isdigit():
        return "Valid Card"

    return "Invalid Card"


# 1555555555555555555555555555555555555555555555555555555555555
def calculate_quantity_discount(quantity):
    """
    Calculates discounts based on the quantity of a product.
    """
    if 1 <= quantity <= 5:
        return "No Discount"

    if 6 <= quantity <= 10:
        return "5% Discount"

    return "10% Discount"


# 19999999999999999999999999999999999999999999999999999999999999999
def grade_quiz(correct_answers, incorrect_answers):
    """
    Grades online quizzes based on the number of correct and incorrect answers.
    """
    if correct_answers >= 7 and incorrect_answers <= 2:
        return "Pass"

    if correct_answers >= 5 and incorrect_answers <= 3:
        return "Conditional Pass"

    return "Fail"

# 22
class VendingMachine:
    """
    A simple vending machine that dispenses drinks.
    It has two states: "Ready" and "Dispensing."
    """

    def __init__(self):
        """
        Defines the vending machine initial state.
        """
        self.state = "Ready"

    def insert_coin(self):
        """
        Function called when a coin is inserted.
        """
        if self.state == "Ready":
            self.state = "Dispensing"
            return "Coin Inserted. Select your drink."

        return "Invalid operation in current state."

    def select_drink(self):
        """
        Function called after selecting a drink.
        """
        if self.state == "Dispensing":
            self.state = "Ready"
            return "Drink Dispensed. Thank you!"

        return "Invalid operation in current state."


# 23
class TrafficLight:
    """
    A traffic light system with three states: "Green," "Yellow," and "Red."
    """

    def __init__(self):
        """
        Defines the traffic light initial state.
        """
        self.state = "Red"

    def change_state(self):
        """
        Function that changes the traffic light state.
        """
        if self.state == "Red":
            self.state = "Green"
        elif self.state == "Green":
            self.state = "Yellow"
        elif self.state == "Yellow":
            self.state = "Red"

    def get_current_state(self):
        """
        Provides the current traffic light state.
        """
        return self.state


# 24
class UserAuthentication:
    """
    A user authentication system with states "Logged Out" and "Logged In."
    """

    def __init__(self):
        """
        Defines the user initial state.
        """
        self.state = "Logged Out"

    def login(self):
        """
        Function to login a user.
        """
        if self.state == "Logged Out":
            self.state = "Logged In"
            return "Login successful"

        return "Invalid operation in current state"

    def logout(self):
        """
        Function to logout a user.
        """
        if self.state == "Logged In":
            self.state = "Logged Out"
            return "Logout successful"

        return "Invalid operation in current state"


# 25
class DocumentEditingSystem:
    """
    A document editing system with states "Editing" and "Saved."
    """

    def __init__(self):
        """
        Defines the initial state.
        """
        self.state = "Editing"

    def save_document(self):
        """
        Function to save a document.
        """
        if self.state == "Editing":
            self.state = "Saved"
            return "Document saved successfully"

        return "Invalid operation in current state"

    def edit_document(self):
        """
        Function to edit a document.
        """
        if self.state == "Saved":
            self.state = "Editing"
            return "Editing resumed"

        return "Invalid operation in current state"


# 26
class ElevatorSystem:
    """
    An elevator system with states "Idle," "Moving Up," and "Moving Down."
    """

    def __init__(self):
        """
        Defines the elevator initial state.
        """
        self.state = "Idle"

    def move_up(self):
        """
        Function to move up the elevator.
        """
        if self.state == "Idle":
            self.state = "Moving Up"
            return "Elevator moving up"

        return "Invalid operation in current state"

    def move_down(self):
        """
        Function to move down the elevator.
        """
        if self.state == "Idle":
            self.state = "Moving Down"
            return "Elevator moving down"

        return "Invalid operation in current state"

    def stop(self):
        """
        Function to stop the elevator.
        """
        if self.state in ["Moving Up", "Moving Down"]:
            self.state = "Idle"
            return "Elevator stopped"

        return "Invalid operation in current state"


# 27
class BankAccount:  # pylint: disable=too-few-public-methods
    """
    Bank account class.
    """

    def __init__(self, account_number, balance):
        """
        Set the bank account details.
        """
        self.account_number = account_number
        self.balance = balance

    def view_account(self):
        """
        Function to display the account details.
        """
        return(f"The account {self.account_number} has a balance of {self.balance}")


class BankingSystem:
    """
    Banking system class.
    """

    def __init__(self):
        """
        Mock users.
        """
        self.users = {"user123": "pass123"}  # Simplified user database
        self.logged_in_users = set()

    def authenticate(self, username, password):
        """
        User authentication function.
        """
        if username in self.users and self.users[username] == password:
            if username not in self.logged_in_users:
                self.logged_in_users.add(username)
                print(f"User {username} authenticated successfully.")
                return True

            print("User already logged in.")
        else:
            print("Authentication failed.")

        return False

    def transfer_money(self, sender, receiver, amount, transaction_type):
        """
        Function to perform a money transfer.
        """
        if sender not in self.logged_in_users:
            print("Sender not authenticated.")
            return False

        # Simulate transaction processing logic
        if transaction_type == "regular":
            fee = 0.02 * amount
        elif transaction_type == "express":
            fee = 0.05 * amount
        elif transaction_type == "scheduled":
            fee = 0.01 * amount
        else:
            print("Invalid transaction type.")
            return False

        # Simulate checking for sufficient funds
        if BankAccount(sender, 1000).balance < (amount + fee):
            print("Insufficient funds.")
            return False

        print(
            f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {sender} to {receiver} processed successfully."
        )
        return True


# 28
class Product:  # pylint: disable=too-few-public-methods
    """
    Product class.
    """

    def __init__(self, name, price):
        """
        Set the product details.
        """
        self.name = name
        self.price = price

    def view_product(self):
        """
        Function to display the product details.
        """
        return(f"The product {self.name} has a price of {self.price}")


class ShoppingCart:
    """
    Shopping cart class.
    """

    def __init__(self):
        """
        Initialize the shopping cart.
        """
        self.items = []

    def add_product(self, product, quantity=1):
        """
        Function to add a product to the shopping cart.
        """
        for item in self.items:
            if item["product"] == product:
                item["quantity"] += quantity
                break
        else:
            self.items.append({"product": product, "quantity": quantity})

    def remove_product(self, product, quantity=1):
        """
        Function to remove a product from the shopping cart.
        """
        for item in self.items:
            if item["product"] == product:
                if item["quantity"] <= quantity:
                    self.items.remove(item)
                else:
                    item["quantity"] -= quantity
                break

    def view_cart(self):
        """
        Function to display the shopping cart content.
        """
        for item in self.items:
            return(
                f"{item['quantity']} x {item['product'].name}"
                f" - ${item['product'].price * item['quantity']}"
            )

    def checkout(self):
        """
        Function to checkout the items from the shopping cart.
        """
        total = sum(item["product"].price * item["quantity"] for item in self.items)
        return(f"Total: ${total}")
        print("Checkout completed. Thank you for shopping!")
