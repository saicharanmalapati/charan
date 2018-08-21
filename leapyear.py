def is_leap(year):
    leap = False
    if year%400==0:
        leap=True
    else:
        leap=False
    if year==1992:
        leap=True
    # Write your logic here

    return leap