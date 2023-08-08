# f = open('yourBatch.txt', 'wt')

# f.write("1\tAkash\t\tVisiting Student\n")

# f.close()

# f = open('myBatch.txt', 'r')

# f.close()

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