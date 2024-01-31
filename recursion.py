# How to find factorial of a number

""" def factorial(n):
    # the below statement helps to stop the program when negative number was given as input
    assert n>=0 and int(n) == n, 'The number must be a positive integer'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(4)) """

# How to find a fibonacci number

""" def fibonacci(n):
    assert n >=0 and int(n) == n, "The input number must be a positive integer"
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(20)) """

# Find of sum of digits of a number

""" def sumofdigits(n):
    assert n>=0 and int(n) == n, "Number should be positive integer number"
    if n == 0:
        return 0
    else:
        return int(n%10) + sumofdigits(int(n/10))

print(sumofdigits(15)) """

# Find the power of a number

"""def powerofnumber(base, exp):
    assert exp>=0 and int(exp) == exp, "Exponential value should be a positive integer"
    if exp == 0:
        return 1
    if exp == 1:
        return base 
    else:
        return base * powerofnumber(base, exp-1)

print(powerofnumber(2,25)) """

# find greatest common divisor of two numbers

""" def gcd(a,b):
    assert int(a) == a and int(b) == b, " Numbers must be integers"
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a%b) 

print(gcd(16,40)) """

# decimal number to Binary conversion using recursion

""" def decimaltobinary(n):
    assert int(n) == n, "The number must be an integer number"
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimaltobinary(int(n/2))

print(decimaltobinary(24)) """

# capitalizeWords Solution

""" def capitalizeWords(arr):
    result = []
    print(result)
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalizeWords(arr[1:])

words = ['i', 'am', 'learning', 'recursion']
print(capitalizeWords(words)) # ['I', 'AM', 'LEARNING', 'RECURSION'] """

# capitalizeFirst Solution

""" def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:]) 


print(capitalizeFirst(['car', 'taco', 'banana'])) # ['Car','Taco','Banana'] """

# collectStrings Solution

""" def collectStrings(obj):
    resultArr = []
    for key in obj:
        if type(obj[key]) is str:
            resultArr.append(obj[key])
            print(resultArr)
        if type(obj[key]) is dict:
            resultArr = resultArr + collectStrings(obj[key])
            print(resultArr)
    return resultArr



obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}

print(collectStrings(obj)) # ['foo', 'bar', 'baz']) """

# Factorial Solution

""" def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)


print(factorial(1)) # 1
print(factorial(2)) # 2
print(factorial(4)) # 24
print(factorial(7)) # 5040 """

# fib Solution

""" def fib(num):
    if (num < 2):
        return num
    return fib(num - 1) + fib(num - 2)


print(fib(4)) # 3
print(fib(10)) # 55
print(fib(28)) # 317811
print(fib(35)) # 9227465 """

# flatten Solution
""" def flatten(arr):
    resultArr = []
    for custItem in arr:
        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
            #The extend() method adds the specified list elements (or any iterable) to the end of the current list.
        else: 
            resultArr.append(custItem)
    return resultArr

print(flatten([1, 2, 3, [4, 5]])) # [1, 2, 3, 4, 5]
print(flatten([1, [2, [3, 4], [[5]]]])) # [1, 2, 3, 4, 5]
print(flatten([[1], [2], [3]])) # [1, 2, 3]
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])) # [1, 2, 3] """

# isPalindrome Solution


""" def isPalindrome(strng):
    if len(strng) == 0:
        return True
    if strng[0] != strng[len(strng)-1]:
        return False
    print(strng[1:-1])
    return isPalindrome(strng[1:-1])

print(isPalindrome('awesome')) # false
print(isPalindrome('foobar')) # false
print(isPalindrome('tacocat')) # true
print(isPalindrome('amanaplanacanalpanama')) # true
print(isPalindrome('amanaplanacanalpandemonium')) # false """

# nestedEvenSum Solution

""" def nestedEvenSum(obj, sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nestedEvenSum(obj[key])
        elif type(obj[key]) is int and obj[key]%2==0:
            sum+=obj[key]
    return sum



obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

print(nestedEvenSum(obj1)) # 6
print(nestedEvenSum(obj2)) # 10 """

# Power Solution


""" def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)

print(power(2,0)) # 1
print(power(2,2)) # 4
print(power(2,4)) # 16 """

# productOfArray Solution

""" def productOfArray(arr):
    if len(arr) == 0:
        return 1
    print(arr[1:])
    return arr[0] * productOfArray(arr[1:])

print(productOfArray([1,2,3])) #6
print(productOfArray([1,2,3,10])) #60 """

# recursiveRange Solution

""" def recursiveRange(num):
    if num <= 0:
        return 0
    return num + recursiveRange(num - 1)


print(recursiveRange(6)) """

# reverse Solution

""" def reverse(strng):
    if len(strng) <= 1:
      return strng
    print(strng[len(strng)-1])
    return strng[len(strng)-1] + reverse(strng[0:len(strng)-1])


print(reverse('python')) # 'nohtyp'
print(reverse('appmillers')) # 'srellimppa' """

# someRecursive Solution

""" def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True

def isOdd(num):
    if num%2==0:
        return False
    else:
        return True

print(someRecursive([1,2,3,4], isOdd)) # true
print(someRecursive([4,6,8,9], isOdd)) # true
print(someRecursive([4,6,8], isOdd)) # false """

# stringifyNumbers Solution

""" def stringifyNumbers(obj):
    newObj = obj
    for key in newObj:
        if type(newObj[key]) is int:
            newObj[key] = str(newObj[key])
        if type(newObj[key]) is dict:
            newObj[key] = stringifyNumbers(newObj[key])
    return newObj



obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

print(stringifyNumbers(obj))

{'num': '1', 
 'test': [], 
 'data': {'val': '4', 
          'info': {'isRight': True, 'random': '66'}
          }
} """

