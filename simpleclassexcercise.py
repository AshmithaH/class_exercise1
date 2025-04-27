class vehicle():
    def __init__(self,vehicleId,type,cost):
        self.vehicleId=vehicleId
        self.type=type
        self.cost=cost
 	
    def calculate(self):
        if self.type=="Two-wheeler" :
            Premium_amount=0.02*self.cost
            total_amount=self.cost-Premium_amount
        elif self.type=="Four-wheeler" :
            Premium_amount=0.06*cost
        else:
            print("invalid vehicle")
            return
        return print(f"vehicle details : {self.vehicleId},{self.type},{self.cost}\nPremium_amount:{Premium_amount} ")
 	
v1=vehicle("1022","Two-wheeler",50000)
v1.calculate()