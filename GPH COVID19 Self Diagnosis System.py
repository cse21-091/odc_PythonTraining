print("Welcome to the GPH COVID-19 Self Diagnosis System \nWe kindly request you to follow the prompts below")


def sd_contact(x):
    x = bool(x)

    if x == 1:
        print("If you have been in contact of anyone you may know,"
              "then inform them to self isolate and get tested")


us_name = input("Please provide us with your full name: \n")

us_age = input(f"{us_name}, how old are you? \n")

us_temp = float(input(f"{us_name}, what was your recorded temperature? \n"))

if us_temp > 38.0:
    print("You have a fever")
    sd_cough = int(input(f"{us_name}, do you have a cough?(1 for Yes, 0 for No)\n"))
    if sd_cough == 1:
        sd_sthroat = int(input(f"{us_name}, do you have a sore throat?(1 for Yes, 0 for No)\n"))
        if sd_sthroat == 1:
            sd_sbreath = int(input(f"{us_name}, do you have shortness of breath?(1 for Yes, 0 for No)\n"))
            if sd_sbreath == 1:
                sd_sbody = int(input(f"{us_name}, do you have a sore body/ aching body?(1 for Yes, 0 for No)\n"))
                if sd_sbody == 1:
                    sd_sbreath = str(sd_sbreath)
                    sd_sbody = str(sd_sbody)
                    print(f"{us_name}, you may have COVID-19\n"
                          f"Your temperature was {us_temp} degrees\n"
                          f"and your symptoms were:\n"
                          f"shortness of breath:{sd_sbreath}\n"
                          f"sore body/ aching body:{sd_sbody}\n")

                    print(sd_contact(1))

                else:
                    print(f"{us_name}, you may have early signs of COVID-19\n"
                          f"Your temperature was {us_temp} degrees\n"
                          f"and your symptoms were:\n"
                          f"shortness of breath:{sd_sbreath}\n"
                          f"sore body/ aching body:{sd_sbody}\n")

                    print(sd_contact(1))
            else:
                print(f"{us_name}, based on your symptoms, it's more likely that you have a common flu\n"
                      f"Your temperature was {us_temp} degrees\n"
                      f"and your symptoms were:\n"
                      f"coughing:{sd_cough}\n"
                      f"sore throat:{sd_sthroat}\n"
                      f"Please consult the general practitioner to receive medical attention if necessary")
        else:
            print(f"{us_name}, based on your symptoms, it's more likely that you have a dry cough\n"
                  f"Your temperature was {us_temp} degrees\n"
                  f"and your symptoms were:\n"
                  f"coughing:{sd_cough}\n"
                  f"Please consult the general practitioner to be prescribed with medication")
    else:
        print(f"{us_name}, please consult your pharmacist for off the counter medication\n"
              f"and closely monitor your symptoms, if it is developing\n"
              f"then consult a medical professional")

else:
    print(f"{us_name}, please wait at the reception, a consultant will be with you shortly.")

print("Thank you for using the GPH COVID-19 self diagnosis system")
