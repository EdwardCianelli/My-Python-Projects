# Budget App

Implements a simple budget manager with categories and methods for depositing, withdrawing, transferring, and visualizing spending.

## Features
- Track ledger of transactions per category
- Transfer between categories
- Generate ASCII spending chart

## Usage
```python
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
create_spend_chart([food])
```

## Skills Demonstrated
- OOP with custom classes
- Lists and dictionaries
- ASCII bar chart visualization
