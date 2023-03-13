'''
write functions for operation
'''
file_name = str(input("File Name: ")).lower()
words = file_name.split(".")
if len(words) >= 2:
    file = words [1]

#write main code
if file_name.endswith("gif") or file_name.endswith("jpeg") or file_name.endswith("png"):
    print("image/" + file,)
elif file_name.endswith("jpg") :
    print("image/" + "jpeg")
elif file_name.endswithelif("pdf") or file_name.endswith("txt") or file_name.endswith("zip"):
    print("application/" + file)
else :
    print("application/octet-stream")

