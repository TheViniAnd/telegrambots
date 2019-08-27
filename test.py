

class Test():
    def one(self):
        x = '5'
        print(x)
    def two(self):
        x = '1'
        print(x)

test = Test()

v = input()

if v == '1':
    test.two()
elif v == '5':
    test.one()