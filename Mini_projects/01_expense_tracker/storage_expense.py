import json
from expense import Expense

class StorageExpense :
 

    def load_expenses(self):
        expenses = []
        
        with open("Mini_projects/01_expense_tracker/data/expenses.json", "r" ) as f :            
            data = json.load(f)
            
            for expense_dict in data :
                expense = Expense.to_expense(expense_dict)
                expenses.append(expense)
        
        return expenses
    

    def save_expenses(self,expenses) :
        data = []
        for expense in expenses :
            data.append(expense.to_dict())

        with open("Mini_projects/01_expense_tracker/data/expenses.json", "w") as f :
            json.dump(data, f, indent=4)