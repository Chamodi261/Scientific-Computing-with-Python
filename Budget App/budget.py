class Category:
  def __init__(self, name):
      self.name = name
      self.ledger = []

  def deposit(self, amount, description=None):
      if description is None:
          self.ledger.append({'amount': amount, 'description': ''})
      else:
          self.ledger.append({'amount': amount, 'description': description})

  def withdraw(self, amount, description=None):
      if self.check_fund(amount):
          if description is None:
              self.ledger.append({'amount': -amount, 'description': ''})
          else:
              self.ledger.append({'amount': -amount, 'description': description})
          return True
      return False

  def get_balance(self):
      balance = 0
      for item in self.ledger:
          balance += item['amount']
      return balance

  def transfer(self, amount, budget_category):
      if self.check_fund(amount):
          self.ledger.append({'amount': -amount, 'description': f'Transfer to {budget_category.name}'})
          budget_category.deposit(amount, f'Transfer from {self.name}')
          return True
      else:
          return False

  def check_fund(self, amount):
      return amount <= self.get_balance()

  def __str__(self):
      name = self.name
      output = name.center(30, '*')
      for item in self.ledger:
          left = item['description'][:23] if item['description'] else ''
          right = "{:.2f}".format(item['amount'])
          output += f"\n{left:<23}{right:>7}"
      output += "\nTotal: " + str(self.get_balance())
      return output


def create_spend_chart(categories):
  spent_dict = {}
  for category in categories:
      spent_amount = sum(item['amount'] for item in category.ledger if item['amount'] < 0)
      spent_dict[category.name] = round(spent_amount, 2)

  total = sum(spent_dict.values())

  percent_dict = {}
  for key, value in spent_dict.items():
      percent_dict[key] = int(round(value / total, 2) * 100)

  output = 'Percentage spent by category\n'
  for i in range(100, -10, -10):
      output += f'{i}'.rjust(3) + '| '
      for percent in percent_dict.values():
          output += 'o  ' if percent >= i else '   '
      output += '\n'
  output += ' '*4 + '-' * (len(percent_dict) * 3 + 1) + '\n     '

  max_len_category = max(len(category) for category in percent_dict)

  for i in range(max_len_category):
      for name in percent_dict.keys():
          output += name[i] + '  ' if len(name) > i else '   '
      if i < max_len_category - 1:
          output += '\n     '

  return output


# Example usage:
food_category = Category("Food")
clothing_category = Category("Clothing")

food_category.deposit(1000, "Initial deposit")
food_category.withdraw(200, "Groceries")
clothing_category.deposit(500, "Initial deposit")
clothing_category.withdraw(100, "Clothes")

categories = [food_category, clothing_category]

print(create_spend_chart(categories))
