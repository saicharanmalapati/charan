def minion_game(string):
    # your code goes here
    ke = 0
    st = 0
    vowels = 'AEIOU'
    n = len(string)
    for i in range(n):
        if string[i] in vowels:
            ke = ke + (n - i)
        else:
            st = st + (n - i)
    if ke > st:
        print("Kevin", ke)
    elif st > ke:
        print("Stuart", st)
    else:
        print("Draw")
