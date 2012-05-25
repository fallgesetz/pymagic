import StringIO
import csv
import inspect
import os
# TODO: faster string search
# TODO: detecting binary is easy, detecting ASCII is hard
import binascii

def cur_file_dir():
    return os.path.dirname(inspect.getfile(inspect.currentframe()))

class Magician(object):
    def __init__(self,signatures_file=None):
        if not signatures_file:
            signatures_file = os.path.join(cur_file_dir(), 'signatures_GCK.txt')
        self.file_mapping = {}
        with open(signatures_file, "r") as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                processed_header = "".join(row[1].split()).lower() # get rid
                # of
                # spaces
                self.file_mapping[processed_header] = row[0]
        self.signatures = self.file_mapping.keys()
        self.max_read = max((len(signature) for signature in self.signatures)
        ) * 2

    def identify(self, file_obj):
        # note to self -- prefer file_obj over filename,
        # because file_obj has a flexible interface. For example,
        # even strings can be wrapped up in StringIO.StringIO
        header_data = file_obj.read(self.max_read)
        hexified_header_data = binascii.hexlify(header_data)
        for signature in self.signatures:
            if hexified_header_data.startswith(signature):
                return self.file_mapping[signature]
        raise Exception("can't find file. Could it be a text file?")


def identify_file(filename):
    """
    Convenience function that takes in a filename
    """
    mage = Magician()
    with open(filename, 'rb') as f:
        return mage.identify(f)

def identify_str(string):
    """
    Convenience function that takes in a string buffer
    """
    f = StringIO.StringIO(string)
    mage = Magician()
    return mage.identify(f)







