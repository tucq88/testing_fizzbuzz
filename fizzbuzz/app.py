def run(args):
    if args == 0:
        return args

    result = args
    if args % (3*5) == 0:
        result = 'FizzBuzz'
    elif args % 3 == 0:
        result = 'Fizz'
    elif args % 5 == 0:
        result = 'Buzz'
    return result
