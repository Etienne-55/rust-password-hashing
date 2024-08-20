class Closet():
    def __init__(self, shirt, pant, shoes):
        
        self.shirt = int(shirt)
        self.pant = int(pant)
        self.shoes = int(shoes)

    def __str__(self):
        return f"shirt: {self.shirt}, pant: {self.pant}, shoes: {self.shoes}"
    
    def add_clothes():

        shirt = input("How many shirts do you want to add?: ")
        pant = input("How many pants do you want to add?: ")
        shoes = input("How many shoes do you want to add?: ")
        return Closet(shirt, pant, shoes)

    def calcule_comb(self):
    
        if self.shirt == 0 or self.pant == 0 or self.shoes == 0:
            return 0
        return self.shirt * self.pant * self.shoes

def main():
    is_running = True 

    while is_running:

        print("Outfit combinations.")
        print("1-Add clothes: ")
        print("2-See combinations: ")
        print("3-Remove clothes: ")
        print("4-Exit: ")

        choice = input("Choose the operation: ")

        if choice == '1':
            closet = Closet.add_clothes()
            
        elif choice == '2':
            if closet is not None:
                combinations = closet.calcule_comb()
                if combinations == 0:
                    print("Closet if empty.")
                else: 
                    print(f"The number of combinations is {combinations}")
            else: 
                print(f"No clothes were added.")
        #elif choice == '3':

        elif choice == '4':
            is_running = False

        else:
            print("Opção invalida.")

    print("Operação encerrada.")

if __name__ == '__main__':
    main()