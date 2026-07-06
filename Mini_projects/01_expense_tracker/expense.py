class Expense :

    current_id = 1 #Variable local permettant de calculer le nbr d'instance d'expense crée

    def __init__(self,date,name,amount): #Constructeur
        self.id = Expense.current_id
        Expense.current_id += 1

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


    def __str__(self): #Équivalent toString() en java
        return f"{self.id:<5} {self.name:<15} {self.date:<25} {self.amount:>5.2f}$"
