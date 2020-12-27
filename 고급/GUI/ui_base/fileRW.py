import os


class FileRW:
    def __init__(self, path):
        self.path = path

    def mkDir(self):
        if os.path.isdir(self.path):
            os.mkdir(self.path)

    def listDir(self):
        return os.listdir(self.path)

    def read(self, fname):
        f = open(self.path + '/' + fname, 'r', encoding='utf-8')
        content = f.read()
        f.close()
        print(content)
        return content

    def write(self, fname, content):
        f = open(self.path + '/' + fname, 'w', encoding='utf-8')
        f.write(content)
        f.close()






