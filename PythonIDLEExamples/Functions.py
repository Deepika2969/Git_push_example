#Function#

print("hello")
a = len('Hello')
print(a)
print('lenght of Hello is' + str(len('hello')))
print('Tell your name')
name = input()
print(f'your name is {name} Gowda')


def Hello_Func():
    pass

print(Hello_Func())
#output:None
print(Hello_Func)
#output:<function Hello_Func at 0x0271DD18>

def Hi_Func():
    print('Hi!!! Every body')
Hi_Func()
Hi_Func()
Hi_Func()


a = "Deepika"
print(a.upper())

#There are many inbuilt functions

def Para_Func(greeting):
    """this returns the formatted string with the name"""
    print('{},Function!!!'.format(greeting))

Para_Func('Hi')

print('Deepika','Ffree' , 'ahdhsh',sep='abc')
print('Ji')

