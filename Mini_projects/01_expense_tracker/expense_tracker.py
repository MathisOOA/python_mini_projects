from datetime import datetime

class ExpenseTracker:
    expense_list = []

    def display_menu(self) : 

        input_user = 0 

        while(input_user != 5) :
            print("""====== Expense Tracker ======
            1. Add Expense
            2. Delete Expense
            3. View Expenses
            4. Show Total Spent
            5. Exit       
            """)

            input_user = int(input('Choose an option: '))

            if(input_user == 1) :
                self.add_expense()

                #Test (À ENLEVER)
                print('ici : ',len(self.expense_list))

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
        amount = float(input('Amount : ')) #gérer les cas où l'utilisateur n'entre pas une valeur convenable

        object_information = {
            'expense_date' : date,
            'expense_name' : expense_name,
            'expense_amount' : amount
        }

        self.expense_list.append(object_information)
    
    def view_expense(self) :
        pass

    def show_total_spent(self) :
        total_expense = 0

        for expense in self.expense_list :
            total_expense += expense['expense_amount']
        
        print('ici',total_expense)


    def delete_expense(self) :
        pass

    def run_app(self) :
        self.display_menu()