given_string = "DBCABA"


def first_recurring(string):
    counts = {}
    for char in string:
        if char in counts:
            return char
        counts[char] = 1
    return None


print(first_recurring(given_string))
