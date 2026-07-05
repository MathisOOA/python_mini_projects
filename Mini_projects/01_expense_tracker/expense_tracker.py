from datetime import datetime
from expense import Expense

class ExpenseTracker:
    
    #TEST À RETIRER QUAND J'AURAI FINIS L'IMPLEMENTATION 
    expense1 = Expense('07/05/2026, 15:43:26', 'chocolat', 21.3)
    expense2 = Expense('11/21/2026, 05:03:26', 'Cacao', 8.32)

    expense_list = [expense1,expense2]

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

            input_user = int(input('Choose an option: '))

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

            else : 
                print('\nPlease choose a valid option!\n')


    def add_expense(self) :
        date = datetime.now()
        date = date.strftime("%m/%d/%Y, %H:%M:%S")
        

        print('Please enter the following details :')
        expense_name = input('Expense name : ')
        amount = float(input('Amount : ')) #Gérer les cas où l'utilisateur n'entre pas une valeur convenable

        expense = Expense(date,expense_name,amount)
        self.expense_list.append(expense)

    
    def view_expense(self) :
        print("""
ID      Name         Date("m/d/Y, H:M:S")     Amount
------------------------------------------------------""")
        
        for expense in self.expense_list :
            print(expense)
        
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

        if(expense != None) : 
            self.expense_list.remove(expense)
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