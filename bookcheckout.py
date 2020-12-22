import database as base
#Function broken into 3 stages to improve GUI implementation
#This File runs the bookcheckout system
def book_check_sys(usrID,bkID):
    ''''This function check that the members ID is valid.
        Takes the inputted UserID and BookID'''
    base.member_id_check(usrID)
    Idstr=base.member_id_check.mID
    base.valid_books()
    base.book_id_check(bkID)
    bookidstr=base.book_id_check.bID
    if bookidstr != Idstr:
        book_check_sys.final_output_1="Error, please check inputs."
        return book_check_sys.final_output_1
    else:
        book_check_sys.final_output_1="Accepted."
        book_check_sys2(usrID,bkID)
        return book_check_sys.final_output_1
    
def book_check_sys2(usrID,bkID):
    ''''Checks the loan status and returns if it is available.
        Takes the inputted UserID and BookID'''
    base.book_select(bkID)
    base.book_loan_status(base.book_select.selected_book)
    if base.book_loan_status.status == "On Loan":
        book_check_sys2.final_output_2="Sorry, this book is on loan."
        return book_check_sys2.final_output_2
    elif base.book_loan_status.status == "Available":
        book_check_sys2.final_output_2="Available! Do you want to loan it?"
        return book_check_sys2.final_output_2
    elif base.book_loan_status.status == "Error":
        book_check_sys2.final_output_2="Error with book. Consult librarian."
        return book_check_sys2.final_output_2

def book_check_sys3(yIN):
    ''''Finishes the loan and updates database and log file.
        Takes value "y" or "n" referring to if they want to loan it'''
    if yIN == 'y':
        book_check_sys3.final_output_3="Loaned!"
        base.update_loan_status(base.mem_num)
        base.update_logfile(base.mem_num)
        return book_check_sys3.final_output_3
    else:
        book_check_sys3.final_output_3="Cancelled"
        return book_check_sys3.final_output_3

