#!/usr/bin/python

''':
   Copyright 2018 Justin Snow 
   Written by: Justin Snow
   https://github.com/Jrsnow8921/PayDates
   Licensed under the MIT License
'''

from datetime import *

class PayDays(object):

  def __init__(self, start, fx, save=0):
    self.start = start
    self.fx = fx
    self.save = save

  def main(self):
    x = self.payDays()
    a = []
    print "This year you'll have (" + str(len(x)) + ") paydays."
    for y in x:
      if self.save == 1:
         b = y.strftime("%m-%d-%Y")
         a.append(b)
      else:
        print y.strftime("%m-%d-%Y")
    if self.save == 1:
      self.savePayDays(a)

  def payDays(self):
    try:
      days = [self.start + timedelta(days=x) for x in range(0, self.daysPassed() + self.fx, self.fx)]
    except:
      print "Something went wrong..."
    return days

  def daysPassed(self):
    try:
      first_of_year = datetime(year=datetime.now().year, month=1, day=1)
      todays_date = datetime.now()
      passed = 365 - (todays_date - first_of_year).days 
    except:
      "Something went wrong..."
    return int(passed)

  def savePayDays(self, x):
    try:
      f = open("payDates.txt", "w")
      f.write("\n".join(map(lambda x: str(x), x)) + "\n")
    except:
      print "Unable to save to file"

PayDays(datetime(year=datetime.now().year, month=1, day=11), 14, 1).main()


