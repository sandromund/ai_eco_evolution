class Loan:
    
    def __init__(self, debtor, creditor, amout, duration, interest_charges):
        self.debtor = debtor
        self.creditor = creditor
        self.amout = amout
        self.duration = duration  # in months
        self.interest_charges = interest_charges
        self.payed = 0
        self.total_amount = self.amout + (self.amout * self.interest_charges)
        self.payment_per_month = self.total_amount / duration
        
    def __str__(self):
        return "Loan: " +self.debtor.name + " - "+ str(self.amout) + " -> " + self.creditor.name 
    
    def __repr__(self):
        return self.__str__()