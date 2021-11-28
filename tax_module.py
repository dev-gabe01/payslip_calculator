# Python 2/3 Compatibility
from __future__ import print_function
from builtins import input
from builtins import str

import os
import sys
import getopt
import re

def help():
	print("Usage: \n")
	print("-n,  --name  : Set name\n")
	print("-s,  --salary   : Set yearly salary \n")
	print("Example: python GenerateMonthlyPayslip.py -n \"Bernard Black\" -s 21000")
	sys.exit(2)

def monthly_income(salary):
	y_income = int(salary)
	m_income = y_income/12
	return m_income

def tax_on_income(salary):
	y_income = int(salary)
	y_taxed = 0
	m_taxed = 0
	if y_income < 20001:
		pass
	elif y_income > 20000 and y_income < 40001:
		y_taxed = (y_income - 20000) * 0.1
	elif y_income > 40000 and y_income < 80001:
		y_taxed = ((40000 - 20000) * 0.1 ) + ((y_income - 40000) * 0.2)
	elif y_income > 80000 and y_income < 180001:
		y_taxed = ((40000 - 20000) * 0.1 ) + ((80000 - 40000) * 0.2) + ((y_income - 80000) * 0.3)
	elif y_income > 180000:
		y_taxed = ((40000 - 20000) * 0.1 ) + ((80000 - 40000) * 0.2) + ((180000 - 80000) * 0.3) + ((y_income - 180000) * 0.4)
	m_taxed = y_taxed/12
	return y_taxed,m_taxed

def net_income(y_income,y_taxed,m_income,m_taxed):
	y_net_income = 0
	m_net_income = 0
	y_net_income = int(y_income) - int(y_taxed)
	m_net_income = int(m_income) - int(m_taxed)
	return y_net_income,m_net_income

def main(name,salary):
	#WRITE A SUMMARY THING HERE BEOFRE WRITE TO FILE
	y_taxed,m_taxed = tax_on_income(salary)
	y_net,m_net = net_income(salary,y_taxed,monthly_income(salary),m_taxed)
	print("\nSummary")
	print("-----------------")
	print("The Monthly Payslip for: %s" % name)
	print("Gross Yearly Income: %s" % salary)
	print("Net Yearly Income: %s" % y_net)
	print("Gross Monthly Income: %s" % monthly_income(salary))
	print("Net Monthly Income: %s" % m_net)
	return m_net
