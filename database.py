#Database file hold all common functions
from datetime import date
from datetime import datetime
def member_id_check(member_id):
    """Checks the validity of a member number from input"""
    try:
        global mem_num
        mem_num=int(member_id)
        if 1000<=mem_num and 9999>=mem_num:
            member_id_check.mID="Accepted"
        else:
            member_id_check.mID="Member number not recognised"
    except ValueError:
        member_id_check.mID="Member number not valid"
    return member_id_check.mID

def valid_books():
    """Produces a list of valid books in the database.txt"""
    with open("database.txt","r") as data:
        global valid_book_ids
        valid_books.valid_book_ids=[]
        global database_book_list
        database_book_list=data.readlines()
        for x in database_book_list:
            book_str=x.strip() #Creates a list from database
            selected_book=book_str.split(":")#Creates a string from list
            valid_books.valid_book_ids.append(str(selected_book[0]))
        return valid_books.valid_book_ids
        data.close()
        
def book_id_check(book_num):
    """Checks if inputted Book ID is valid"""
    try:
        global book_id
        book_id=int(book_num)
        if str(book_id) in valid_books.valid_book_ids:
            book_id_check.bID="Accepted"
            global max_book_id
            max_book_id=len(valid_books.valid_book_ids)
        else:
            book_id_check.bID="Book ID not recognised"
    except ValueError:
        book_id_check.bID="Book ID number not recognised"
    return book_id_check.bID

def book_select(book_num):
    """Isolates the books chosen by the user from the database"""
    with open("database.txt","r") as data:
        global database_book_list
        database_book_list=data.readlines()
        global list_pos
        list_pos=0
        for x in database_book_list:
            book_str=x.strip()
            book_select.selected_book=book_str.split(":")
            if book_select.selected_book[0] == str(book_num):
                data.close()
                return book_select.selected_book
            list_pos+=1

def book_loan_status(sltBK):
    """Creates global variables which are used to show a books status"""
    book_loan_status.status=None
    if sltBK[5] != "0":
        book_loan_status.status="On Loan"
        return book_loan_status.status
    elif sltBK[5] == "0":
        book_loan_status.status="Available"
        return book_loan_status.status
    else:
        book_loan_status.status="Error"
        return book_loan_status.status

def update_loan_status(updated_number):
    """Change the loan status of a book in the database"""
    del book_select.selected_book[-1]
    book_select.selected_book.append(str(updated_number))
    updated=':'.join(book_select.selected_book)
    del database_book_list[list_pos]
    database_book_list.insert(list_pos,updated)
    for index in range(0,max_book_id):
        strip_list=database_book_list[index]
        stripped_str=strip_list.strip()
        del database_book_list[index]
        database_book_list.insert(index,stripped_str)
    with open("database.txt","r+") as data:
        data.seek(0)
        data.truncate(0)
        for index in range(0,max_book_id):
            data.write(str(database_book_list[index]+'\n'))
        data.close()
        
def update_logfile(mem_id):
    """Update the log file with any checkout or return"""
    with open("logfile.txt","r+") as log:
        logs_list=log.readlines()
        today=date.today()
        given_date=today.strftime("%d/%m/%Y")
        if book_loan_status.status == "On Loan":
            log_list_pos=0
            count=len(logs_list)
            #For loop check to see if a books return status is not returned
            for x in logs_list:
                log_str=x.strip()
                log_selection=log_str.split(":")
                if str(log_selection[0]) == str(book_id)\
                   and str(log_selection[-2])=="Not Returned":
                    del log_selection[-2]
            #Then inserts given date instead
                    log_selection.insert(2,given_date)
                    updated=':'.join(log_selection)
                    del logs_list[log_list_pos]
                    logs_list.insert(log_list_pos,updated)
                    for index in range(0,count):
                        strip_list=logs_list[index]
                        stripped_str=strip_list.strip()
                        del logs_list[index]
                        logs_list.insert(index,stripped_str)
                    log.seek(0)
                    log.truncate(0)
                    for index in range(0,count):
                        log.write(str(logs_list[index]+'\n'))
                    log.close()
                log_list_pos+=1
        elif book_loan_status.status == "Available":
            new_entry=str("%d:%s:Not Returned:%d"%(book_id,given_date,mem_id))
            logs_list.append(new_entry)
            count=len(logs_list)
            for x in range(0,count):
                strip_list=logs_list[x]
                stripped_str=strip_list.strip()
                del logs_list[x]
                logs_list.insert(x,stripped_str)
            log.seek(0)
            log.truncate(0)
            for x in range(0,count):
                log.write(str(logs_list[x]+'\n'))
            log.close()
        else:
            print("Error ")
    log.close()

def days_between(date_1, date_2):
    """"Works out time between dates"""
    date_1 = datetime.strptime(date_1, "%d/%m/%Y")
    date_2 = datetime.strptime(date_2, "%d/%m/%Y")
    days_between.time_between = abs((date_2 - date_1).days)
