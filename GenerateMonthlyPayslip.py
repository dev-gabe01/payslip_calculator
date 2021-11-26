# Python 2/3 Compatibility
from __future__ import print_function
from builtins import input
from builtins import str

import os
import sys
import getopt
import re
import tax_module


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
		tax_module.help()
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


if __name__ == "__main__":
	if len(sys.argv) <= 3:
		tax_module.help()
	tax_module.main(name,salary)
