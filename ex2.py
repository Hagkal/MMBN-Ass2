import os

class Heap:

    def getColNum(self, firstLine, colName):
        """
        this method will return the number of the attribute wanted
        :param firstLine: the complete line
        :param colName: the attribute name
        :return: the number of the attribute. numbered by seperator: ','
        """
        firstLine = firstLine[:-1]
        att = firstLine.split(",")

        for i in range(0, len(att)):
            if att[i] == colName:
                return i

        return -1


    def __init__(self, file_name):
        """
        :param file_name: the name of the heap file to create. example: kiva_heap.txt
        """
        self.fileName = file_name
        try:
            wFile = open(file_name, "w+")
            wFile.close()
        except IOError:
            print"IO Error has occured"



    def create(self, source_file):
        """
        The function create heap file from source file.
        :param source_file: the name of file to create from. example: kiva.txt
        """
        try:
            heapFile = open(self.fileName, "a+")
            readFile = open(source_file, "r")
            currentLine = readFile.readline()

            while (currentLine != ""):
                heapFile.write(currentLine)
                currentLine = readFile.readline()

            heapFile.close()
            readFile.close()

        except IOError:
            print"IO Error has occured"


    def insert(self, line):
        """
        The function insert new line to heap file
        :param line: string reprsent new row, separated by comma. example: '653207,1500.0,USD,Agriculture'
        """
        try:
            wFile = open(self.fileName, "a+")
            wFile.write(line+"\n")
            wFile.close()
        except IOError:
            print "IO Error has occured"


    def delete(self, col_name, value):
        """
        The function delete records from the heap file where their value in col_name is value.
        Deletion done by mark # in the head of line.
        :param col_name: the name of the column. example: 'currency'
        :param value: example: 'PKR'
        """
        try:
            rFile = open(self.fileName, "r+")
            wFile = open(self.fileName + ".tmp", "w+")
            line = rFile.readline()
            colNum = self.getColNum(line, col_name)
            flag = False

            while line != "" and colNum != -1:
                flag = True
                list = line.split(",")
                if (list[colNum] != value):
                    wFile.write(line)
                line = rFile.readline()

            wFile.close()
            rFile.close()

            if flag:
                os.remove(rFile.name)
                os.rename(wFile.name, self.fileName)
            else:
                os.remove(wFile.name)

        except IOError:
            print"IO Error has occured"

    def update(self, col_name, old_value, new_value, ):
        """
        The function update records from the heap file where their value in col_name is old_value to new_value.
        :param col_name: the name of the column. example: 'currency'
        :param old_value: example: 'TZS'
        :param new_value: example: 'NIS'
        """
        try:
            rFile = open(self.fileName, "r")
            wFile = open(self.fileName + ".tmp", "w+")

            line = rFile.readline()
            colNum = self.getColNum(line, col_name)
            flag = False

            while line != "" and colNum != -1:
                flag = True
                list = line.split(",")
                if list[colNum] == old_value:
                    list[colNum] = new_value
                    line = ','.join(str(x) for x in list)

                wFile.write(line)
                line = rFile.readline()

            rFile.close()
            wFile.close()
            if flag:

                os.remove(self.fileName)
                os.rename(wFile.name, self.fileName)
            else:
                os.remove(wFile.name)

        except IOError:
            print "IO Error has occured"



# heap = Heap('heap.txt')
# heap.create('kiva.txt')
# heap.insert('653207,1500.0,USD,Agriculture')
# heap.update('currency','PKR','NIS')
# heap.delete('currency','NIS')

class SortedFile:

    def __init__(self, file_name, col_name):
        """
        :param file_name: the name of the sorted file to create. example: kiva_sorted.txt
        :param col_name: the name of the column to sort by. example: 'lid'
        """

    def create(self, source_file):
        """
        The function create sorted file from source file.
        :param source_file: the name of file to create from. example: kiva.txt
        """

    def insert(self, line):
        """
        The function insert new line to sorted file according to the value of col_name.
        :param line: string of row separated by comma. example: '653207,1500.0,USD,Agriculture'
        """

    def delete(self, value):
        """
        The function delete records from sorted file where their value in col_name is value.
        Deletion done by mark # in the head of line.
        :param value: example: 'PKR'
        """

    def update(self, old_value, new_value):
        """
        The function update records from the sorted file where their value in col_name is old_value to new_value.
        :param old_value: example: 'TZS'
        :param new_value: example: 'NIS'
        """


# sf = SortedFile('SortedFile.txt', 'currency')
# sf.create('kiva.txt')
# sf.insert('653207,2.0,USD,Agriculture')
# sf.delete('625.0')
# sf.update('150.0','12')

class Hash:
    def __init__(self, file_name, N=5):
        """
        :param file_name: the name of the hash file to create. example: kiva_hash.txt
        :param N: number of buckets/slots.
        """

    def create(self, source_file, col_name):
        """
        :param source_file: name of file to create from. example: kiva.txt
        :param col_name: the name of the column to index by example: 'lid'
        Every row will represent a bucket, every tuple <value|ptr> will separates by comma.
        Example for the first 20 instances in 'kiva.txt' and N=10:
        653060|11,
        653091|17,653051|1,
        653052|18,653062|14,653082|9,
        653063|4,653053|2,
        653054|16,653084|5,
        653075|15,
        653066|19,
        653067|7,
        653088|12,653048|10,653078|8,1080148|6,653068|3,
        653089|13,
        """

    def add(self, value, ptr):
        """
        The function insert <value|ptr> to hash table according to the result of the hash function on value.
        :param value: the value of col_name of the new instance.
        :param ptr: the row number of the new instance in the heap file.
        """


    def remove(self, value, ptr):
        """
        The function delete <value|ptr> from hash table.
        :param value: the value of col_name.
        :param ptr: the row number of the instance in the heap file.
        """


# heap = Heap("heap_for_hash.txt")
# hash = Hash('hash_file.txt', 10)

# heap.create('kiva.txt')
# hash.create('kiva.txt', 'lid')

# heap.insert('653207,1500.0,USD,Agriculture')
# hash.add('653207','11')
#teshane master master!!!
# test test test
#lalalala



test1 = Heap("Test1.txt")
test1.create("kiva_loans.txt")

test1.insert("666,6.66,HAG,Omri")
test1.update("currency", "HAG", "KAL")
test1.update("currency", "ss", "ss")
test1.delete("corrency", "KAL")