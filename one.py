#one.py

## indent zero gets run when one.py is called


def func1():
    print('func1() in one.py says hello \n')

print("TOP level in  ONE.PY\n")

def func2():
    pass

## built in name variable:

if __name__ == '__main__':
    print('ONE.PY is being run directly!!!!\n')
    
## mostly used for code organization
    func1()
    func2()

else:
    print('ONE.PY has been IMPORTED\n')