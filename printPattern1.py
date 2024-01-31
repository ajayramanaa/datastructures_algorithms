
def myFunction(n):
    iterations = n
    summary=0
    for i in range (1,n):
        if iterations-1 !=0:
            summary=summary + (i * (10 ** (n-1)))
            iterations = iterations -1

if __name__ == '__main__':
    n = int(input())
    print(myFunction)

