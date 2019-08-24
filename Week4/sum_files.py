import os
import tempfile


class File:

    def __init__(self, filepath):
        self.filepath = filepath

    def write(self, text):
        with open(self.filepath, 'w') as f:
            f.write(text)

    def __add__(self, other):
        with open(self.filepath, 'r') as f1, open(other.filepath, 'r') as f2:
            storage_path = os.path.join(tempfile.gettempdir(), "union.txt")
            data1 = f1.read()
            data2 = f2.read()
            with open(storage_path, 'w') as nf:
                nf.write(data1 + data2)
            return File(storage_path)

    def __str__(self):
        return self.filepath

    def __iter__(self):
        self.filepointer = open(self.filepath, 'r')
        return self

    def __next__(self):
        line = self.filepointer.readline()
        if line:
            return line
        else:
            raise StopIteration


file1 = File("/tmp/file1.txt")
file2 = File("/tmp/file2.txt")
# file2.write("reporting!")

file3 = file1 + file2
count = 0
for line in File("/tmp/union.txt"):
    count += 1
    print(line)
