#! /usr/bin/python3

#test regular expressions to extract a particular value from a line of text

import re

#takes in a regex expression and test_string and return matching values
#if found else report not found
def test_regular_expression(regex, test_string):
    pattern = re.compile(r'' + regex )
    match   = pattern.search(test_string)
    if match :
        try :
            return match.group(1)
        except :
            print('Match found but no substring returned')
            return ''
        else:
            print(regex, 'does not match', string)
            return ''

auth_log_line = 'Mar 16 11:58:13 it20 sshd[12041]: Accepted password for it341 from 65.96.149.57 port 60695 ssh2'
apache_log_line = '205.236.184.32 - - [09/Mar/2014:00:03:21 +0000] "GET /wzbc-2014-03-05-14-00.mp3 HTTP/1.1" 200 56810323'

regex_1 = r"(\D{3}\s\d{2}\s)"
regex_2 = r"(\d{2}\:{1}\d{2}\:{1}\d{2})"
regex_3 = r"\d{2}\:{1}\d{2}\:{1}\d{2}(.*)sshd{1}"
regex_4 = r"sshd\[(\d*)\]"
regex_5 = r"for\s(.{5})"
regex_6 = r"\s(\d*\.\d*\.\d*\.\d*)\s"
regex_7 = r"port\s(\d*)\s"
regex_8 = r"(\d*\.\d*\.\d*\.\d*)"
regex_9 = r"(\d{2}\/\D*\/\d{4})"
regex_10 = r"GET\s(\S*)"

print('regex_1', regex_1, '\t returned ', test_regular_expression(regex_1, 
    auth_log_line))
print('regex_2', regex_2, '\t returned ', test_regular_expression(regex_2, 
    auth_log_line))
print('regex_3', regex_3, '\t returned ', test_regular_expression(regex_3, 
    auth_log_line))
print('regex_4', regex_4, '\t returned ', test_regular_expression(regex_4, 
    auth_log_line))
print('regex_5', regex_5, '\t returned ', test_regular_expression(regex_5, 
    auth_log_line))
print('regex_6', regex_6, '\t returned ', test_regular_expression(regex_6, 
    auth_log_line))
print('regex_7', regex_7, '\t returned ', test_regular_expression(regex_7, 
    auth_log_line))
print('regex_8', regex_8, '\t returned ', test_regular_expression(regex_8, 
    apache_log_line))
print('regex_9', regex_9, '\t returned ', test_regular_expression(regex_9, 
    apache_log_line))
print('regex_10', regex_10, '\t returned ', test_regular_expression(regex_10
    , apache_log_line))



