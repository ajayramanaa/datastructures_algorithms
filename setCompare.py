# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_subset(test_case):
    _, set_a = test_case[:2]
    _, set_b = test_case[2:]

    return set_a.issubset(set_b)

if __name__ == "__main__":
    # Number of test cases
    t = int(input())

    for _ in range(t):
        # Number of elements in set A
        n_a = int(input())

        # Elements of set A
        set_a = set(map(int, input().split()))

        # Number of elements in set B
        n_b = int(input())

        # Elements of set B
        set_b = set(map(int, input().split()))

        # Check if set A is a subset of set B and print the result
        result = is_subset((n_a, set_a, n_b, set_b))
        print(result)