#PatientDetails
firstName = input("Name: ")
surname = input("Surname: ")
age = input("age: ")
gender = input("gender: ")
contactDetails = input("contactDetails: ")
residence = input("Residence: ")
nextOfKin = input("NextOfKin: ")
mediAid = input("MedicalAid:\n1. Yes \n2. No\n ")
mediAid = int(mediAid)
if mediAid == 1:
    aidName = input("Name of Medical Aid: ")
elif mediAid == 2:
    print("Please pay consultation fee.")
print("Patient succesfully registered.")

#listofsymptoms
temperature = float(input("Temperature: "))
if temperature <=36.0:
    print("Temperature is low.")
elif temperature >= 38.0:
    print("Temperature is high. Please select your symptoms below:")
else:
    print("Temperature is within the normal range.You are free to go home, Please cotinue to stay safe! ")
print("Please select your symptoms.\n1. cough\n2. fever\n3. headache\n4. Shortness of breath\n5. Sore throat\n6. Fatigue\n")
symptom = input("")
symptom = int(symptom)
symptom = input("")
symptom = int(symptom)
symptom = input("")
symptom = int(symptom)

print("Please proceed to doctor's office.")
