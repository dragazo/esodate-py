from esodate import *

# gregorian leap year tests
assert GregorianDate(100, 1, 1).leap_year() == False
assert GregorianDate(101, 1, 1).leap_year() == False
assert GregorianDate(104, 1, 1).leap_year() == True
assert GregorianDate(200, 1, 1).leap_year() == False
assert GregorianDate(300, 1, 1).leap_year() == False
assert GregorianDate(400, 1, 1).leap_year() == True
assert GregorianDate(2000, 1, 1).leap_year() == True

# gregorian february leap year logic (based on leap years)
assert GregorianDate(1900, 2, 1).days_in_month() == 28
assert GregorianDate(1904, 2, 1).days_in_month() == 29

# gregorian days in year test (based on leap years)
assert GregorianDate(1900, 1, 1).days_in_year() == 365
assert GregorianDate(2020, 1, 1).days_in_year() == 366

# gregorian day of year test (based on leap years)
assert GregorianDate(1900, 12, 31).day_of_year() == 365
assert GregorianDate(2020, 12, 31).day_of_year() == 366

# gregorian date comparison tests
assert GregorianDate(1900, 12, 31) == GregorianDate(1900, 12, 31)
assert GregorianDate(1900, 12, 31) <= GregorianDate(1900, 12, 31)
assert GregorianDate(1900, 12, 31) >= GregorianDate(1900, 12, 31)
assert not (GregorianDate(1900, 12, 31) != GregorianDate(1900, 12, 31))
assert not (GregorianDate(1900, 12, 31) < GregorianDate(1900, 12, 31))
assert not (GregorianDate(1900, 12, 31) > GregorianDate(1900, 12, 31))

x = GregorianDate(1, 1, 1)
y = x.copy()

assert x == y
assert not x < y
assert x is not y

assert x < y.adv(1)
assert y.day == 2

for i in range(100): y.adv(y.days_in_year())
assert y > x
assert y.year == 101
assert y == GregorianDate(101, 1, 2)

print("\n\nall tests completed\n")