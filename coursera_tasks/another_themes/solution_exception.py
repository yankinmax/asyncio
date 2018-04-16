import sys

class FileReader:

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        try:            
            with open(self.filename) as f:
                print('Content: {}'.format(f.read()))            
        except IOError:
            print("File {} does not exist".format(self.filename))        


def _main():    
    reader = FileReader("example1.txt")
    reader.read()


if __name__ == '__main__':
    _main()