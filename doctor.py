class Doctor:
    doctors = []

    def __init__(self, id = 0, name = "", specialization = "", working_time = "", qualification = "", room_number = ""):
        self.id = int(id)
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = int(room_number)

    """
    Formats each doctor’s information (properties) in the same format 
    used in the .txt file (i.e., has underscores between values)
    """
    def format_doctor_info(self, doctor):
        # 1: format this doctor's information in this format: 66_Dr. Mike_Heart_9am-5pm_MS_2
        # 2: return the formatted string: 66_Dr. Mike_Heart_9am-5pm_MS_2
        return str(f"{doctor.id}_{doctor.name}_{doctor.specialization}_{doctor.working_time}_{doctor.qualification}_{doctor.qualification}_{doctor.room_number}")

    # Asks the user to enter doctor properties (listed in the Properties point)
    def enter_doctor_info(self):
        # ask user to enter doctor's data and use variables to receive it.
        self.id = int(input("Enter the doctor's id:\n"))
        self.name = input("Enter the doctor's name:\n")
        self.specilist = input("Enter the doctor's specilist:\n")
        self.timing = input("Enter the doctor's timing:\n")
        self.qualification = input("Enter the doctor's qualification:\n")
        self.room_no = int(input("Enter the doctor's room number:\n"))

    # Reads from “doctors.txt” file and fills the doctor objects in a list
    def read_doctors_file(self):
        self.doctors.clear()
        with open("doctors.txt", "r") as doc_file:
            file_content = doc_file.readlines()
            for line in file_content:
                values = line.split("_")
                doctor = Doctor(values[0], values[1], values[2], values[3], values[4], values[5])
                self.doctors.append(doctor)
        print("Finished loading doctors.txt to doctors list")

    # Searches whether the doctor is in the list of doctors using the doctor ID that the user enters
    def search_doctor_by_id(self):
        found = False
        id = int(input("\nEnter the doctor ID:\n"))
    
        # loop the doctor list to check if there is a a matched one
        for doctor in self.doctors:
            if id == int(doctor.id):
                found = True
                print ("{:<4} {:<22} {:<15} {:<15} {:<15} {:<10}".format(doctor.id, doctor.name, doctor.specilist , doctor.timing, doctor.qualification, doctor.room_no))
                    
        if found == False:
            print("Can't find the doctor with the same id on the system")

    
    # Searches whether the doctor is in the list of doctors using the doctor name that the user enters
    def search_doctor_by_name(self):
        found = False
        name = str(input("\nEnter the doctor name:\n"))

        # loop the doctor list to check if there is a a matched one
        for doctor in self.doctors:
            if name == str(doctor.name):
                found = True
                print ("{:<4} {:<22} {:<15} {:<15} {:<15} {:<10}".format(doctor.id, doctor.name, doctor.specilist , doctor.timing, doctor.qualification, doctor.room_no))
                    
        if found == False:
            print("Can't find the doctor with the same name on the system")

    def display_doctor_info(self):
        for doctor in self.doctors:
            info = [doctor.id, doctor.name, doctor.specialist, doctor.timing, doctor.qualification, doctor.room_no]
            print(f"{doctor.name}: {info}\n")

    # Asks the user to enter the ID of the doctor to change their information, and then the user can enter the new doctor information
    def edit_doctor_info(self):
        found = False
        id = input("Please enter the id of the doctor that you want to edit their information: ")
        #loop the doctor list to find the doctor that will be updated
        for doctor in self.doctors:
            if id == doctor.id:
                found = True
                # enter the new doctor information & update the doctor information in the list
                # doctor object is mutable
                doctor.name = input("Enter the doctor's name:\n")
                doctor.specilist = input("Enter the doctor's specilist:\n")
                doctor.timing = input("Enter the doctor's timing:\n")
                doctor.qualification = input("Enter the doctor's qualification:\n")
                doctor.room_no = int(input("Enter the doctor's room number:\n"))
                break
              
        if found == False:
            print("Can't find the doctor with the given id on the system")

    # Displays all the doctors’ information
    def display_doctors_list(self):
        # loop the doctor list to print out each doctor's information correctly
        for doctor in self.doctors:
            print ("{:<4} {:<22} {:<15} {:<15} {:<15} {:<10}".format(doctor.id, doctor.name, doctor.specilist , doctor.timing, doctor.qualification, doctor.room_no))

    # Writes the list of doctors to the doctors.txt file after formatting it correctly  
    def write_list_of_doctors_to_file(self):
        # loop the doctor list
        # call format_dr_info() for each doctor
        # then write the formatted data to doctors.txt
        with open("doctors.txt", "w") as doc_file:
            for doctor in self.doctors:
                formatted_doc = self.format_dr_info(doctor)
                doc_file.write(formatted_doc)
        print("Finished writing data from the list to doctors.txt.")

    # add a new doctor to the file
    def add_dr_to_file(self):
        # call enter_dr_info() to get new data from the user
        # call format_dr_info() to format new data
        # then write the formatted data to doctors.txt
        with open("doctors.txt", "a") as doc_file:
            new_doctor = self.enter_dr_info()
            self.doctors.append(new_doctor)
            formatted_doc = self.format_dr_info(new_doctor)
            doc_file.write(f"\n{formatted_doc}")
        print("Finished adding a new doctor to doctors.txt.")
