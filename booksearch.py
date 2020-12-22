#File holds the booksearch code
def booksearch(usr_str):
    """Function check for a book in the library and displays information.
        Takes the user inputted book title"""
    with open("database.txt","r") as d:
        result=[]
        search=str(usr_str)
        if len(search)!=0:
            for line in d:
                s=line.strip()
                strings=s.split(":")
                if search in line:
                    new=','.join(strings)
                    result.append(new)
            if len(result)==0:
                booksearch.output=\
                "Check your spelling or this book is not in the library."
            else:
                booksearch.output="\n".join(result)
        else:
            booksearch.output="Please enter a book title"
        d.close
