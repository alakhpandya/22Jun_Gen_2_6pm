# f = open("ourBatch.csv", "r+")
# f.close()

with open("ourBatch.csv", "r+") as f:       # same as f = open("ourBatch.csv", "a+")
    print(f.readline())
    print(f.readline())
# print(f.closed)

# Next class: with block mechanism through ContextManager