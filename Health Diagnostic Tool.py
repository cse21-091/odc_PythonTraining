import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class HealthDiagnosticApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Health Diagnostic Tool")

        # Load and resize the background image
        background_image = Image.open("C:/Users/cse21-091/OneDrive - Botswana Accountancy College/Pictures/Camera Roll/Retro Computer Aesthetic HD Wallpapers   Top Retro Computer.jpg")
        self.background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_widgets()

    def create_widgets(self):
        self.instructions_label = tk.Label(self.root, text="ANSWER THE FOLLOWING QUESTIONS WITH 'YES' OR 'NO':", font=("Helvetica", 20, "bold"))
        self.instructions_label.pack(pady=10)

        self.name_var = tk.StringVar(value="")
        self.age_var = tk.IntVar(value=0)

        name_label = tk.Label(self.root, text="FIRST NAME:", font=("Helvetica", 20, "bold"))
        name_label.pack()
        self.name_entry = tk.Entry(self.root, textvariable=self.name_var, font=("Helvetica", 20))
        self.name_entry.pack()

        age_label = tk.Label(self.root, text="AGE:", font=("Helvetica", 20, "bold"))
        age_label.pack()
        self.age_entry = tk.Entry(self.root, textvariable=self.age_var, font=("Helvetica", 20))
        self.age_entry.pack()

        self.fever_var = tk.StringVar(value="no")
        self.cough_var = tk.StringVar(value="no")
        self.breathing_var = tk.StringVar(value="no")
        self.fatigue_var = tk.StringVar(value="no")

        self.create_question("Do you have a fever?", self.fever_var)
        self.create_question("Do you have a persistent cough?", self.cough_var)
        self.create_question("Are you experiencing difficulty in breathing?", self.breathing_var)
        self.create_question("Do you feel unusually fatigued?", self.fatigue_var)

        self.submit_button = tk.Button(self.root, text="DIAGNOSE", command=self.diagnose, font=("Helvetica", 20, "bold"))
        self.submit_button.pack(pady=20)

    def create_question(self, text, var):
        question_frame = tk.Frame(self.root, bg="lightblue")  # Change background color
        question_label = tk.Label(question_frame, text=text, font=("Helvetica", 20, "bold"))
        question_label.pack(side="left", padx=10)
        yes_radio = tk.Radiobutton(question_frame, text="YES", variable=var, value="yes", font=("Helvetica", 20, "bold"))
        yes_radio.pack(side="left")
        no_radio = tk.Radiobutton(question_frame, text="NO", variable=var, value="no", font=("Helvetica", 20, "bold"))
        no_radio.pack(side="left")
        question_frame.pack(pady=5)

    def diagnose(self):
        name = self.name_var.get()
        age = self.age_var.get()

        fever = self.fever_var.get() == 'yes'
        cough = self.cough_var.get() == 'yes'
        breathing_difficulty = self.breathing_var.get() == 'yes'
        fatigue = self.fatigue_var.get() == 'yes'

        if age < 15:
            department = "PEDIATRICIAN DEPARTMENT"
            message = f"DUE TO YOUR AGE, IT'S RECOMMENDED THAT YOU VISIT OUR {department}."
            messagebox.showinfo("RECOMMENDED DEPARTMENT", message)
        else:
            if fever or cough or breathing_difficulty or fatigue:
                result = "COVID-19"
                department = "COVID-19 DEPARTMENT IN BLOCK 2"
            elif fever or cough or fatigue:
                result = "COMMON COLD"
                department = "GENERAL PRACTITIONER IN ROOM 5"
            elif not (fever or cough or breathing_difficulty or fatigue):
                result = "GOOD HEALTH"
                department = "GENERAL NURSE IN ROOM 1"
            else:
                result = "RESPIRATORY PROBLEMS"
                department = "PULMONOLOGIST IN ROOM 3"

            message = f"BASED ON YOUR SYMPTOMS, IT APPEARS TO BE {result}. PLEASE PROCEED TO SEE {department} FOR FURTHER EVALUATION."
            messagebox.showinfo("DIAGNOSIS RESULT", message)

def main():
    root = tk.Tk()
    app = HealthDiagnosticApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

