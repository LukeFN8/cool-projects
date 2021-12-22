is_dodo = "true"
tim = 0
choise = 0
dodometer = 3
dif = int(input("easy:1,medium:2,hard:3 "))
if dif == 1:
    tim = 10
elif dif == 2:
    tim = 5
elif dif == 3:
    tim = 3
while is_dodo == "true" or tim != 0:
    print("you are a dodo butt. do things to be less shity")

    choise = int(input("press 1 to not be a dodo butt "))
    if choise == 1:
        dodometer = 0
    if dodometer == 0:
        is_dodo = "false"
        tim = 0
