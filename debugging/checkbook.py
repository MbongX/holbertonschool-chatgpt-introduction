#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount < 0:
            print("Deposit amount cannot be negative.")
            return

        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount < 0:
            print("Withdrawal amount cannot be negative.")
            return

        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))


def get_valid_amount(prompt):
    """
    Function Description:
        Prompts the user for a numeric amount and validates the input.

    Parameters:
        prompt (str): The message displayed to the user.

    Returns:
        float: A valid numeric amount entered by the user.
    """

    while True:
        try:
            amount = float(input(prompt))
            return amount

        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    cb = Checkbook()

    while True:
        action = input(
            "What would you like to do? "
            "(deposit, withdraw, balance, exit): "
        )

        if action.lower() == 'exit':
            print("Exiting program.")
            break

        elif action.lower() == 'deposit':
            amount = get_valid_amount(
                "Enter the amount to deposit: $"
            )
            cb.deposit(amount)

        elif action.lower() == 'withdraw':
            amount = get_valid_amount(
                "Enter the amount to withdraw: $"
            )
            cb.withdraw(amount)

        elif action.lower() == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()