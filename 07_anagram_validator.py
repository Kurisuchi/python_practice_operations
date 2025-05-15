def main():
    str1 = "Eleven plus two?"
    str2 = "One plus twelve!"
    str3 = "A cinnamon roll?"
    str4 = "No canola oil, Mr.!"
    result1 = is_anagram(str1, str2)
    result2 = is_anagram(str3, str4)

    print(f"Is {str1} an anagram of {str2}? {result1}")
    print(f"Is {str3} an anagram of {str4}? {result2}")

def is_anagram(first_string, second_string):
    first = "".join(char for char in first_string.lower() if char.isalpha())
    second = "".join(char for char in second_string.lower() if char.isalpha())
    
    return sorted(first) == sorted(second)

if __name__ == '__main__':
    main()