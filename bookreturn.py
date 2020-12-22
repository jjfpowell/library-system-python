import database as base
#This file sets the process to return the book
def book_return(entry):
    """This function holds the code to return a book. Takes the Book ID number"""
    base.valid_books()
    base.book_id_check(entry)
    base.book_select(entry)
    base.book_loan_status(base.book_select.selected_book)
    if base.book_loan_status.status=="Available":
        book_return.result=\
        "This book cannot be returned as its currently available"
    elif base.book_loan_status.status=="On Loan":
        book_return.result="Returned!"
        member_number=int(base.book_select.selected_book[5])
        #Previous line isolates the member number from the database
        base.update_loan_status(0)
        base.update_logfile(member_number)
    elif book_loan_status.status == "Error":
        book_return.result="Error with this book. Consult librarian."
    return book_return.result
