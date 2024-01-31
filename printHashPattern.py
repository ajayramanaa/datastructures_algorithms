def printHashPatter(symbol: str, num: int):
    for i in range (num+1):
        s = symbol * i
        #print(s.rjust(num))  # prints the pattern right left. it prefixes some empty spaces.
        print(s)


symbol = '#'
no_of_rows = 10
printHashPatter(symbol, no_of_rows)