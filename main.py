file_name = 'Text.txt'
file = open(file_name, mode='r')
file_content = file.read()
file.close()
print(file_content)
