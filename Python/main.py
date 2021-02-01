from car import Car
from UberX import UberX
from UberBlack import UberBlack
from account import Account


if __name__ == "__main__":

    print("super class ")
    car = Car("AMS234", Account("Andres Herrera", "121323"))
    print(vars(car))
    print(vars(car.driver))
    print(" ")


    print("Sub class UberX ")
    uberX = UberX("x",Account("Angie",12345),"chebrolet","MD")
    print(vars(uberX))
    print(vars(uberX.driver))
    print(" ")

    print("Sub class UberBlack ")
    uberBlack = UberBlack("black",Account("Bob",54321),["chebrolet","mazta"],["MD","KS"])
    print(vars(uberBlack))
    print(vars(uberBlack.driver))