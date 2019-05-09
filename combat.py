
pikachu_hp = 100
pikachu_speed_attack = 15
pikachu_volt_ball = 25

charmander_hp = 75
charmander_attack = 45

bulbasur_hp = 110
bulbasur_attack = 20

squirtle_hp = 135
squirtle_attack = 17

combat_select = input(print("who do you want to fight against? (charmander / bulbasur/ squirtle): "))

if combat_select == "charmander":
    print("GO CHARMANDER")

    while pikachu_hp > 0 and charmander_hp > 0:
        attack = input(print("select you attack (speed attack/ volt ball): "))
        if attack == "speed attack":
            charmander_hp = charmander_hp - pikachu_speed_attack
            print("Not very effective")
        if attack == "volt ball":
            charmander_hp = charmander_hp - pikachu_volt_ball
            print("Very effective")
        if charmander_hp <= 0:
            print("GZ")
            break
        pikachu_hp = pikachu_hp - charmander_attack
        print("charmander attack, your HP :", pikachu_hp)
        if pikachu_hp <= 0:
            print("You lose")
            break

elif combat_select == "bulbasur":
    print("GO BULBASUR")

    while pikachu_hp > 0 and bulbasur_hp > 0:
        attack = input(print("select you attack (speed attack/ volt ball): "))
        if attack == "speed attack":
            bulbasur_hp = bulbasur_hp - pikachu_speed_attack
            print("Not very effective")
        if attack == "volt ball":
            bulbasur_hp = bulbasur_hp - pikachu_volt_ball
            print("Very effective")
        if bulbasur_hp <= 0:
            print("GZ")
            break
        pikachu_hp = pikachu_hp - bulbasur_attack
        print("bulbasur attack, your HP :", pikachu_hp)
        if pikachu_hp <= 0:
            print("You lose")
            break

elif combat_select == "squirtle":
    print("GO SQUIRTLE")

    while pikachu_hp > 0 and squirtle_hp > 0:
        attack = input(print("select you attack (speed attack/ volt ball): "))
        if attack == "speed attack":
            squirtle_hp = squirtle_hp - pikachu_speed_attack
            print("Not very effective")
        if attack == "volt ball":
            squirtle_hp = squirtle_hp - pikachu_volt_ball
            print("Very effective")
        if squirtle_hp <= 0:
            print("GZ")
            break
        pikachu_hp = pikachu_hp - squirtle_attack
        print("squirtle attack, your HP :", pikachu_hp)
        if pikachu_hp <= 0:
            print("You lose")
            break


print("Your way has just begun")