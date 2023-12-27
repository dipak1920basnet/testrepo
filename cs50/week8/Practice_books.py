class Books:
    def __init__(self, name, author_name, pages):
        self.name = name
        self.author_name = author_name
        self.pages = pages
def main():
    hello = get_info()
    print(f"Hy I have read the books named {hello.name}, writen by {hello.author_name}. It has total of {hello.pages} ")

def get_info():
    name = input("Enter name:")
    pages = input("Enter pages:")
    author_name=input("Enter the name of the author:")
    books = Books(name, pages, author_name)
    return books

if __name__=="__main__":
    main()