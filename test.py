from esodate import *
from datetime import *

# pairs of equivalent dates and ddates for conversion tests
dates = [
	[date(2019, 4, 5), ddate(3185, 2, 22)],
	[date(2072, 8, 11), ddate(3238, 4, 4)],
	[date(2074, 8, 11), ddate(3240, 4, 4)],
	[date(2076, 2, 28), ddate(3242, 1, 59)],
	[date(2076, 2, 29), ddate(3242, 1, 60)],
	[date(2076, 3, 1), ddate(3242, 1, 61)],
]

assert ddate(3242, 1, 59).day_of_year() == 59
assert ddate(3242, 1, 60).day_of_year() == 60
assert ddate(3242, 1, 61).day_of_year() == 61

for pair in dates:
	a = ddate(date=pair[0])
	b = pair[1].date()
	assert a == pair[1]
	assert b == pair[0]
	assert a.date() == pair[0]
	assert ddate(date=b) == pair[1]

print("\n\nall tests completed\n")