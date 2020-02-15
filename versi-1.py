#############################################
#                                           #
#           Credit : Rijal Islami           #
#           Instagram : @ishurami           #
#                                           #
#############################################
#                                           #
#   Version 1 just has a few features,      #
#     like the loop limited to 10 times.    #
#   If your score reach 10 or you type      #
#     the wrong number 3 times, then the    #
#     program will stop                     #
#                                           #
#############################################

from numpy.random import randint

score = 0
wrong = 0
ans = 0

# max score is 10
val_1 = randint(0, 10)
print(val_1)

while score < 10 and wrong < 3:
    val_2 = randint(0, 10)
    print(val_2)
    value = val_1 + val_2
    ans = int(input('   '))

    if value % 10 == ans:
        score += 1
    else:
        wrong += 1

    val_1 = val_2

print("Your score :", score)
