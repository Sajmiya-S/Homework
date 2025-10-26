class Expense:
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return self.name
    
class ExpenseTracker:
    def __init__(self):
        self.allexpense = []
        # self.allexpense = []

    def add_expense(self,name,amount):
        self.allexpense.append(Expense(name,amount))
        # self.allexpense.append(amount)
        print(f'Expense "{name}" added to Expense Tracker')

    def view_expense(self):
        if not self.allexpense:
            print('No expense')
        else:
            n = 1
            for i in self.allexpense:
                print(f'{n}. {i.name} - Rs.{i.amount}')
                n += 1

    def calculate_total_expense(self):
        self.total = 0
        for i in self.allexpense:
            self. total += i.amount
        return f'Total expense : {self.total}'
    

def main():
    et = ExpenseTracker()
    print('\nWelcome to Expense Tracker\n____________________________')
    while True:
        print('\n1.Add expense\n2.View expense\n3.Calculate total expense\n4.Exit')
        c = int(input('Enter your choice: '))
        if c == 1:
            name = input('Enter brief description of expense: ')
            amount = int(input('Enter amount spent : '))
            et.add_expense(name,amount)
        elif c == 2:
            et.view_expense()
        elif c == 3:
            et.view_expense()
            print(et.calculate_total_expense())
        elif c == 4:
            break
        else:
            print('Invalid choice')


main()