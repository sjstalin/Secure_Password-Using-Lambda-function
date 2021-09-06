'''Python Programming Lab4- Lambda Functions.
    Joshua Stalin S 2147118
    04/09/2021'''
# to check the Length of the Pass

def pass_test(password):
    length = len(password)
    return int(length)


#to check the Strenght of Pass
# setting up constants to check if all the Conditions are justified

def pass_strength(password):
    c = 0
    l = 0
    d = 0
    u = 0

    for x in password:

        if x.lower():
            l = 1

        if x.isdigit():
            d = 1

        if x.isalnum() == False:
            c = 1

        if x.upper():
            u = 1


    #print(l, d, c, u)
    strength = l + d + c + u

    # the strength should be 4
    return int(strength)

# lambda function
# def lambda_function(lenght,strength):
# return lambda lenght, strength: lenght + strength

lambda_function = lambda length, strength: length + strength