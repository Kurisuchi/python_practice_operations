def main():
    my_string = "That lemon pie is not for sale."
    result = reverse_string(my_string)

    print(f"Original string: {my_string}\nReversed string: {result}")

def reverse_string(my_string):
    return my_string[::-1]

if __name__ == '__main__':
    main()