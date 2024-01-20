# file = open('check.txt')


# str = file.read()
# rev_str = reversed(str)
# file.write(rev_str)


# sub = "f\ng\n"

# print(str)
# #print(sub in str)





# file.close()

with open('check.txt','r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('check.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)