# COVID-19 Self-Diagnosis System and questions
print("WELCOME TO THE GPH COVID-19 SELF DIAGNOSIS SYSTEM")
print("WE KINDLY REQUEST YOU TO FOLLOW THE PROMPTS BELOW")

def sd_contact(x):
    x = bool(x)
    if x == 1:
        print("IF YOU HAVE BEEN IN CONTACT WITH ANYONE YOU MAY KNOW, THEN INFORM THEM TO SELF-ISOLATE AND GET TESTED")

us_name = input("PLEASE PROVIDE US WITH YOUR FULL NAME:\n")
us_age = int(input(f"{us_name}, HOW OLD ARE YOU?\n"))
us_temp = float(input(f"{us_name}, WHAT WAS YOUR RECORDED TEMPERATURE?\n"))

if us_temp > 38.0:
    print("YOU HAVE A FEVER")
    sd_cough = int(input(f"{us_name}, DO YOU HAVE A COUGH? (1 FOR YES, 0 FOR NO)\n"))
    if sd_cough == 1:
        sd_sthroat = int(input(f"{us_name}, DO YOU HAVE A SORE THROAT? (1 FOR YES, 0 FOR NO)\n"))
        if sd_sthroat == 1:
            sd_sbreath = int(input(f"{us_name}, DO YOU HAVE SHORTNESS OF BREATH? (1 FOR YES, 0 FOR NO)\n"))
            if sd_sbreath == 1:
                sd_sbody = int(input(f"{us_name}, DO YOU HAVE A SORE BODY/ACHING BODY? (1 FOR YES, 0 FOR NO)\n"))
                if sd_sbody == 1:
                    sd_sbreath = str(sd_sbreath)
                    sd_sbody = str(sd_sbody)
                    print(f"{us_name}, YOU MAY HAVE COVID-19\n"
                          f"YOUR TEMPERATURE WAS {us_temp} DEGREES\n"
                          f"AND YOUR SYMPTOMS WERE:\n"
                          f"SHORTNESS OF BREATH: {sd_sbreath}\n"
                          f"SORE BODY/ACHING BODY: {sd_sbody}\n")
                    print(sd_contact(1))
                else:
                    print(f"{us_name}, YOU MAY HAVE EARLY SIGNS OF COVID-19\n"
                          f"YOUR TEMPERATURE WAS {us_temp} DEGREES\n"
                          f"AND YOUR SYMPTOMS WERE:\n"
                          f"SHORTNESS OF BREATH: {sd_sbreath}\n"
                          f"SORE BODY/ACHING BODY: {sd_sbody}\n")
                    print(sd_contact(1))
            else:
                print(f"{us_name}, BASED ON YOUR SYMPTOMS, IT'S MORE LIKELY THAT YOU HAVE A COMMON FLU\n"
                      f"YOUR TEMPERATURE WAS {us_temp} DEGREES\n"
                      f"AND YOUR SYMPTOMS WERE:\n"
                      f"COUGHING: {sd_cough}\n"
                      f"SORE THROAT: {sd_sthroat}\n"
                      f"PLEASE CONSULT THE GENERAL PRACTITIONER TO RECEIVE MEDICAL ATTENTION IF NECESSARY")
        else:
            print(f"{us_name}, BASED ON YOUR SYMPTOMS, IT'S MORE LIKELY THAT YOU HAVE A DRY COUGH\n"
                  f"YOUR TEMPERATURE WAS {us_temp} DEGREES\n"
                  f"AND YOUR SYMPTOMS WERE:\n"
                  f"COUGHING: {sd_cough}\n"
                  f"PLEASE CONSULT THE GENERAL PRACTITIONER TO BE PRESCRIBED WITH MEDICATION")
    else:
        print(f"{us_name}, PLEASE CONSULT YOUR PHARMACIST FOR OVER-THE-COUNTER MEDICATION\n"
              f"AND CLOSELY MONITOR YOUR SYMPTOMS; IF THEY ARE DEVELOPING, CONSULT A MEDICAL PROFESSIONAL")
else:
    print(f"{us_name}, PLEASE WAIT AT THE RECEPTION; A CONSULTANT WILL BE WITH YOU SHORTLY.")

print("THANK YOU FOR USING THE GPH COVID-19 SELF DIAGNOSIS SYSTEM")
