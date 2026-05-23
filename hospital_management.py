# Hospital Management System in Python

patients = []

def menu():
    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Remove Patient")
    print("5. Exit")

while True:
    menu()

    choice = input("Enter your choice: ")

    # Add Patient
    if choice == "1":
        name = input("Enter patient name: ")
        age = input("Enter patient age: ")
        disease = input("Enter disease: ")

        patient = {
            "Name": name,
            "Age": age,
            "Disease": disease
        }

        patients.append(patient)
        print("Patient added successfully!")

    # View Patients
    elif choice == "2":
        if len(patients) == 0:
            print("No patient records found.")
        else:
            print("\nPatient Records:")
            for i, patient in enumerate(patients, start=1):
                print(f"\nPatient {i}")
                print("Name    :", patient["Name"])
                print("Age     :", patient["Age"])
                print("Disease :", patient["Disease"])

    # Search Patient
    elif choice == "3":
        search_name = input("Enter patient name to search: ")

        found = False

        for patient in patients:
            if patient["Name"].lower() == search_name.lower():
                print("\nPatient Found")
                print("Name    :", patient["Name"])
                print("Age     :", patient["Age"])
                print("Disease :", patient["Disease"])
                found = True
                break

        if not found:
            print("Patient not found.")

    # Remove Patient
    elif choice == "4":
        remove_name = input("Enter patient name to remove: ")

        found = False

        for patient in patients:
            if patient["Name"].lower() == remove_name.lower():
                patients.remove(patient)
                print("Patient removed successfully!")
                found = True
                break

        if not found:
            print("Patient not found.")

    # Exit
    elif choice == "5":
        print("Exiting Hospital Management System...")
        break

    else:
        print("Invalid choice. Please try again.")
