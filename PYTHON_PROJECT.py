#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  30 21:54:11 2024

@author: sudhanshu
"""

class HospitalHelper:
    def __init__(self):
        self.patient_records = {}

    def record_patient_info(self):
        print("\nRecord Patient Information:")
        patient_id = input("Enter patient ID: ")
        while True:
          name = input("Please enter your name: ")
          if name.isalpha():
             break
          else:
             print("Invalid input. Please enter alphabetic characters only.")

        print("Your name is:", name)

        while True:
          age = input("Please enter your age: ")
          if age.isdigit() and int(age) < 100:
            break
          else:
            print("Invalid input. Please enter a numeric value less than 100.")

        print("Your age is:", age)

        while True:
          gender = input("Please enter your gender (male/female/other): ").lower()
          if gender in ['male', 'female', 'other']:
            break
          else:
              print("Invalid input. Please enter 'male', 'female', or 'other'.")

          print("Please enter your gender (male/female/other): ")

        medical_history = input("Enter patient's medical history: ")
        self.patient_records[patient_id] = {
            'Name': name,
            'Age': age,
            'Gender': gender,
            'Medical History': medical_history
        }
        print("Patient information recorded successfully!")

    def view_patient_info(self):
        print("\nView Patient Information:")
        if not self.patient_records:
            print("No patient records found.")
            return
        patient_id = input("Enter patient ID to view information: ")
        if patient_id not in self.patient_records:
            print("Patient ID not found.")
            return
        patient_info = self.patient_records[patient_id]
        print("Patient Information:")
        for key, value in patient_info.items():
            print(f"{key}: {value}")

    def record_diagnosis(self):
        print("\nRecord Diagnosis:")
        patient_id = input("Enter patient ID: ")
        if patient_id not in self.patient_records:
            print("Patient ID not found.")
            return
        diagnosis = input("Enter diagnosis: ")
        self.patient_records[patient_id]['Diagnosis'] = diagnosis
        print("Diagnosis recorded successfully!")

    def prescribe_medication(self):
        print("\nPrescribe Medication:")
        patient_id = input("Enter patient ID: ")
        if patient_id not in self.patient_records:
            print("Patient ID not found.")
            return
        medication = input("Enter prescribed medication: ")
        self.patient_records[patient_id]['Prescribed Medication'] = medication
        print("Medication prescribed successfully!")

    def schedule_tests(self):
        print("\nSchedule Tests:")
        patient_id = input("Enter patient ID: ")
        if patient_id not in self.patient_records:
            print("Patient ID not found.")
            return
        tests = input("Enter tests to be scheduled: ")
        self.patient_records[patient_id]['Scheduled Tests'] = tests
        print("Tests scheduled successfully!")

    def discharge_patient(self):
        print("\nDischarge Patient:")
        patient_id = input("Enter patient ID: ")
        if patient_id not in self.patient_records:
            print("Patient ID not found.")
            return
        del self.patient_records[patient_id]
        print("Patient discharged successfully!")

    def view_all_patients(self):
        print("\nView All Patients:")
        if not self.patient_records:
            print("No patients in records.")
            return
        print("Patient IDs:")
        for patient_id in self.patient_records.keys():
            print(patient_id)

    def display_menu(self):
        print("\nHospital Helper Menu:")
        print("1. Record Patient Information")
        print("2. View Patient Information")
        print("3. Record Diagnosis")
        print("4. Prescribe Medication")
        print("5. Schedule Tests")
        print("6. Discharge Patient")
        print("7. View All Patients")
        print("8. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.record_patient_info()
            elif choice == '2':
                self.view_patient_info()
            elif choice == '3':
                self.record_diagnosis()
            elif choice == '4':
                self.prescribe_medication()
            elif choice == '5':
                self.schedule_tests()
            elif choice == '6':
                self.discharge_patient()
            elif choice == '7':
                self.view_all_patients()
            elif choice == '8':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


# Instantiate the HospitalHelper class and run the program
hospital_helper = HospitalHelper()
hospital_helper.run()

