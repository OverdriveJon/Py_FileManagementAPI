import csv
import os.path

_filelist = []
_filelist_header = []
_filename = 'FM_API.csv'


def addtolist_normal(*args):
    _filelist.append(args)
    pass


def addtolist_header(*args):
    _filelist_header.append(str(args))
    pass


def addheader(num):
    for x in range(num):
        _row_header_name = str(input('Digite o header ' + str(x+1) + '\n'))
        addtolist_header(_row_header_name)


_rowlen = int(input('Quantas colunas o arquivo deve ter ? \n'))
addheader(_rowlen)

if os.path.exists(_filename):
    candidate_file = open(_filename, mode='w', newline='')
else:
    candidate_file = open(_filename, mode='x', newline='')

candidate_writer = csv.DictWriter(candidate_file, fieldnames=_filelist_header, delimiter=',', quoting=csv.QUOTE_MINIMAL)

candidate_writer.writeheader()

