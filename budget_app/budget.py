class Category:
  def __init__(self, category):
    self.ledger = []
    self.category = category
    self.deposits = 0
    self.withdrawals = 0
    self.balance = 0
    
  def deposit(self, dep, description=''):
    self.ledger.append({"amount": dep, "description": description})
    self.deposits += dep
    self.balance += float(dep)
    
  def withdraw(self, drawing, description=''):
    fund = self.check_funds(drawing)

    if fund:
      self.ledger.append({"amount": float(-drawing), "description": description})
      self.withdrawals += drawing
      self.balance -= drawing
      return True
    return False

  def get_balance(self):
    return self.balance

  def transfer(self, amount, destination):
    fund = self.check_funds(float(amount))

    if fund:
      self.ledger.append({"amount": float(-amount), "description": f'Transfer to {destination.category}'})
      destination.ledger.append({"amount": amount, "description": f'Transfer from {self.category}'})
      self.balance -= amount
      destination.balance += amount
      return True
    return False

  def check_funds(self, amount):
    if self.balance < amount:
      return False
    return True

  def __str__(self):
    MAX_LENGTH = 30
    star_len = int((MAX_LENGTH - len(self.category)) / 2)
    header = f"{'*'*star_len}{self.category}{'*'*star_len}"
    result = header + '\n'

    temp = [' ' for x in range(30)]
    for entry in self.ledger:
      x = entry['amount']
      a = [l for l in f'{x:.2f}' ]
      a.reverse()
      d = [l for l in entry['description']]
      
      for i in range(1,len(a)+1):
        temp[-i] = a[i-1]
      for i in range(min(len(d),23)):
        temp[i] = d[i]

      line_item = ''.join(temp)
      result += line_item + '\n'
      temp = [' ' for x in range(30)]

    result += f'Total: {self.balance:.2f}'

    return result

def create_spend_chart(categories):
  total = 0
  for category in categories:
    total += category.withdrawals
    print(total)

  spend_percentage = {}
  for category in categories:
    spend_percentage[category.category] = int((((category.withdrawals / total) * 10) // 1) * 10)

  print(spend_percentage)
  # generate chart
  header = 'Percentage spent by category\n'
  
  chart = ''
  for n in range(100,-1,-10):
    chart += str(n).rjust(3) + '|'
    for c,v in spend_percentage.items():
      if v >= n:
        chart += ' o '
      else:
        chart += '   '
    chart += ' \n'
    
  footer = "    " + "-"*(3 * len(categories) + 1) + '\n'
  descriptions = list(map(lambda category: category.category, categories))
  max_length = max(map(lambda description: len(description), descriptions))
  descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
  for x in zip(*descriptions):
    footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"
  
#   for c in categories:
#     print(c.withdrawals)

  return (header + chart + footer).rstrip("\n")

