import os, sys
s = ''
def convert12to24(strTime):
    if strTime[-2:] == 'PM' and strTime[2:] != '12':
        strTime = str (12 + int(strTime[:2])) + strTime[2:]
    elif strTime[-2:]=='AM' and strTime[:2]=='12':
        strTime = '00' + strTime[2:]
    return strTime[:-2]

inputStr = '00:37:00AM'

print(convert12to24(inputStr))