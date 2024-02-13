class Mpesa:
    def __init__(self,acc_balance,phone_no):
        self.acc_balance = acc_balance
        self.phone_no = phone_no
    def send_money(self,amount,recepient_no):
        if amount > self.acc_balance:
            print("Sorry your transaction cannot be completed.")
            exit()
        else:
            self.acc_balance -= amount
            print(f"{amount}KES has been sent to {recepient_no} successfully. Your account balance is {self.acc_balance}")


class Personal_Mpesa(Mpesa):
    def __init__(self,acc_balance,phone_no,id_no):
        super().__init__(acc_balance,phone_no)
        self.id_no = id_no

    def buy_airtime(self,amount,recepient_no):
        if amount > self.acc_balance:
            print("Sorry your transaction cannot be completed.")
        else:
            self.acc_balance -= amount
            print(f"{amount}KES worth of airtime has been purchased for {recepient_no} successfully.Your account balance is {self.acc_balance}")

class Business_Mpesa(Mpesa):
    def __init__(self,acc_balance,phone_no,id_no,business_no):
        super().__init__(acc_balance, phone_no)
        self.business_no = business_no
    def receive_money(self,amount):
        self.acc_balance += amount
        print(f"{amount}KES received from {self.business_no}. New account balance is {self.acc_balance}")

personal = Personal_Mpesa(500,722222222,2222222)
personal.send_money(100,712345678)
personal.buy_airtime(25,722222222)

business = Business_Mpesa(500,710231343,232324342,722313134)
business.receive_money(500)