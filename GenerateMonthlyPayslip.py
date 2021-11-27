import sys
import getopt
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
		try:
			name = str(arg)
		except Exception as err:
			print("Encountered an error. Are you sure the name you have put in is correct?")
			print(err)
			sys.exit(2)
	if opt in ("-s", "--salary"):
		foundSalary = True
		try:
			name = int(arg)
		except Exception as err:
			print("Encountered an error. Are you sure the salary you have put in is correct?")
			print(err)
			sys.exit(2)

if not foundName:
    print("A name operation is required")
    tax_module.help()

if not foundSalary:
    print("A salary is required")
    tax_module.help()


if __name__ == "__main__":
	if len(sys.argv) <= 3:
		tax_module.help()
	tax_module.main(name,salary)
