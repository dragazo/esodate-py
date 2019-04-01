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

# -- gregorian date -- #

@total_ordering
class GregorianDate:
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day
	
	# returns a copy of the current date
	def copy(self):
		return GregorianDate(self.year, self.month, self.day)
	
	# compares two gregorian dates
	def __eq__(self, other):
		return self.year == other.year and self.month == other.month and self.day == other.day
	def __lt__(self, other):
		if self.year < other.year: return True
		if self.year > other.year: return False
		
		if self.month < other.month: return True
		if self.month > other.month: return False
		
		return self.day < other.day
	
	# ------------------------------------------------
	
	# return true iff this is a leap year
	def leap_year(self):
		if self.year % 400 == 0: return True
		if self.year % 100 == 0: return False
		return self.year % 4 == 0
	
	# gets the number of days in the current month
	def days_in_month(self):
		if self.month == 2 and self.leap_year(): return 29
		return (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)[self.month - 1]
	
	# gets the number of days in the current year
	def days_in_year(self):
		return 366 if self.leap_year() else 365
	
	# ------------------------------------------------
	
	# gets the number of days into the current year this is.
	# the first day of the year returns 1.
	def day_of_year(self):
		pos = GregorianDate(self.year, 1, 1)
		days = self.day
		
		while self.month != pos.month:
			dim = pos.days_in_month()
			days += dim
			pos.adv(dim)
		
		return days
	
	# ------------------------------------------------
	
	# gets the name of this month
	def month_name(self):
		return (None, "January", "February", "March", "April", "May",
			"June", "July", "August", "September", "October",  "November",
			"December")[self.month]
	
	def __str__(self):
		return "{} {}, {}".format(
			self.month_name(), self.day, self.year)
	
	# ------------------------------------------------
	
	# advances the current date object by the specified number of days.
	# returns self.
	def adv(self, days):
		for i in range(0, days):
			if self.day == self.days_in_month():
				self.day = 1
				if self.month == 12:
					self.month = 1
					self.year += 1
				else:
					self.month += 1
			else:
				self.day += 1
		return self
		
	# ------------------------------------------------
	
	def to_discordian(self):
		return DiscordianDate(self.year + 1166, 1, 1).adv(self.day_of_year())
		
# -- discordian date -- #

@total_ordering
class DiscordianDate:
	def __init__(self, year, season, day):
		self.year = year
		self.season = season
		self.day = day
	
	# returns a copy of the current date
	def copy(self):
		return DiscordianDate(self.year, self.season, self.day)
	
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
		return (self.season - 1) * 73 + self.day

	# ------------------------------------------------

	# gets the name of the current season
	def season_name(self):
		return (None, "Chaos", "Discord", "Confusion", "Bureacracy",
			"Aftermath")[self.season]
	
	# gets the name of the current day
	def day_name(self):
		total_days = self.day_of_year()
		return ("Sweetmorn", "Boomtime", "Pungenday", "Prickle-Prickle",
			"Setting Orange")[(total_days - 1) % 5]
		
	def __str__(self):
		return "{}, the {} day of {} in the YOLD {}".format(
			self.day_name(), nth(self.day), self.season_name(), self.year)

	# ------------------------------------------------

	# advances the current date object by the specified number of days.
	# returns self.
	def adv(self, days):
		for i in range(0, days):
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
	
	def to_gregorian(self):
		return GregorianDate(self.year - 1166, 1, 1).adv(self.day_of_year())

