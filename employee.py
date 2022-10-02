

class Employee:
    def __init__(self, name, monthly_salary, hourly_salary, hours, contract_commission, contracts, bonus_commission):
        self.name = name
        self.monthly_salary = monthly_salary
        self.hourly_salary = hourly_salary
        self.hours = hours
        self.contract_commission = contract_commission
        self.contracts = contracts
        self.bonus_commission = bonus_commission

    def get_pay(self):
        return self.monthly_salary+(self.hourly_salary*self.hours)+(self.contract_commission*self.contracts)+self.bonus_commission

    def __str__(self):
        if self.monthly_salary==0 and self.contract_commission==0 and self.bonus_commission==0:
            return self.name+" works on a contract of "+str(self.hours)+" hours at "+str(self.hourly_salary)+"/hour. Their total pay is "+str(self.get_pay())+"."
        if self.monthly_salary!=0 and self.contract_commission==0 and self.bonus_commission==0:
            return self.name+" works on a monthly salary of "+str(self.monthly_salary)+". Their total pay is "+str(self.get_pay())+"."
        if self.monthly_salary==0 and self.contract_commission!=0 and self.bonus_commission==0:
            return self.name+" works on a contract of "+str(self.hours)+" hours at "+str(self.hourly_salary)+"/hour and receives a commission for "+str(self.contracts)+"contract(s) at"+str(self.contract_commission)+"/contract. Their total pay is "+str(self.get_pay())+"."
        if self.monthly_salary!=0 and self.contract_commission!=0 and self.bonus_commission==0:
            return self.name+" works on a monthly salary of "+str(self.monthly_salary)+" and receives a commission for "+str(self.contracts)+" contract(s) at"+str(self.contract_commission)+"/contract. Their total pay is "+str(self.get_pay())+"."
        if self.monthly_salary==0 and self.contract_commission==0 and self.bonus_commission!=0:
            return self.name+" works on a contract of "+str(self.hours)+" hours at "+str(self.hourly_salary)+"/hour and receives a bonus commission of "+str(self.bonus_commission)+". Their total pay is "+str(self.get_pay())+"."
        if self.monthly_salary!=0 and self.contract_commission==0 and self.bonus_commission!=0:
            return self.name+" works on a monthly salary of "+str(self.monthly_salary)+" and receives a bonus commission of "+str(self.bonus_commission)+". Their total pay is "+str(self.get_pay())+"."
        


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, 0, 0, 0, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 0, 25, 100, 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 0, 200, 4, 0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 0, 25, 150, 220, 3, 0)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 0, 0, 0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 0, 30, 120, 0, 0, 600)

