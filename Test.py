# 答案Solution for part02-20_next_leap_year
start_year = int(input("Year: "))
year = start_year + 1
while True:
    if year % 100 == 0:
        if year % 400 == 0:
            break
    elif year % 4 == 0:
        break
    year += 1
print(f"The next leap year after {start_year} is {year}")

# 我的
year = int(input('Year:'))
originalyear = year
## leap year or not?
def leapchecker(year):
    leapyearflag = 1
    if year % 100 == 0:
        if year % 400 == 0:
            leapyearflag = 0
        else:
            leapyearflag = 1
    elif year % 4 == 0:
        leapyearflag = 0
    return leapyearflag
## print
leapyearflag = leapchecker(year)
while True:
    if leapyearflag == 0:
        if leapchecker(year + 4) == 0:
            print(f'The next leap year after {year} is {year + 4}')
            break
    year += 1
    leapyearflag = leapchecker(year)
    if leapyearflag == 0:
        nextleap = year
        print(f'The next leap year after {originalyear} is {nextleap}')
        break