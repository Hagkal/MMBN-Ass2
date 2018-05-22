import os
import time

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
        self.lineLength = 0
        try:
            wFile = open(file_name, "w+")
            wFile.close()
        except IOError:
            print "IO Error has occured"



    def create(self, source_file):
        """
        The function create heap file from source file.
        :param source_file: the name of file to create from. example: kiva.txt
        """
        try:
            heapFile = open(self.fileName, "a+")
            readFile = open(source_file, "r")

            currentLine = readFile.readline()
            heapFile.write(currentLine)

            currentLine = readFile.readline()
            self.lineLength = len(currentLine)

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
            iFirstLine = len(line)
            iTotLines = -1
            colNum = self.getColNum(line, col_name)
            flag = True

            while line != "" and colNum != -1:
                list = line.split(",")
                if (list[colNum] == value):
                    line = "#" + line[1:]
                wFile.write(line)
                line = rFile.readline()
                iTotLines += 1
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
        self.fileName = file_name
        self.numBuckets = N
        self.title = ""
        self.sortCol = ""
        try:
            open(file_name, "w+").close()
        except IOError:
            print "can't open file"


    def hashFunc(self, value):
        """
        our hash function
        :param value: the given value
        :return: the currect bucket
        """
        try:
            i = int(value)
            return (i % self.numBuckets) + 1
        except ValueError:
            try:
                f = float(value)
                return int(f%self.numBuckets) + 1
            except ValueError:
                return (ord(value[0])%self.numBuckets)+1


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
        try:

            targetFile = open(self.fileName, "w+")
            for j in range(self.numBuckets - 1):
                targetFile.write("\n")
            targetFile.close()
            sourceFile = open(source_file, "r")

            line = sourceFile.readline()
            colNum = self.getColNum(line, col_name)
            self.title = line
            self.sortCol = col_name
            lineCount = 0
            line = sourceFile.readline()

            while line != "" and colNum != -1:
                list = line.split(",")
                idx = self.hashFunc(list[colNum])
                lineCount += 1

                if idx == self.numBuckets: # last line case
                    targetFile = open(self.fileName, "a+")
                    targetFile.write(list[colNum] + "|" + str(lineCount) + ",")
                    targetFile.close()

                else: # not last line case. need to copy everything
                    targetFile = open(self.fileName, "r")
                    newTargetFile = open("tmp", "w+")
                    for i in range(idx - 1):
                        newTargetFile.write(targetFile.readline())

                    tmpLine = targetFile.readline()
                    tmpLine = tmpLine[:-1] + list[colNum] + "|" + str(lineCount) + ",\n"
                    newTargetFile.write(tmpLine)
                    tmpLine = targetFile.readline()

                    while tmpLine != "":
                        newTargetFile.write(tmpLine)
                        tmpLine = targetFile.readline()

                    targetFile.close()
                    newTargetFile.close()
                    os.remove(targetFile.name)
                    os.rename(newTargetFile.name, self.fileName)

                line = sourceFile.readline()

            sourceFile.close()
        except IOError:
            print "can't open file"

    def add(self, value, ptr):
        """
        The function insert <value|ptr> to hash table according to the result of the hash function on value.
        :param value: the value of col_name of the new instance.
        :param ptr: the row number of the new instance in the heap file.
        """
        try:
            oldFile = open(self.fileName, "r")
            newFile = open("tmp", "w+")

            idx = self.hashFunc(value)
            for i in range(idx-1):
                newFile.write(oldFile.readline())

            newFile.write(oldFile.readline()[:-1] + str(value) + "|" + str(ptr) + ",\n")

            for line in oldFile:
                newFile.write(line)

            oldFile.close()
            newFile.close()
            os.remove(oldFile.name)
            os.rename(newFile.name, self.fileName)

        except IOError:
            print("can't open file")


    def remove(self, value, ptr):
        """
        The function delete <value|ptr> from hash table.
        :param value: the value of col_name.
        :param ptr: the row number of the instance in the heap file.
        """
        try:
            oldFile = open(self.fileName, "r")
            newFile = open("tmp", "w+")

            idx = self.hashFunc(value)
            for i in range(idx-1):
                newFile.write(oldFile.readline())

            line = oldFile.readline()
            list = line.split(",")
            line = ""
            for item in list:
                list2 = item.split("|")
                if ((list2[0] != value or list2[1] != ptr) and list2[0] != "\n"):
                    line += str(item) + ","
            line += "\n"

            newFile.write(line)

            for l in oldFile:
                newFile.write(l)

            oldFile.close()
            newFile.close()
            os.remove(oldFile.name)
            os.rename(newFile.name, self.fileName)

        except IOError:
            print "can't open file"

# heap = Heap("heap_for_hash.txt")
# hash = Hash('hash_file.txt', 10)

# heap.create('kiva.txt')
# hash.create('kiva.txt', 'lid')

