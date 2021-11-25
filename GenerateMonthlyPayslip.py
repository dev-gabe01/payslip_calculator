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
	print("Example: python GenerateMonthlyPayslip.py -n Bernard Black -s 21000")
	sys.exit(2)

#opts, args = getopt.getopt(sys.argv[1:],"nsh:",["name","salary","help"])
opts, args = getopt.getopt(sys.argv[1:],"n:s:h",["name=","salary=", "help"])
option_dict = {
		"-n": "name",
		"--name": "name",
		"-s": "salary",
		"--salary": "salary"
}
foundName = False
foundSalary = False

for opt, arg in opts:
	if opt in ("-h", "--help"):
		help()
	if opt in ("-n", "--name"):
		foundName = True
		name = arg
	if opt in ("-s", "--salary"):
		foundSalary = True
		salary = arg

if not foundName:
    print("A name operation is required")
    help()

if not foundSalary:
    print("A salary is required")
    help()

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
	elif y_income > 20001 and y_income < 40000:
		y_taxed = (y_income - 20000) * 0.1
		m_taxed = y_taxed/12
	elif y_income > 40001 and y_income < 80000:
		y_taxed = ((40000 - 20000) * 0.1 ) + ((y_income - 40000) * 0.2)
		m_taxed = y_taxed/12
	elif y_income > 80001 and y_income < 180000:
		y_taxed = ((40000 - 20000) * 0.1 ) + ((80000 - 40000) * 0.2) + ((y_income - 80000) * 0.3)
		m_taxed = y_taxed/12
	elif y_income > 180001:
		y_taxed = ((40000 - 20000) * 0.1 ) + ((80000 - 40000) * 0.2) + ((180000 - 80000) * 0.3) + ((y_income - 180000) * 0.4)
		m_taxed = y_taxed/12
	return y_taxed,m_taxed

def net_income(y_income,y_taxed,m_income,m_taxed):
	y_net_income = 0
	m_net_income = 0
	y_net_income = y_income - y_taxed
	m_net_income = m_income - m_taxed
	return y_net_income,m_net_income


def main(name,salary):
	#WRITE A SUMMARY THING HERE BEOFRE WRITE TO FILE
	y_taxed,m_taxed = tax_on_income(salary)
	y_net = (int(salary) - int(y_taxed))
	m_net = (int(monthly_income(salary)) - int(m_taxed))
	print("\nSummary")
	print("-----------------")
	print("The Monthly Payslip for: %s" % name)
	print("With a Yearly income before tax of: %s" % salary)
	print("With a Yearly income after tax of: %s" % y_net)
	print("With a Monthly income before tax of: %s" % monthly_income(salary))
	print("With a Monthly income after tax of: %s" % m_net)


if __name__ == "__main__":
	if len(sys.argv) <= 3:
		help()
	main(name,salary)
