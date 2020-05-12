# open file modes
# r = read-only       rb = read binary
# r+ = read / write   rb+ = read / write binary
# w = write only      wb = write only binary

# open file in read mode
file_ptr = open("file.txt", "r")
print(file_ptr)
if file_ptr:
    print("file is open successfully")
# close the file
file_ptr.close()
print("file is closed")

# Reading the file
# open file in read mode
file_ptr = open("file.txt", "r")
# store all data into a content variable
file_content = file_ptr.read(50)
# print the type of data stored
print(type(file_content))
# print content of the file
print(file_content)
# close the file
file_ptr.close()

# writing to the file
# open file in append mode
file_ptr = open("file.txt", "a")
# appending new content
file_ptr.write("\n Python is the modern day language."
               " It makes programming simple.")
# close the file
file_ptr.close()
