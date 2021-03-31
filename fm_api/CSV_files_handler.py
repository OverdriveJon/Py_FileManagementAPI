import csv
import os.path


# Função principal que basicamente faz o script rodar

def addheadertofile():
    _filelist_row = []
    _filelist_header = []
    _filename = 'FM_API.csv'

    # Func que adiciona as strings no header
    # Adicionar no header é um processo diferente de colocar as outras colunas
    def addheader(num):
        for x in range(num):
            _row_header_name = str(input('Digite o header ' + str(x + 1) + '\n'))
            _filelist_header.append(_row_header_name)

    _rowlen = int(input('Quantas colunas o arquivo deve ter ? \n'))
    addheader(_rowlen)

    if os.path.exists(_filename):
        _file = open(_filename, mode='w', newline='')
    else:
        _file = open(_filename, mode='x', newline='')

    file_writer = csv.DictWriter(_file, fieldnames=_filelist_header, delimiter=',',
                                 quoting=csv.QUOTE_MINIMAL)

    file_writer.writeheader()

    def addrows():
        for y in range(len(_filelist_header)):
            _row_name = str(
                input('Digite a coluna numero ' + str(y + 1) + ' para a coluna de nome ' + _filelist_header[y] + '\n'))
            _filelist_row.append(_row_name)

    addrows()

    def writetofile():
        numberofrows = int(input('Quantas colunas deseja criar ?\n'))
        for c in range(numberofrows):
            _filedic = {}
            for m in range(len(_filelist_header)):
                _filedic[_filelist_header[m]] = _filelist_row[m]
            file_writer.writerow(_filedic)
    writetofile()
    _file.close()

# As string estao sendo escritas de maneira muito esquista no documento
# pelos menos elas estao sendo escritas LOL
# NAO MAIS XD
