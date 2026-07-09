from datetime import datetime
from expense import Expense
from storage_expense import StorageExpense

class ExpenseTracker:

    def __init__(self):
        self.storage = StorageExpense()
        self.expense_list = self.storage.load_expenses()

    def display_menu(self) : 

        input_user = 0 

        while(input_user != 5) :
            print("""\n====== Expense Tracker ======
        1. Add Expense
        2. Delete Expense
        3. View Expenses
        4. Show Total Spent
        5. Exit       
            """)

            try : 
                input_user = int(input('Choose an option: '))
            except ValueError:
                print('Please choose an option between 1-5!')

            if(input_user == 1) :
                self.add_expense()

            elif(input_user == 2) :
                self.delete_expense()

            elif(input_user == 3 ) :
                self.view_expense()

            elif(input_user == 4) :
                self.show_total_spent()

            elif(input_user == 5) :
                print('Goodbye!')


    def add_expense(self) :
        date = datetime.now()
        date = date.strftime("%m/%d/%Y, %H:%M:%S")
        
        print('Please enter the following details :')
        expense_name = input('Expense name : ')
        amount = float(input('Amount : '))

        expense = Expense(Expense.current_id, date, expense_name, amount)
        self.expense_list.append(expense)

        self.storage.save_expenses(self.expense_list)


    def sort_expenses_by(self,variable) :
        try :
            self.expense_list.sort(key = lambda expense: getattr(expense,variable))
            return True
        except AttributeError as e:
            print('The variable entered is not valid ! :',e)
            return False
    

    def view_expense(self) :

        while True :
            print("""
ID      Name         Date("m/d/Y, H:M:S")     Amount
------------------------------------------------------""") 
            for extense in self.expense_list :
                print(extense)

            print("""
Do you wish to sort your expenses by? :
[id] [name] [date] [amount]

Type 'exit' to return.""")

            sort_option = input('\nChoose an option: ').lower()

            if(sort_option == 'exit') :
                break

            self.sort_expenses_by(sort_option)


    def show_total_spent(self) :
        total_expense = 0

        for expense in self.expense_list :
            total_expense += expense.amount
        
        print('You spent in total {:.2f} $'.format(total_expense))


    def delete_expense(self) :
        try :
            expense_id = int(input('Enter the ID of the expense you wish to remove : ')) #Gérer les cas où l'utilisateur n'entre pas une valeur convenable
        except ValueError :
            print("Invalid input. Please enter a number.")
            return
        
        expense = self.get_expense(expense_id)

        if(expense) : 
            self.expense_list.remove(expense)
            self.storage.save_expenses(self.expense_list)
            print('The expense was successfully removed!')

        else :
            print('The ID you entered isn\'t valid!')
        

    def get_expense(self, expense_id) :
        for expense in self.expense_list :
            if(expense.id == expense_id) :
                return expense
        return None
    
    def run_app(self) :
        self.display_menu()