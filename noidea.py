n, m = map(int, input().split())
arr = set(input().split(' '))
a = set(input().split(' '))
b = set(input().split(' '))
happiness = 0

for i in arr:
    if i in a:
        happiness += 1
    if i in b:
        happiness -= 1
print(happiness)
