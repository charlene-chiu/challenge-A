
"""
This program generates random input to test date_difference.py.
Date: 2022/11/21
Version: 1
Edited by Charlene Chiu
"""
import datetime
import random
import date_difference
import argparse

def get_parser():
    parser = argparse.ArgumentParser(prog='validation.py', description='Validation of dates calcualtions. \n e.g., validation.py -r 0 -f 01/01/2022 -s 31/12/2021')
    parser.add_argument('-f', '--first', default='29/12/2020', type=str, help='date 1')
    parser.add_argument('-s', '--second', default='03/12/2020', type=str, help='date 2')
    parser.add_argument('-r', '--randomVar', choices=[0, 1], default=1, type=int, help='random input; 0: no, 1: yes')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    return parser

def randomDate():
    start_date = datetime.date(1901, 1, 1)
    end_date = datetime.date(2999, 12, 31)

    time_between_dates = end_date - start_date
    #print(time_between_dates)
    # to get the number of days from time_between_dates
    days_between_dates = time_between_dates.days 
    #print(days_between_dates)
    # random.randrange(days) to get a random integer less than the previous result days
    random_number_of_days_1 = random.randrange(days_between_dates) 
    random_number_of_days_2 = random.randrange(days_between_dates) 
    #print(random_number_of_days)
    # datetime.timedelta(days=n) to get a datetime.timedelta representing the previous result n
    random_date_1 = start_date + datetime.timedelta(days=random_number_of_days_1)
    random_date_2 = start_date + datetime.timedelta(days=random_number_of_days_2)
    return random_date_1, random_date_2

def main(input1, input2, random_var):
    format = '%d/%m/%Y'
    if random_var == 1:
        random_date = randomDate()
        test_date_1 = random_date[0].strftime(format)
        test_date_2 = random_date[1].strftime(format)
        print("Date 1: " + test_date_1)
        print("Date 2: " + test_date_2)

        delta_days = random_date[0] - random_date[1]
        validation_days = abs(delta_days.days) - 1
        my_days = date_difference.main(test_date_1, test_date_2)

        if int(my_days) == validation_days:
            print(test_date_1 + " - " + test_date_2 + " = " + str(my_days))
        else:
            print(">>>>>>>ERROR")
            print("Correct answer: " + str(validation_days))
            print("My answer: " + str(my_days))
            print("<<<<<<<<<<<")
    else:
        date1 = datetime.datetime.strptime(input1, format)
        date2 = datetime.datetime.strptime(input2, format)
        print("Date 1: " + input1)
        print("Date 2: " + input2)

        delta_days = date1  - date2
        validation_days = abs(delta_days.days) - 1
        my_days = date_difference.main(input1, input2)

        if int(my_days) == validation_days:
            print(input1 + " - " + input2 + " = " + str(my_days))
        else:
            print(">>>>>>>ERROR")
            print("Correct answer: " + str(validation_days))
            print("My answer: " + str(my_days))
            print("<<<<<<<<<<<")        

if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()        
    res = main(input1 = args.first, input2 = args.second, random_var = args.randomVar)
