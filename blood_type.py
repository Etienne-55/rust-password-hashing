hash_table = {}

def main():
        is_running = True

        while is_running:
            print("Patient blood type database.")
            print("1. Enter patient data: ")
            print("2. Remove data: ")
            print("3. Show database: ")
            print("4. exit: ")

            choice = input("Choose the operation: ")

            if choice == '1':
                add_data()

            elif choice == '2':
                remove_data()

            elif choice == '3':
                show_data()

            elif choice == '4':
                is_running = False

            else:
                print("Opção invalida.")

        print("Operação encerrada.")

class Patient_stats():
    def __init__(self, patient_name, blood_type):

        self.patient_name = patient_name
        self.blood_type = blood_type

    def __str__(self):
        return f"patient name: {self.patient_name}, blood type: {self.blood_type}"
    
def add_data():

    patient = input("Enter patient name: ")
    blood_type = input("Enter blood type: ")
    
    hash_key = len(hash_table) + 1

    hash_table[hash_key] = {'patient': patient, 'blood_type': blood_type}
    
def show_data():
    
    for key, value in hash_table.items():
        print(f"Key: {key}, patient: {value['patient']}, blood_type: {value['blood_type']}")   
      
def remove_data():
    key_adress = int(input("Enter the patient register number to remove: "))
    for hash_key, value in hash_table.items():
        if key_adress == hash_key:
            del hash_table[int(hash_key)]
            print(f"Patient: {value['patient']} removed from the database.")
            return
    print(f"Patient {value['patient']} not found in the database.")

if __name__ == '__main__':
     main()