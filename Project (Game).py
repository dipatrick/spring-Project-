
                            #Course Project : GAME

print("Its A Game! So Find Out The Lucky Number ")

Lucky_Number = "44"
find = ""
find_count = 0
find_limit = 5
time_is_out = False
while find != Lucky_Number and not (time_is_out):
    if find_count < find_limit:
        find = input("Find Out!\n")
        find_count += 1
    else:
        time_is_out = True
if time_is_out:
        print("Sorry >You Lose try again!!!")
else:
        print("You Have Won The Lucky One Congz!!****")
