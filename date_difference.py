"""
This program calculates the number of full days elapsed between two events.
Date: 2022/11/21
Version: 1
Edited by Charlene Chiu
"""
import argparse

def transDate(date):
    date_cut = date.split("/")
    date_string = date.replace("/","")
    if len(date_string) == 8 and len(date_cut[2]) == 4 :
        date_string = date_string[4:] + date_string[2:4] + date_string[:2]
        return date_string
    else:        
        return 0
    
def leapYear(trans_date):
    """
    % 4 leap year; % 100 normal year; %400 leap year
    """
    year = int(trans_date[:4])
    if ((year % 4 == 0) and (year % 100 > 0)) or (year % 400 == 0):
        return 1
    else:
        return 0

def btwDays(trans_date1, trans_date2, hash_table):
    """
    to get the number of days from trans_date1 and trans_date2 with hash_table
    """    
    ans = abs(hash_table[trans_date2] - hash_table[trans_date1])
    ans = ans - 1
    return ans

def buildHash(start_date, end_date):
    """
    Establish date hash table
    """        
    trans_start_date = transDate(start_date)
    trans_end_date = transDate(end_date)
    value = 0
    hash_table = {}
    key = trans_start_date
    big_month = ['01','03','05','07','08','10']
    small_month = ['04','06','09','11']

    while int(key) <= int(trans_end_date):
        hash_table[key] = value
        value+=1    
        # leap yaer & February
        if key[4:6] == '02' and leapYear(key) and key[6:] == '29':
            key = key[:4] + '03' + '01'
        elif key[4:6] == '02' and not leapYear(key) and key[6:] == '28':
            key = key[:4] + '03' + '01'
        elif key[4:6] in big_month and key[6:] == '31':
            key = key[:4] + str(int(key[4:6])+1).zfill(2) + '01'
        elif key[4:6] in small_month and key[6:] == '30':
            key = key[:4] + str(int(key[4:6])+1).zfill(2) + '01'
        # new year
        elif key[4:6] == '12' and key[6:] == '31':
            key = str(int(key[:4])+1) + '0101'
        else:
            key = str(int(key)+1)
    return hash_table

def dateCheck(trans_date):
    """
    Check date format
    """
    big_month = ['01','03','05','07','08','10','12']
    small_month = ['04','06','09','11'] 
    # YYYY goes wrong
    if int(trans_date[:4]) > 2999 or int(trans_date[:4]) < 1901:
        msg = "Invalid Year!"  
    # MM goes wrong
    elif int(trans_date[4:6]) > 12:
        msg = "Invalid Month!"    
    # DD goes wrong
    elif trans_date[4:6] == '02' and leapYear(trans_date) and int(trans_date[6:]) > 29: # leap year
        msg = "Invalid Day!"
    elif trans_date[4:6] == '02' and not leapYear(trans_date) and int(trans_date[6:]) > 28: # not leap year
        msg = "Invalid Day!"
    elif trans_date[4:6] in big_month and int(trans_date[6:]) > 31: 
        msg = "Invalid Day!"
    elif trans_date[4:6] in small_month and int(trans_date[6:]) > 30:
        msg = "Invalid Day!"
    return trans_date + ": " + msg

def get_parser():
    parser = argparse.ArgumentParser(prog='date_difference.py', description='Dates calcualtions. \n e.g., date_difference.py -f 01/01/2022 -s 31/12/2021')
    parser.add_argument('-f', '--first', default='29/12/2022', type=str, help='date 1')
    parser.add_argument('-s', '--second', default='03/12/2022', type=str, help='date 2')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    return parser

def main(input1, input2):
    # calender range
    hash_table = buildHash("01/01/1901", "31/12/2999") 
    #input1 = "29/13/2020"
    #input2 = "03/13/2020"
    date1 = transDate(input1)
    date2 = transDate(input2)
    # error check
    if date1 and date2:
        if date1 in hash_table and date2 in hash_table:
            res = btwDays(date1, date2, hash_table)
        elif (date1 not in hash_table) and (date2 not in hash_table) :
            print("Both " + input1 + " and " + input2 + " are not existing in hash table.")      
            res = dateCheck(date1) + dateCheck(date2)  
        elif date1 not in hash_table:
            print(input1 + " does not exist in hash table.")
            res = dateCheck(date1)  
        elif date2 not in hash_table:
            print(input2 + " does not exist in hash table.") 
            res = dateCheck(date2)
        return res
    else:
        return "Invalid Format!!"  

if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()        
    res = main(input1 = args.first, input2 = args.second)
    print(res)







