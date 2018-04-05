from types import coroutine
from collections import deque
#Way of watching sockets
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

@coroutine
def read_wait(sock):
    yield 'read_wait', sock

@coroutine
def write_wait(sock):
    yield 'write_wait', sock

f = read_wait('somesocket')

f.send(None)

#('read_wait', 'somesocket')

class Loop:
    def __init__(self):
        self.ready = deque()
        self.selector = DefaultSelector()

    #receive on a socket in non-blocking mode
    async def sock_recv(self, sock, maxbytes):
    #wait for something to happen
        await read_wait(sock)
        return sock.recv(maxbytes)
    #to accept the connection
    async def sock_accept(self, sock):
        await read_wait(sock)
        return sock.accept()

    async def sock_sendall(self, sock, data):
    #while we have some data we're waiting for something to send it
        while data: 
            try:    
                nsent = sock.send(data)
                data = data[nsent:]
            except BlockingIOError:
                await write_wait(sock)
            
            

    def create_task(self, coro):
        self.ready.append(coro)

    def run_forever(self):
        while True:
        #if there is nothing ready to run go get all of the i/o of them
            while not self.ready:
                events = self.selector.select()
                for key, _ in events:
                    self.ready.append(key.data)
                    self.selector.unregister(key.fileobj)
            while self.ready:
                self.current_task = self.ready.popleft()
                try:
                    op, *args = self.current_task.send(None)  #Run to the yield
                    getattr(self, op)(*args)  #Sneaky method call
                except StopIteration:
                    pass
    #the current_task is interested on reading on that socket
    def read_wait(self, sock):
        self.selector.register(sock, EVENT_READ, self.current_task)
    #the current_task is interested on writing on that socket
    def write_wait(self, sock):
        self.selector.register(sock, EVENT_WRITE, self.current_task)