# heap.insert('653207,1500.0,USD,Agriculture')
# hash.add('653207','11')
#teshane master master!!!
# test test test
#lalalala


"""
test1 = Hash("Test1.txt", 10)
test1.create("fixed_kiva_loans1.txt", "lid")
test1.add("653082", "9")
test1.remove("653082", "9")

test1.insert("666,6.66,HAG,Omri")
test1.update("currency", "HAG", "KAL")
test1.update("currency", "ss", "ss")
test1.delete("currency", "PKR")
"""

def creationTest():
    """
    function that will print the time of creation for all 4 types of files
    :return:
    """
    heap = Heap("heapTest.txt")
    start = time.time()
    heap.create("fixed_kiva_loans1.txt")
    end = time.time()
    print "Heap creation time: " + str(end - start)

    sorted = SortedFile("sortedFile.txt", "sector")
    start = time.time()
    sorted.create("fixed_kiva_loans1.txt")
    end = time.time()
    print "Sorted file creation time: " + str(end - start)

    hash10 = Hash("Hash10.txt", 10)
    start = time.time()
    hash10.create("fixed_kiva_loans1.txt", "lid")
    end = time.time()
    print "Hash with N=10 creation time: " + str(end-start)

    hash100 = Hash("Hash100.txt", 100)
    start = time.time()
    hash100.create("fixed_kiva_loans1.txt", "lid")
    end = time.time()
    print "Hash with N=100 creation time: " + str(end - start)

    hash1000 = Hash("Hash1000.txt", 1000)
    start = time.time()
    hash1000.create("fixed_kiva_loans1.txt", "lid")
    end = time.time()
    print "Hash with N=1000 creation time: " + str(end - start)

    ############################ TEST 2
    rFile = open("Test2.txt", "r")
    total = 0

    start = time.time()
    for l in rFile:
        heap.insert(l)
    end = time.time()
    print "Heap adding 50 records time: " + str(end-start)
    rFile.seek(0)

    start=time.time()
    for k in rFile:
        sorted.insert(k)
    end = time.time()
    print "Sorted file adding 50 records time: " + str(end-start)
    rFile.seek(0)

    start = time.time()
    for j in rFile:
        list = j.split(",")
        hash10.add(list[0], "6")
    end = time.time()
    print "Hash with N=10 adding 50 records time: " + str(end-start)
    rFile.seek(0)

    start = time.time()
    for h in rFile:
        list = h.split(",")
        hash100.add(list[0], "6")
    end = time.time()
    print "Hash with N=100 adding 50 records time: " + str(end-start)
    rFile.seek(0)

    start=time.time()
    for g in rFile:
        list = g.split(",")
        hash1000.add(list[0], "6")
    end = time.time()
    print "Hash with N=1000 adding 50 records time: " + str(end-start)
    rFile.seek(0)

    ################# TEST 3
    originalFile = open("fixed_kiva_loans1.txt", "r")
    line = originalFile.readline()
    total = 0
    for i in range(50):
        line = originalFile.readline()
        list = line.split(",")
        start = time.time()
        heap.update("lid", list[0], "111222")
        end = time.time()
        total += (end-start)
    print "Heap updating 50 records time: " + str(total)
    originalFile.seek(0)

    line = originalFile.readline()
    total = 0
    for i in range(50):
        line = originalFile.readline()
        list = line.split(",")
        start = time.time()
        heap.update("sector", list[3], "OMRI")
        end = time.time()
        total += (end - start)
    print "Heap updating 50 records time: " + str(total)

    ################## TEST 4
    total = 0

    for l in rFile:
        list = l.split(",")
        start = time.time()
        heap.delete("lid", list[0])
        end = time.time()
        total += (end-start)
    print "Heap deleting 50 records time: " + str(total)

    rFile.seek(0)
    total = 0
    for l in rFile:
        list = l.split(",")
        start = time.time()
        sorted.delete(list[3])
        end = time.time()
        total += (end-start)
    print "Sorted file deleting 50 records time: " + str(total)

    rFile.seek(0)
    total = 0
    for l in rFile:
        list = l.split(",")
        start = time.time()
        hash10.remove(list[0], "6")
        end = time.time()
        total += (end - start)
    print "Hash with N=10 deleting 50 records time: " + str(total)

    rFile.seek(0)
    total = 0
    for l in rFile:
        list = l.split(",")
        start = time.time()
        hash100.remove(list[0], "6")
        end = time.time()
        total += (end - start)
    print "Hash with N=100 deleting 50 records time: " + str(total)

    rFile.seek(0)
    total = 0
    for l in rFile:
        list = l.split(",")
        start = time.time()
        hash1000.remove(list[0], "6")
        end = time.time()
        total += (end - start)
    print "Hash with N=1000 deleting 50 records time: " + str(total)


