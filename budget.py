class Category:
# constructor
    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.balance = float()
  
# deposit
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": float(amount), "description": description})
        self.balance += amount

#  funds
    def check_funds(self, amount = -1):
        if (amount > self.balance):
            return False
        else:
            return True

# withdraw
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({"amount": float(0 - amount), "description": description})
        return self.check_funds(amount)

# balance
    def get_balance(self):
        return self.balance

# transfer
    def transfer(self, amount, categ):
        if self.withdraw(amount, "Transfer to "+categ.name):
            categ.deposit(amount, "Transfer from "+self.name)
        return self.check_funds(amount)

# printing classes
    def __str__(self):
        print_value = str()
        star = (30 - len(self.name)) // 2
        for i in range(star):
            print_value += "*"
        
        print_value += self.name
        if (len(self.name) % 2) == 1 : star += 1
        
        for i in range(star):
            print_value += "*"
        print_value+= "\n"

        for i in self.ledger:
            des= i["description"][:23]
            print_value += des
            am = "{:.2f}".format(i["amount"])

            for j in range((23 - len(des)) + (7 - len(am))):
                print_value += " "
            print_value+= am + "\n"
        
        print_value += "Total: "+"{:.2f}".format(self.balance)
        return print_value

def create_spend_chart(categories):
    # if len(categories) > 4: return "Too many categories" 

    char = "Percentage spent by category\n"
    total = 0
    l = list()
    longest = 0
    sum_of_all = list()

    for cat in categories:
        if len(cat.name) > longest : longest = len(cat.name)
        sum = 0
        for spent in cat.ledger:
            if int(spent["amount"]) < 0 : 
                total -= spent["amount"]
                sum -= spent["amount"]
        sum_of_all.append(sum)
    for piece in sum_of_all:
        l.append((((piece * 100) // total) // 10) * 10)

    for i in [100,90,80,70,60,50,40,30,20,10,0]:     
        if i == 0:
            char += "  "
        elif i != 100:  
            char += " "
        char += str(i) + "|"

        for j in range(len(l)):
            if (l[j] >= i) and (j == len(l)-1):
                char +=" o  "
            elif (l[j] >= i) and (j != len(l)-1):
                char += " o "
            elif (l[j] < i) and (j == len(l)-1):
                char += "    "
            else:
                char += "   "  
        
        char +="\n"
    char += "    " + ("---" * (len(categories)-1)) + "----" + "\n" 

    for i in range(longest):
        char+= "    "
        for cat in categories:
            if i >= len(cat.name):
                between = " "
            else:
                between = cat.name[i]
            char += " "+ between + " "
        if i != longest - 1:
            char += "\n"
  
    return char


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())

clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(auto)
mata = Category("Mama")
tata = Category("Tata")
sora = Category("Cineva")
print(create_spend_chart([food, clothing, auto, mata, tata, sora]))