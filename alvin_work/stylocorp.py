import os
from ordered_set import OrderedSet
class Corpus:
    def __init__(self, path, sep):
        self.path = path
        self.files = os.listdir(path)
        self.prints = [Print(os.path.join(path,f), sep) for f in self.files]
        self.sep = sep
        self.authors = OrderedSet([s.split(sep)[0] for s in self.files])

    def get_authors_prints(self, author):
        return [p for p in self.prints if p.author == author]
    
    def list_authors(self):
        return list(self.authors)
    

class Print:
    def __init__(self, path, sep):
        self.path = path
        self.sep = sep
        self.author = path.split(sep)[0]
        self.title = path.split(sep)[1]
        self.text = open(path).read()