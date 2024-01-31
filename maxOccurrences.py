from collections import Counter

my_list = [1, 4,4,4,4,4,4,4,4,4,5,5, 1]

# Use Counter to count occurrences of each element in the list
element_counts = Counter(my_list)
print(element_counts)

# Use max function with key parameter to find the element with maximum occurrences
max_element = max(element_counts, key=element_counts.get)

# Print the result
print(f"The element with maximum occurrences is: {max_element}")

list.count(max(list))