from string import ascii_lowercase

def main():
    str1 = "How quickly jumping zebras vex."
    str2 = "Sphinx of black quartz, judge my vow."

    result1 = check_string(str1)
    result2 = check_string(str2)

    print(f"{result1}\n{result2}")

def check_string(my_string):
    missed_letters = ""
    lowercase = set(my_string.lower())
    missing_letters = set(ascii_lowercase) - lowercase
    
    for i in sorted(missing_letters):
        missed_letters = missed_letters + i

    if set(ascii_lowercase).issubset(sorted(lowercase)):
        return "The string contains all the letters of the alphabet."
    else:
        return f"The string is missing the following letters: {missed_letters}"

if __name__ == '__main__':
    main()