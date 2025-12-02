def file_error():
    try:
        f = open('tests.txt')
    except FileNotFoundError as e:
        print(e)
    else:
        print(f.read()) # prints contents
        f.close()
    finally:
        print("Executed successful....")
file_error()