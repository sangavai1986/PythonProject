f = open("output.txt","w")
f.write("Writing a new content to the file\n")
f.close()

f = open("output.txt","a")
f.write("Appending to the file")
f.close()

f = open("output.txt")
print(f.read())
f.close()