** start of main.py **

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        total = 0
        for thing in self.ledger:
            total += thing["amount"]
        return total

    def transfer(self, amount, other_cat):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + other_cat.name)
            other_cat.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        body = ""
        for i in self.ledger:
            desc = i["description"][:23]
            amt = "{:.2f}".format(i["amount"])
            body += desc.ljust(23) + amt.rjust(7) + "\n"
        total_line = "Total: " + str(self.get_balance())
        return title + body + total_line


def create_spend_chart(categories):
    spend = []
    for c in categories:
        total = 0
        for thing in c.ledger:
            if thing["amount"] < 0:
                total += -thing["amount"]
        spend.append(total)

    all_spent = sum(spend)
    percents = []
    for s in spend:
        p = (s / all_spent) * 100
        percents.append(int(p // 10) * 10)

    chart = "Percentage spent by category\n"
    for n in range(100, -1, -10):
        row = str(n).rjust(3) + "|"
        for p in percents:
            if p >= n:
                row += " o "
            else:
                row += "   "
        chart += row + " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    longest = 0
    for c in categories:
        if len(c.name) > longest:
            longest = len(c.name)

    for i in range(longest):
        row = "     "
        for c in categories:
            if i < len(c.name):
                row += c.name[i] + "  "
            else:
                row += "   "
        if i < longest - 1:
            chart += row + "\n"
        else:
            chart += row

    return chart


** end of main.py **

