'''Python Programming Lab4- Lambda Functions.
    Joshua Stalin S 2147118
    04/09/2021'''

import pass_test as pt

i = 0

while i == 0:
    password = input("\t\t\t\t\t\t\tEnter the password: ")
    if pt.pass_test(password) < 8:
        print("\t\t\t\t\t\t\tPassword is too short\n")

    if pt.pass_strength(password) != 4:
        print("\t\t\t\t\t\t\t\t\tPlease enter a strong password\n")
        print("\t\t\t\t\tPassword should contain at least One (Uppercase,Character,Number,Lowecase)\n")

    else:
        final = pt.lambda_function(pt.pass_test(password), pt.pass_strength(password))
        if final >= 12:
            print("\t\t\t\t\t\t\t\tSecure Password!\n")
            i = 1