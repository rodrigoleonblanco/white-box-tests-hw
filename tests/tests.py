import unittest

from src.white_box import verify_age, validate_credit_card, calculate_quantity_discount, grade_quiz, VendingMachine, TrafficLight, UserAuthentication, DocumentEditingSystem, ElevatorSystem, BankAccount, BankingSystem, Product, ShoppingCart

class TestFunctions(unittest.TestCase):

    def test_verify_age(self):
        self.assertEqual(verify_age(25), "Eligible")
        self.assertEqual(verify_age(17), "Not Eligible")
        self.assertEqual(verify_age(66), "Not Eligible")

    def test_validate_credit_card(self):
        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card")
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")
        self.assertEqual(validate_credit_card("12345678901234a"), "Invalid Card")

    def test_calculate_quantity_discount(self):
        self.assertEqual(calculate_quantity_discount(3), "No Discount")
        self.assertEqual(calculate_quantity_discount(7), "5% Discount")
        self.assertEqual(calculate_quantity_discount(12), "10% Discount")

    def test_grade_quiz(self):
        self.assertEqual(grade_quiz(7, 1), "Pass")
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")
        self.assertEqual(grade_quiz(4, 4), "Fail")


class TestVendingMachine(unittest.TestCase):

    def test_initial_state(self):
        vending_machine = VendingMachine()
        self.assertEqual(vending_machine.state, "Ready")

    def test_insert_coin(self):
        machine = VendingMachine()
        self.assertEqual(machine.insert_coin(), "Coin Inserted. Select your drink.")
        self.assertEqual(machine.insert_coin(), "Invalid operation in current state.")

    def test_select_drink(self):
        machine = VendingMachine()
        machine.insert_coin()
        self.assertEqual(machine.select_drink(), "Drink Dispensed. Thank you!")
        self.assertEqual(machine.select_drink(), "Invalid operation in current state.")


class TestTrafficLight(unittest.TestCase):

    def test_initial_state(self):
        traffic_light = TrafficLight()
        self.assertEqual(traffic_light.state, 'Red')

    def test_change_state(self):
        light = TrafficLight()
        self.assertEqual(light.get_current_state(), "Red")
        light.change_state()
        self.assertEqual(light.get_current_state(), "Green")
        light.change_state()
        self.assertEqual(light.get_current_state(), "Yellow")
        light.change_state()
        self.assertEqual(light.get_current_state(), "Red")

    def test_get_current_state(self):
        traffic_light = TrafficLight()
        self.assertEqual(traffic_light.get_current_state(), 'Red')


class TestUserAuthentication(unittest.TestCase):

    def test_initial_state(self):
        user_auth = UserAuthentication()
        self.assertEqual(user_auth.state, 'Logged Out')

    def test_login(self):
        auth = UserAuthentication()
        self.assertEqual(auth.login(), "Login successful")
        self.assertEqual(auth.login(), "Invalid operation in current state")

    def test_logout(self):
        auth = UserAuthentication()
        auth.login()
        self.assertEqual(auth.logout(), "Logout successful")
        self.assertEqual(auth.logout(), "Invalid operation in current state")

class TestDocumentEditingSystem(unittest.TestCase):

    def test_initial_state(self):
        editor = DocumentEditingSystem()
        self.assertEqual(editor.state, "Editing")

    def test_save_document(self):
        editor = DocumentEditingSystem()
        self.assertEqual(editor.save_document(), "Document saved successfully")
        self.assertEqual(editor.save_document(), "Document saved successfully")

    def test_edit_document(self):
        editor = DocumentEditingSystem()
        self.assertEqual(editor.edit_document(), "Editing resumed")

class TestElevatorSystem(unittest.TestCase):

    def test_initial_state(self):
        elevator = ElevatorSystem()
        self.assertEqual(elevator.state, "Idle")

    def test_move_up(self):
        elevator = ElevatorSystem()
        self.assertEqual(elevator.move_up(), "Elevator moving up")
        self.assertEqual(elevator.state, "Moving Up")
        self.assertEqual(elevator.move_up(), "Invalid operation in current state")

    def test_move_down(self):
        elevator = ElevatorSystem()
        self.assertEqual(elevator.move_down(), "Elevator moving down")
        self.assertEqual(elevator.state, "Moving Down")
        self.assertEqual(elevator.move_down(), "Invalid operation in current state")

    def test_stop(self):
        elevator = ElevatorSystem()
        elevator.move_up() 
        self.assertEqual(elevator.stop(), "Elevator stopped")
        self.assertEqual(elevator.state, "Idle")
        self.assertEqual(elevator.stop(), "Invalid operation in current state")

class TestBankAccountInit(unittest.TestCase):

    def test_initial_state(self):
        account = BankAccount("1234567890", 1000)
        self.assertEqual(account.account_number, "1234567890")
        self.assertEqual(account.balance, 1000)

    def test_view_account(self):
        account = BankAccount("1234567890", 1000)
        result = account.view_account()
        self.assertEqual(result, "The account 1234567890 has a balance of 1000")

class TestBankingSystem(unittest.TestCase):

    def test_initialization(self):
        banking_system = BankingSystem()
        self.assertEqual(banking_system.users, {"user123": "pass123"})
        self.assertEqual(banking_system.logged_in_users, set())


    def test_authenticate(self):
        system = BankingSystem()
        self.assertTrue(system.authenticate("user123", "pass123"))
        self.assertFalse(system.authenticate("user123", "wrongpass"))

    def test_transfer_money(self):
        system = BankingSystem()
        system.authenticate("user123", "pass123")
        self.assertTrue(system.transfer_money("user123", "receiver", 100, "regular"))
        self.assertFalse(system.transfer_money("user123", "receiver", 10000, "regular"))

class TestProduct(unittest.TestCase):

    def test_initialization(self):
        product = Product("Laptop", 999.99)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 999.99)

    def test_view_product(self):
        product = Product("Laptop", 999.99)
        expected_output = "The product Laptop has a price of 999.99"
        self.assertEqual(product.view_product(), expected_output)


class TestShoppingCart(unittest.TestCase):

    def test_initialization(self):
        cart = ShoppingCart()
        self.assertEqual(cart.items, [])


    def test_add_product(self):
        cart = ShoppingCart()
        product = Product("Laptop", 999.99)
        cart.add_product(product, 2)
        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0]["product"], product)
        self.assertEqual(cart.items[0]["quantity"], 2)

    def test_remove_product(self):
        cart = ShoppingCart()
        product = Product("Laptop", 999.99)
        cart.add_product(product, 2)
        cart.remove_product(product, 1)
        self.assertEqual(cart.items[0]["quantity"], 1)
        cart.remove_product(product, 1)
        self.assertEqual(cart.items, [])

    def test_view_cart(self):
        product1 = Product("Laptop", 1000)
        product2 = Product("Mouse", 50)
        cart = ShoppingCart()
        cart.add_product(product1, 1)
        cart.add_product(product2, 2)
        cart_details = cart.view_cart()
        self.assertEqual(
            cart_details,
            "1 x Laptop - $1000\n2 x Mouse - $100"
        )

    def test_checkout(self):
        product1 = Product("Laptop", 1000)
        product2 = Product("Mouse", 50)
        cart = ShoppingCart()
        cart.add_product(product1, 1)
        cart.add_product(product2, 2)
        total = cart.checkout()
        self.assertEqual(total, "Total: $1100")