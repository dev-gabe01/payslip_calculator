# payslip_calculator

## Contents
## 1. Introduction
## 2. Run Script
## 3. Coding Decisions


## 1. Introduction ##

This is a console application that given employee annual salary details outputs a monthly pay slip.

Attributes of the employee are:
• name
• annual salary

Attributes of the monthly pay slip are:
• name
• gross monthly income
• monthly income tax
• net monthly income
= annual salary / 12 (months)
= (annual tax rate as provided below) / 12 (months) = gross monthly income - income tax

The following annual tax rates apply:

| Taxable income     | Tax on this income            |
| -------------------|:-----------------------------:|
| $0 - $20,000       | $0                            |
| $20,001 - $40,000  | 10c for each $1 over $20,000  |
| $40,001 - $80,000  | 20c for each $1 over $40,000  |    
| $80,001 - $180,000 | 30c for each $1 over $80,000  |    
| $180,001 and over  | 40c for each $1 over $180,000 |

## 2. Run Script ##

Run the script with python along with the two arguments, n for name and s for salary. i.e.
python GenerateMonthlyPayslip.py -n Lulu -s 100000

To run the test script, you will need to run:
python test_module.py

## 3. Coding Decisions ##

I have written the majority of the code in the tax module. Writing code in modules adds reusability and simplicity.

In the GenerateMonthlyPayslip script I have opted for key arguments rather than positional arguments. This makes the code more robust and will not error out depending on the whether the salary or name is inputed first. There is also an error catcher for the input types for salary or name. If salary is not an integer or name is not a string, it will throw an error.

I have also decided to include a help function to make usability easier for the end user.

I included a simple test to make sure that the values the script is generating matches what is expected.
