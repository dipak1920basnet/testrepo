file_name = str(input("File name: ")).lower()
if "." in file_name:
    first , last = file_name.split(".")
    if file_name.endswith(".gif"):
        print(f"{first}/{last}")
    elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
        print(f"image/jpeg")
    elif file_name.endswith(".png"):
        print(f"image/{last}")
    elif file_name.endswith(".pdf"):
        print(f"application/{last}")
    elif file_name.endswith(".txt"):
        print(f"{first}/{last}")
    elif file_name.endswith(".zip"):
        print(f"{first}/{last}")
    else:
        print(f".{last} does not exist")
else:
    print("application/octet-stream")
    