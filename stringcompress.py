from itertools import groupby
string = input()
for items, group in groupby(string):
    print((len(list(group)), int(items)), end=" ")
