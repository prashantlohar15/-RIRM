# Ans 1
import re
list1 = ['2124567890','212-456-7890','(212)456-7890','(212)-456-7890','212.456.7890','212 456 7890','+12124567890','+12124567890',
          '+1 212.456.7890','+212-456-7890','1-212-456-7890']
Valid_Number = []
In_Valid_Number = []
for i in list1:
    if re.findall('[-+( ](\d{3})+[)-.]+(\d{3})+[-.]+(\d{4})+', i):
        Valid_Number.append(i)

    else:
        In_Valid_Number.append(i)
print('Valid contact number :', Valid_Number)
print('Not a valid contact number :', In_Valid_Number)


# Ans2
social_link = input('Input : ')

Social_links = '\n''https://www.facebook.com/fulioTech/''\n''https://www.linkedin.com/company/ful-io/'
mails = '\n''support@ful.io'
Contact = '\n''+1 343 303 6668'

if social_link=='https://ful.io':
    
    print('Social_links :',Social_links)
    print('Mails :', mails)
    print('Contact :',Contact)