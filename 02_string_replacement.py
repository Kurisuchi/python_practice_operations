def main():
    orig_string = "Greetings, everybody!"
    old_string = "everybody"
    new_string = "friends"
    result = replace_string(orig_string, old_string, new_string)

    print(orig_string)
    print(result)

def replace_string(orig_string, old_string, new_string):
    text = orig_string.replace(old_string, new_string)
    return text

if __name__ == '__main__':
    main()