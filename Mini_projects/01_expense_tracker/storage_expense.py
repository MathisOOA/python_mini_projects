import json

class StorageExpense :
 

    def load_expenses(self):
        with open("Mini_projects/01_expense_tracker/data/expenses.json", "r" ) as f :
            return json.load(f)
        
    def save_expenses(self,expenses) :
        data = []
        for expense in expenses :
            data.append(expense.to_dict())

        with open("Mini_projects/01_expense_tracker/data/expenses.json", "w") as f :
            json.dump(data, f, indent=4)

