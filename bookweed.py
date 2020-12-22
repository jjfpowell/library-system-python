#File holds bookweeding code
import database as base
import matplotlib.pyplot as plt
from datetime import date
from database import valid_books as v
from database import days_between as d
"""Bookweeding function to identify books which have not been taken
out in over 21 days"""
def weeding():
    today=date.today()
    given_date=today.strftime("%d/%m/%Y")#Gets todays date
    base.valid_books()
    up_list=base.valid_books.valid_book_ids
    del up_list[0]
    with open("logfile.txt","r") as log:
        logs_list=log.readlines()
        index_list=[]
        for x in logs_list:
            log_str=x.strip()
            selected_line=log_str.split(":")
            index_list.append(selected_line[0])
        last_entry=[]
        for x in up_list:
            res=''.join(index_list).rindex(str(x))
            last_entry.append((res-1))
        weeding.books_to_weed=[]
        weeding.num_days=[]
        for z in last_entry:
            x=logs_list[z]
            log_str=x.strip()
            selected_line=log_str.split(":")
            base.days_between(given_date,selected_line[2])
            if d.time_between>=21:
                weeding.books_to_weed.append(selected_line[0])
                weeding.num_days.append(d.time_between)
        log.close()
