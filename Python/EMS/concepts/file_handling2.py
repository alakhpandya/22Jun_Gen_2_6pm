# f = open('yourBatch.txt', 'wt')

# f.write("1\tAkash\t\tVisiting Student\n")

# f.close()

# f = open('myBatch.txt', 'r')

# f.close()

"""
f = open("ourBatch.txt", "rt")
data = f.readlines()
f.close()

# print(data)
print("Enter following details:")
sr_no = input("Sr no: ")
name = input("Name: ")
role = input("Role: ")
data.append(sr_no + "\t" + name + "\t\t" + role + "\n")

# print(data)
f = open("ourBatch.txt", "w")
f.writelines(data)
f.close()
"""
"""
f = open("ourBatch.txt", "a")
f.write("15\tVansh\t\tOffline Student\n")
f.close()
"""

# f = open("myBatch.txt", "x")
# f.write("15\tVansh\t\tOffline Student\n")
# f.close()

# f = open("myBatch.txt", "r+")
# f.read()
# f.write("Akash Enters...")
# f.close()

# coma separeted values: CSV

f = open("ourBatch.csv", "r")
data = f.readlines()
f.close()

"""
Details of roll no-5:
Name: Khush
Role: Anotator
"""
sr = int(input("Enter sr no: "))
sr_no, name, role = data[sr].split(",")
print(f"Details of roll no-{sr}:")
print("Name:", name)
print("Role:", role)