x = open('message2.txt', 'w')
x.write("Jesus is the way, the truth and the life!")
x.close()

x = open('message2.txt', 'r')
y = x.read()
print(y)