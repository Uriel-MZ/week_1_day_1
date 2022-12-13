def hi(uname):
    # print('Hi there ' + uname.title() + '!')
    return f'Hi there {uname.title()}!'

hi('SHOHA')

a = [4, 8, 3]
b = [5, 6, 7]

#Hello Padawans- 107!!!!!
# Use ctrl + / to comment things out (or cmd + / on mac)


def isCon(a_list):
    l = 0
    r = len(a_list) - 1
    while l < r:
        if a_list[l] + 1 != a_list[l+1]:
            return False
    return True




