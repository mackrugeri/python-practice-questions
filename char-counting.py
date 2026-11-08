from collections import Counter

def char_counting(string):
    most_common = Counter(string)
    print(most_common)

    max_common_value = max(most_common.values())
    most_repeated_char = [
        (char, value) for char,value in most_common.items() if value == max_common_value
    ]
    print(most_repeated_char)

char_counting("programming")