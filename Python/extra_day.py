#This is a problem from hackerrnak, 'Write a function'
def isEvenly(number,divisor):
    result = not bool(number%divisor)
    return  result


def is_leap(year):
    leap = False
    if isEvenly(year,4):
        leap = True
        if isEvenly(year,100):
            leap = False
            if isEvenly(year,400):
                leap = True
    return leap

year = int(input())
print(is_leap(year))
