
from BankUser import User


def main():
    name = input("Ingrese su nombre\n> ")
    rut = input("Ingrese su RUT\n> ")
    mail = input("Ingrese su correo\n> ")
    password = input("Ingrese su contraseña\n> ")
    if password != input("Confirme su contraseña\n> "):
        print("Las contraseñas no coinciden")
        return False

    user = User(name, rut, mail, password)
    user.print()
    while True:
        if input("Quiere realizar un deposito o un retiro? (Y/N)\n> ").upper() == "N":
            break
        ammount = int(input("Ingrese la cantidad a depositar/retirar\n> "))
        if input("Quiere depositar o retirar? (D/R)\n> ").upper() == "D":
            user.deposit(ammount)
        else:
            user.withdraw(ammount)
        user.print()


if __name__ == "__main__":
    main()
