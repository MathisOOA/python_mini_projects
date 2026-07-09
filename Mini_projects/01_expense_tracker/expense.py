class Expense :

    current_id = 1 #Variable local permettant de calculer le nbr d'instance d'expense crée

    def __init__(self,id,date,name,amount): #Constructeur

        if id is None :
            self.id = Expense.current_id
            Expense.current_id += 1
        else : 
            self.id = id
            if(id >= Expense.current_id) :
                Expense.current_id = id + 1

        self.date = date
        self.name = name
        self.amount = amount 

    def to_dict(self) :
        return {
            "id": self.id,
            "name": self.name,
            "date": self.date,
            "amount": self.amount
        }
    
    def to_expense(dict_expense) :
        return Expense(dict_expense['id'],dict_expense['date'],dict_expense['name'],dict_expense['amount'])

    def __str__(self): #Équivalent toString() en java
        return f"{self.id:<5} {self.name:<14} {self.date:<24} {self.amount:>5.2f}$"
