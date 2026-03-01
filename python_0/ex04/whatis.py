import sys

def whatis(object: any) -> None:
    if len(object) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(object) == 1:
        return

    try:
        number = int(object[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == '__main__':
    try:    
        whatis(sys.argv)
    except AssertionError as e:
        print(f"AssertionError: {e}")