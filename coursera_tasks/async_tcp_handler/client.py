from collections import defaultdict
import socket
import time


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.buffer_size = 1024
        

    def put(self, metric_name, metric_value, timestamp=None):
        if not timestamp:
            timestamp = str(int(time.time()))
        else:
            timestamp = str(timestamp)
        timestamp += '\n'
        metric_value = str(metric_value)
        message = ' '.join(['put', metric_name, metric_value, timestamp])
        with socket.create_connection((self.host, self.port), self.timeout) as sock:         
            #sock.settimeout(self.timeout)
            sock.sendall(message.encode("utf8"))
            data = sock.recv(self.buffer_size).decode()

        if data == 'error\nwrong command\n\n':
            raise ClientError()


    def get(self, metric_name):
        self.metric_name = metric_name        
        with socket.create_connection((self.host, self.port), self.timeout) as sock:         
            #sock.settimeout(self.timeout)
            key = 'get {}\n'.format(self.metric_name)            
            sock.sendall(key.encode("utf8"))
            data = sock.recv(self.buffer_size).decode()
            if data == "ok\n\n":
                return {} 
            elif data == 'error\nwrong command\n\n':
                raise ClientError()

            metric_items = data.lstrip('ok\n').rstrip('\n\n')   #removes from left and right sides unneccessary symbols
            metric_items = [x.split() for x in metric_items.split('\n')]
            metric_dict = defaultdict(list)
            for key, metric, timestamp in metric_items:
                metric_dict[key].append((int(timestamp), float(metric)))

            return dict(metric_dict)
            

if __name__ == '__main__':
    #client = Client("127.0.0.1", 8888, timeout=15)
    client = Client("127.0.0.1", 8181, timeout=15)    

    client.put("palm.cpu", 0.5, timestamp=1150864247)
    client.put("palm.cpu", 2.0, timestamp=1150864248)
    client.put("palm.cpu", 0.5, timestamp=1150864248)

    client.put("eardrum.cpu", 3, timestamp=1150864250)
    client.put("eardrum.cpu", 4, timestamp=1150864251)
    client.put("eardrum.memory", 4200000)

    print(client.get("*"))
    print(client.get("non_existing_key"))