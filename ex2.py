import os

class Heap:
    """
     this function will return the number of the given column
    """

    def getColNum(self, firstLine, colName):
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
        wFile = open(file_name, "w+")
        wFile.close()


    def create(self, source_file):
        """
        The function create heap file from source file.
        :param source_file: the name of file to create from. example: kiva.txt
        """

        heapFile = open(self.fileName, "a+")
        readFile = open(source_file, "r")
        currentLine = readFile.readline()

        while (currentLine != ""):
            heapFile.write(currentLine)
            currentLine = readFile.readline()

        heapFile.close()
        readFile.close()


    def insert(self, line):
        """
        The function insert new line to heap file
        :param line: string reprsent new row, separated by comma. example: '653207,1500.0,USD,Agriculture'
        """

        wFile = open(self.fileName, "a+")
        wFile.write(line+"\n")
        wFile.close()


    def delete(self, col_name, value):
        """
        The function delete records from the heap file where their value in col_name is value.
        Deletion done by mark # in the head of line.
        :param col_name: the name of the column. example: 'currency'
        :param value: example: 'PKR'
        """

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


    def update(self, col_name, old_value, new_value, ):
        """
        The function update records from the heap file where their value in col_name is old_value to new_value.
        :param col_name: the name of the column. example: 'currency'
        :param old_value: example: 'TZS'
        :param new_value: example: 'NIS'
        """

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

        self.filename = file_name
        self.colname = col_name
        self.title=""
        wFile = open(file_name, "w+")
        wFile.close()


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

    def __copyFunc(self, copyFrom, copyTo):

        #rFile = open (copyFrom, "r+")
        #wFile = open (copyTo, 'w+')
        copyTo.seek(0)
        copyFrom.seek(0)
        line = copyFrom.readline()

        while line != "":
            copyTo.write(line)
            copyTo.flush()
            line = copyFrom.readline()


    def create(self, source_file):
        """
        The function create sorted file from source file.
        :param source_file: the name of file to create from. example: kiva.txt
        """

        rFile = open(source_file, "r")
        wFile1 = open(self.filename, "w+")
        wFile2 = open(self.filename + "2" + ".tmp", "w+")

        firstLine = rFile.readline()
        self.title= firstLine
        colNum = self.getColNum(firstLine, self.colname)

        lineString = rFile.readline()
        lineLength = len(lineString)*(-1) - 1
        lineList = lineString.split(',')
        wFile1.write(lineString)
        lineString = rFile.readline()
        lineList = lineString.split(',')

        i=0
        while lineString != "" and i < 500:
            value = lineList[colNum]
            wFile1.seek(lineLength , 2)
            linetemp1String = wFile1.readline()
            linetemp1List = linetemp1String.split(',')
            flag = False
            valuetemp1 = linetemp1List[colNum]

            if value >= valuetemp1:
                wFile1.seek(0, 2)
                wFile1.write(lineString)

            else:
                wFile1.seek(0)
                wFile2.seek(0)
                linetemp1String = wFile1.readline()
                linetemp1List = linetemp1String.split(',')
                while linetemp1String != "":
                    valuetemp1 = linetemp1List[colNum]
                    if value > valuetemp1 and flag == False:
                        wFile2.write(linetemp1String)
                        wFile2.flush()

                    elif value <= valuetemp1 and flag == False:
                        wFile2.write(lineString)
                        wFile2.flush()
                        flag = True

                    if flag == True:
                        wFile2.write(linetemp1String)
                        wFile2.flush()

                    linetemp1String = wFile1.readline()
                    linetemp1List = linetemp1String.split(',')

                self.__copyFunc(wFile2, wFile1)
                wFile1.seek(lineLength, 2)
                wFile2.close()
                wFile2 = open(wFile2.name, "w+")

            lineString = rFile.readline()
            lineList = lineString.split(',')
            i+=1



    def insert(self, line):
        """
        The function insert new line to sorted file according to the value of col_name.
        :param line: string of row separated by comma. example: '653207,1500.0,USD,Agriculture'
        """

        rFile = open (self.filename, 'r')
        colNum = self.getColNum(self.title, self.colname)
        wFile = open(self.filename + "1" + ".tmp", "w+")

        lineString = rFile.readline()
        lineList = lineString.split(',')
        parameterLineList = line.split(',') # line given in a list format
        flag = False

        while lineString != "":
            if lineList[colNum] < parameterLineList[colNum] and flag == False:
                wFile.write(lineString)
                lineString = rFile.readline()
                lineList = lineString.split(',')

            elif flag:
                wFile.write(lineString)
                lineString = rFile.readline()

            else:
                wFile.write(line)
                flag = True
        wFile.close()
        rFile.close()
        os.rename(rFile.name, "tempo")
        os.rename(wFile.name, self.filename)


    def delete(self, value):
        """
        The function delete records from sorted file where their value in col_name is value.
        Deletion done by mark # in the head of line.
        :param value: example: 'PKR'
        """

        rFile = open(self.filename, 'r')
        firstLine = rFile.readline()
        colNum = self.getColNum(firstLine, self.colname)
        wFile = open(self.filename + "1" + ".tmp", "w+")

        # copying first line
        wFile.write(firstLine)

        lineString = rFile.readline()
        lineList = lineString.split(',')

        while lineString != "":
            if lineList[colNum] == value:
                lineString = rFile.readline()
                lineList = lineString.split(',')

            else:
                wFile.write(lineString)
                lineString = rFile.readline()
                lineList = lineString.split(',')

        os.rename(wFile, self.filename)


    def update(self, old_value, new_value):
        """
        The function update records from the sorted file where their value in col_name is old_value to new_value.
        :param old_value: example: 'TZS'
        :param new_value: example: 'NIS'
        """
        rFile = open(self.filename, 'r')
        firstLine = rFile.readline()
        colNum = self.getColNum(firstLine, self.colname)
        wFile = open(self.filename + "1" + ".tmp", "w+")

        # copying first line
        wFile.write(firstLine)

        lineString = rFile.readline()
        lineList = lineString.split(',')
        flag = False

        while lineString != "":
            for i in range(0, len(lineList)):
                if lineList[i] == old_value and flag == False:
                    lineList[i] = new_value
                    lineString = lineList
                    wFile.write(lineString)
                    flag = True
                    lineString = rFile.readline()
                    lineList = lineString.split(',')

            if flag == False:
                wFile.write(lineString)
                lineString = rFile.readline()
                lineList = lineString.split(',')

            flag = False

        os.rename(wFile, self.filename)

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
        self.filename = file_name
        self.numOfBuckets = N
        wFile = open(file_name, "w+")
        wFile.close()

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



test1 = SortedFile("Test1.txt1.tmp", "sector")
test1.create("fixed_kiva_loans.txt")
test1.insert("667343,999.0,PHP,Agri")