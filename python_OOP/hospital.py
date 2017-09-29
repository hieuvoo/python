# Patient:
# Attributes:
# Id: an id number
# Name
# Allergies
# Bed number: should be none by default
class Patient(object):
    def __init__(self, id_num, name, bed_num, *allergies):
        self.bed = bed_num
        self.id = id_num
        self.name = name
        self.allergies = allergies
# Hospital
# Attributes:
# Patients: an empty array
# Name: hospital name
# Capacity: an integer indicating the maximum number of patients the hospital can hold.
class Hospital(Patient):
    def __init__(self, hospital_name, capacity):
        self.patients = []
        self.hospital_name = hospital_name
        self.capacity = capacity
# Methods:
# Admit: add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the capacity do not admit the patient. Return a message either confirming that admission is complete or saying the hospital is full.
    def admit(self, id, name, *allergies):
        super(Hospital, self).__init__(id, name, 0, *allergies)
        if len(self.patients) >= self.capacity:
            print "The hospital is full"
        else:
            if len(self.patients) == 0:
                self.bed_num = 1
            else:
                self.bed_num = 1
                for i in range(len(self.patients)):
                    if self.patients[i][3] != self.bed_num:
                        pass
                    else:
                        self.bed_num += 1
            print self.name, "admitted to", self.hospital_name, "in bed: ", self.bed_num
            self.patients.append([self.id,self.name,self.allergies,self.bed_num])
        return self
# Discharge: look up and remove a patient from the list of patients. Change bed number for that patient back to none.
    def discharge(self, patient_name):
        for i in range(len(self.patients)-1):
            if self.patients[i][1] == patient_name:
                print self.patients[i][1], "discharged from bed ", self.patients[i][3]
                self.patients.pop(i)
        return self
    def info(self):
        print self.patients

hospital1 = Hospital("General", 1000)
hospital1.admit(1,"Hieu","meh")
hospital1.admit(2,"Angela","Took a selfie in traffic")
hospital1.admit(3,"Ein","Allergic to everything")
hospital1.admit(4,"Homer","Alcohol poisoning")
hospital1.discharge("Hieu")
hospital1.admit(5,"Bart","meh")
hospital1.admit(6,"Lisa","meh")
hospital1.info()