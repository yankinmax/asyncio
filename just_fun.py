def countdown(n):  #simple generator
    while n > 0:
        yield n
        n -= 1

countdown(50)

for i in countdown(5):   #just for loop
    print(i)


from types import coroutine

@coroutine
def span():
    result = yield 'somevalue'
    print('The result is', result)

f = span()  #<generator object span at 0xb71d56bc>

f.send(None)

#'somevalue'

f.send(42)

#The result is 42

async def foo():
    print('Start foo')
    await span()
    print('End foo')

f = foo()  #<coroutine object foo at 0xb70c2b3c>

f.send(None)

#Start foo
#'somevalue'

f.send(42)

#The result is 42
#End foo

async def bar():
    print('Start bar')
    await foo()
    print('End bar')

f = bar()  #<coroutine object foo at 0xb70c2b3c>

f.send(None)

#Start bar
#Start foo
#'somevalue'

f.send(42)

#The result is 42
#End foo
#End bar

async def blah():
    yield 42

#SyntaxError