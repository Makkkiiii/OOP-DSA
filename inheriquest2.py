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
        
        

hospital = Hospital()


patient1 = Patient("Hari Shyam", 30, "1234567890", "P001")
patient2 = Patient("Ram Hari", 25, "0987654321", "P002")


hospital.admit_patient(patient1)
hospital.admit_patient(patient2)


patient1.add_ailment("Fever")
patient1.add_ailment("Cough")
patient2.add_ailment("Headache")


hospital.show_admitted_patients()


doctor = Doctor("Dr. Krishna", 45, "1122334455", "D001")


doctor.assign_patient(patient1)
doctor.assign_patient(patient2)


doctor.display_assigned_patients()
patient1.view_ailments()
patient2.view_ailments()


hospital.discharge_patient("P001")


hospital.show_admitted_patients()


doctor.display_info()
patient1.display_details()
patient2.display_details()