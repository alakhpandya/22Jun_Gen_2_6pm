"""
f = open("C:\\Users\\Alakh Pandya\\Desktop\\Batches\\22Jun_Gen_2_6pm\\Python\\EMS\\concepts\\ourBatch.txt")

data = f.read()
print(data)
# print(type(data))

print(f.tell())

data = f.read(15)

# myList = []
# myList.append(data)
# print(myList)
data = f.read(20)
# print(data)
print(f.tell())

f.seek(50)
data = f.read()
print(data)

line = f.readline()
print(line)
print(f.readline())

data = f.readlines()
print(data)

# f.write("Hello")
print(f.writable())
print(f.readable())

f.close()
"""

# file handling syntax:
"""
name_of_file_pointer = open("file name with extension and full path", "Mode1Mode2")

Mode1   Name        Description                                     Mode2   Name
r       Read        Opens the file for reading only                 t       text        default

w       Write       Opens the file for writing only                 b       binary

a       append

x     Exclusively
        Create

r+      read+

w+      write+

a+      append+
"""