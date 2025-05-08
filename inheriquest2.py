class Person:
    def __init__(self, name, age, contact_number):
        self.__name = name
        self.__age = age
        self._contact_number = contact_number

    def get_contact_number(self):
        return self._contact_number

    def set_contact_number(self, contact_number):
        self._contact_number = contact_number

    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}, Contact: {self._contact_number}")


class Patient(Person):
    def __init__(self, name, age, contact_number, patient_id):
        super().__init__(name, age, contact_number)
        self.__patient_id = patient_id
        self.__ailments = []

    def add_ailment(self, ailment):
        self.__ailments.append(ailment)
        print(f"Ailment '{ailment}' added for Patient ID: {self.__patient_id}")

    def view_ailments(self):
        print(f"Ailments for Patient ID {self.__patient_id}: {', '.join(self.__ailments) if self.__ailments else 'None'}")

    def display_details(self):
        self.display_info()
        print(f"Patient ID: {self.__patient_id}")
        self.view_ailments()


class Doctor(Person):
    def __init__(self, name, age, contact_number, doctor_id):
        super().__init__(name, age, contact_number)
        self.__doctor_id = doctor_id
        self._patients = []

    def assign_patient(self, patient):
        self._patients.append(patient)
        print(f"Patient ID {patient._Patient__patient_id} assigned to Doctor ID: {self.__doctor_id}")

    def remove_patient(self, patient_id):
        for patient in self._patients:
            if patient._Patient__patient_id == patient_id:
                self._patients.remove(patient)
                print(f"Patient ID {patient_id} removed from Doctor ID: {self.__doctor_id}")
                return
        print(f"Patient ID {patient_id} not found under Doctor ID: {self.__doctor_id}")

    def display_assigned_patients(self):
        patient_ids = [patient._Patient__patient_id for patient in self._patients]
        print(f"Doctor ID {self.__doctor_id} Assigned Patients: {', '.join(patient_ids) if patient_ids else 'None'}")


class Hospital:
    def __init__(self):
        self._admitted_patients = []

    def admit_patient(self, patient):
        self._admitted_patients.append(patient)
        print(f"Patient ID {patient._Patient__patient_id} admitted to the hospital.")

    def discharge_patient(self, patient_id):
        for patient in self._admitted_patients:
            if patient._Patient__patient_id == patient_id:
                self._admitted_patients.remove(patient)
                print(f"Patient ID {patient_id} discharged from the hospital.")
                return
        print(f"Patient ID {patient_id} not found in the hospital.")

    def show_admitted_patients(self):
        patient_ids = [patient._Patient__patient_id for patient in self._admitted_patients]
        print(f"Admitted Patients: {', '.join(patient_ids) if patient_ids else 'None'}")


# Create a hospital instance
hospital = Hospital()

# Create a doctor instance
doctor = Doctor("Dr. Krishna", 45, "1122334455", "D001")

# Dictionary to hold patients
patients = {}

# Menu-driven interface
while True:
    print("\nMenu:")
    print("1. Admit a patient")
    print("2. Discharge a patient")
    print("3. View admitted patients")
    print("4. Add ailment to a patient")
    print("5. View patient ailments")
    print("6. Assign a patient to a doctor")
    print("7. View doctor's assigned patients")
    print("8. Add a new patient")
    print("0. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            contact = input("Enter patient contact number: ")
            patient_id = input("Enter patient ID: ")
            if patient_id not in patients:
                patient = Patient(name, age, contact, patient_id)
                patients[patient_id] = patient
                hospital.admit_patient(patient)
            else:
                print("Patient ID already exists.")

        elif choice == 2:
            patient_id = input("Enter patient ID to discharge: ")
            hospital.discharge_patient(patient_id)

        elif choice == 3:
            hospital.show_admitted_patients()

        elif choice == 4:
            patient_id = input("Enter patient ID: ")
            if patient_id in patients:
                ailment = input("Enter ailment: ")
                patients[patient_id].add_ailment(ailment)
            else:
                print("Patient not found.")

        elif choice == 5:
            patient_id = input("Enter patient ID: ")
            if patient_id in patients:
                patients[patient_id].view_ailments()
            else:
                print("Patient not found.")

        elif choice == 6:
            patient_id = input("Enter patient ID: ")
            if patient_id in patients:
                doctor.assign_patient(patients[patient_id])
            else:
                print("Patient not found.")

        elif choice == 7:
            doctor.display_assigned_patients()

        elif choice == 8:
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            contact = input("Enter patient contact number: ")
            patient_id = input("Enter patient ID: ")
            if patient_id not in patients:
                patients[patient_id] = Patient(name, age, contact, patient_id)
                print(f"Patient '{name}' added successfully.")
            else:
                print("Patient ID already exists.")

        elif choice == 0:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")