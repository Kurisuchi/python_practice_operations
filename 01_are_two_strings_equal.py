def check_strings(first_string, second_string):
    return first_string == second_string

def main():
    str1 = "Orange"
    str2 = "Apple"
    str3 = "Apple"
    result1 = check_strings(str1, str2)
    result2 = check_strings(str2, str3)

    print(f"Are the two strings equal? {result1}")
    print(f"Are the two strings equal? {result2}")

if __name__ == '__main__':
    main()