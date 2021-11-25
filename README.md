# payslip_calculator
Version=1.0

Please ensure you have a well-written ReadMe which covers off why you built the solution the way you did, design decisions made, how to run your code/tests, assumptions & trade-offs made.




A console application that given employee annual salary details outputs a monthly pay slip.

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