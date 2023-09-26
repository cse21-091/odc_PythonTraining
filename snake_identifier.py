run = "yes"
snake_count = 0
while run == "yes":
    colour = input("Is snake Brown?")
    if colour == "yes":
        pattern = input("Does it have a coffin shaped head?")
        if pattern == "yes":
            print("Snake is venomous - Black Mamba")
        else:
            print("Snake is non venomous - Olive Grass Snake")
    else:
        pattern = input("Does it have a pale yellow underside?")
        if pattern == "yes":
            print("Snake is venomous  - Green Mamba")
        else:
            print("Snake is non venomous - Green Water Snake")
    snake_count += 1
    print(snake_count, "Snakes counted")

    run = input("Check another snake?")
