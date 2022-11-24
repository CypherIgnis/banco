class User():
    
    current_id = 0

    def __init__(self, name, rut, mail, password):
        self.id = type(self).current_id
        type(self).current_id += 1
        self.name = name
        self.rut = rut
        self.mail = mail
        self.password = password
        self.balance = 0

    def deposit(self, ammount):
        if ammount > 0:
            self.balance += int(ammount)
            return
        print("Debe ser un numero positivo!")

    def withdraw(self, ammount):
        if ammount > 0:
            if ammount <= self.balance:
                self.balance -= int(ammount)
                return
            print("No puede retirar mas de lo que posee!")
            return
        print("Debe ser un numero positivo!")

    def print(self):
        print(f"\nNombre: {self.name}")
        print(f"RUT: {self.rut}")
        print(f"Correo: {self.mail}")
        print(f"Balance: {self.balance}")

