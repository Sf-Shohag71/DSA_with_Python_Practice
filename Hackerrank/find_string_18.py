def find_string(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count

# def count_substring(string, sub_string):
    # return sum(1 for i in range(len(string)) if string.startswith(sub_string, i))


if __name__ == '__main__':
    string = "ABCDCDCABCDCDC"
    sub_string = "CDC"
    count = find_string(string, sub_string)
    print(count)