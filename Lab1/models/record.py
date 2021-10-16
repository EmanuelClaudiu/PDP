from pickle import SHORT_BINUNICODE


class Record:
    
    def __init__(self, id, source, destination, source_before, destination_before, amount):
        self.serial_number = id
        self.source = source
        self.destination = destination
        self.source_before = source_before
        self.destination_before = destination_before
        self.amount = amount