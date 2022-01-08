#!/usr/bin/python
from tkinter import *
from service import TicketSPlitService

root = Tk()

title = Label(root, text="----------Add a match----------", pady=20)
title.grid(row=0, column=1)

l1 = Label(root, text="Match tag")
l1.grid(row=1, column=0)
l2 = Label(root, text="Bet")
l2.grid(row=1, column=1)
l3 = Label(root, text="Stake")
l3.grid(row=1, column=2)

match_tag = Entry(root)
match_tag.grid(row=2, column=0)
bet = Entry(root)
bet.grid(row=2, column=1)
stake = Entry(root)
stake.grid(row=2, column=2)

NEW_ROW = 5
INPUT = []
TICKET_TO_SHOW = 0

def handleClick():
    global NEW_ROW, INPUT
    new_match = Label(root, text=f"{match_tag.get()} - {bet.get()} - {stake.get()}")
    new_match.grid(row=NEW_ROW, column=1)
    INPUT.append({
        "tag": str(match_tag.get()),
        "bet": str(bet.get()),
        "stake": float(stake.get())
    })
    NEW_ROW += 1
    match_tag.delete(0, END)
    bet.delete(0, END)
    stake.delete(0, END)

def finishTicket():
    global INPUT
    t = TicketSPlitService(INPUT)
    t.prettyPrint()
    printTickets(t, NEW_ROW + 1, NEW_ROW + 2)

def printTickets(ticketMaster, pannelRow, buttonsRow):
    global NEW_ROW
    _column = 0
    for ticket in ticketMaster.TICKETS:
        toShow = f"Ticket #{ticketMaster.TICKETS.index(ticket) + 1}\n"
        for match in ticket:
            toShow += f"{ticket.index(match) + 1}. {match['tag']} - {match['bet']} - {match['stake']}\n"
        toShow += f"Stake: {ticketMaster.calculateStake(ticket)}"
        t = Label(root, text=toShow, padx=10)
        t.grid(row=NEW_ROW, column=_column)
        _column += 1
        if _column == 4:
            _column = 0
            NEW_ROW += 1

add_button = Button(root, text="Add match to ticket", command=handleClick)
add_button.grid(row=3, column=1, pady=20)
ticket_ready = Button(root, text="Finish ticket", command=finishTicket)
ticket_ready.grid(row=4, column=1, pady=20)

root.mainloop()