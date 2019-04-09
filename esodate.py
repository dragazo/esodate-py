import math
import datetime
from functools import total_ordering

# given a number, returns e.g. '1st', '2nd', '13th', etc.
def nth(n):
	# get the sign prefix and fix n<0
	prefix = ""
	if n < 0:
		n = -n
		prefix = "-"

	# 11-13 in low 2 digits have special rules
	low_2 = n % 100
	if low_2 >= 11 and low_2 <= 13: return prefix + "{}th".format(n)
	
	# otherwise pick ending based of last digit
	return prefix + "{}{}".format(n, { 1:"st", 2:"nd", 3:"rd" }.get(n % 10, "th"))

# -- discordian date -- #

@total_ordering
class ddate:

	# constructs a new ddate from ddate params or a datetime.date object.
	# if date is specified, this is a lossless conversion to discordian date.
	def __init__(self, year=3166, season=1, day=1, date=None):
		if date is not None:
			self.year = date.year + 1166
			self.season = 1
			self.day = 1
			
			self.adv(date.timetuple().tm_yday - 1)
		else:
			self.year = year
			self.season = season
			self.day = day
			
	# converts this ddate into a datetime.date object.
	def date(self):
		return datetime.date(year=self.year - 1166, month=1, day=1) \
			+ datetime.timedelta(days=self.day_of_year()-1)
	
	def __copy__(self):
		return ddate(self.year, self.season, self.day)
	
	# compares two discordian dates
	def __eq__(self, other):
		return self.year == other.year and self.season == other.season and self.day == other.day
	def __lt__(self, other):
		if self.year < other.year: return True
		if self.year > other.year: return False
		
		if self.season < other.season: return True
		if self.season > other.season: return False
		
		return self.day < other.day
	
	# ------------------------------------------------
	
	# return true iff this is a leap year
	def leap_year(self):
		gyear = self.year - 1166 # do this in terms of gregorian years
		if gyear % 400 == 0: return True
		if gyear % 100 == 0: return False
		return gyear % 4 == 0
	
	# gets the number of days in the current season
	def days_in_season(self):
		return 74 if self.season == 1 and self.leap_year() else 73
	
	# gets the number of days in the current year
	def days_in_year(self):
		return 366 if self.leap_year() else 365
	
	# ------------------------------------------------
	
	# gets the number of days into the current year this is.
	# the first day of the year returns 1.
	def day_of_year(self):
		return (self.season - 1) * 73 + self.day + \
			(1 if self.leap_year() and self.season > 1 else 0)

	# ------------------------------------------------

	# gets the name of the current season
	def season_name(self):
		return ("Chaos", "Discord", "Confusion", "Bureacracy",
			"Aftermath")[self.season - 1]
	
	# gets the name of the current day
	def day_name(self):
		return ("Sweetmorn", "Boomtime", "Pungenday", "Prickle-Prickle",
			"Setting Orange")[(self.day_of_year() - 1) % 5]
		
	def __str__(self):
		return "{}, the {} day of {} in the YOLD {}".format(
			self.day_name(), nth(self.day), self.season_name(), self.year)

	# ------------------------------------------------

	# advances the current date object by the specified number of days.
	# returns self.
	def adv(self, days=1):
		for i in range(days):
			if self.day == self.days_in_season():
				self.day = 1
				if self.season == 5:
					self.season = 1
					self.year += 1
				else:
					self.season += 1
			else:
				self.day += 1
		return self
		
	# ------------------------------------------------
	
	

