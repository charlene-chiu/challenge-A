# challenge-A

##   date_difference.py
### Description:
This program calculates the number of full days elapsed between two events.
###  Usage:
`python date_difference.py -f [datetime 1] -s [datetime 2]`  
### Example: 
`python date_difference.py -f 01/12/2020 -s 02/05/2022`
### Output: 
`516`

##   validation.py
### Description:
This program validate the result of date_difference.py and generate random cases.
###  Usage:
`python validation.py -r 0 -f 01/12/2020 -s 02/05/2022`  
### Example: 
1. Case validation: `python validation.py -r 0 -f 01/12/2020 -s 02/05/2022`
2. Random case validation: `python validation.py -r 1`
### Output: 
1. `Date 1: 01/12/2020` <br>
`Date 2: 02/05/2022` <br>
`01/12/2020 - 02/05/2022 = 516`
2. `Date 1: 17/01/2684`<br>
`Date 2: 12/10/2389`<br>
`17/01/2684 - 12/10/2389 = 107477`
