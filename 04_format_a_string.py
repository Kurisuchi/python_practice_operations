def main():
    first_number = 5
    second_number = 9

    result = calc_string(first_number, second_number)
    print(result)

def calc_string(first_number, second_number):
    sum = first_number + second_number
    return f'The sum of {first_number} and {second_number} is {sum}.'

if __name__ == '__main__':
    main()