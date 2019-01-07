import os
import csv

class Data():
    def __init__(self, file_path = None):
        self.file_descriptor = None
        self.file_path = file_path
        self.data = None

    def open(self, file_path = None, mode = "r"):
        self.file_path = file_path if file_path is not None else self.file_path  
        self.file_descriptor = open(self.file_path, mode, newline='')
        return self

    def read_as_csv(self, delimiter = ',', skip_header = False):
        self.data = csv.reader(self.file_descriptor, delimiter=delimiter)
        if skip_header: 
            next(self.data)
        for row in self.data:
            yield row
