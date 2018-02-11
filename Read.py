#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import char_lcd
import time
import testdb
import socket

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    display1('view items(v)?\nsubmit (y/n) ?','static')
    
    c=raw_input("submit?")
    if c=='v':
        a=[]
        b=[]
        c=[]
        d=[]

        import sqlite3
        conn = sqlite3.connect('test.db')
        cursor = conn.execute(" SELECT * from selected_items ")
        for row in cursor:
            a.append(row[0])
            b.append(row[1])
            c.append(row[2])
            d.append(row[3])
        for i in range(len(a)):
            s='ITEM :'+str(b[i])+'\n'+'Price : Rs'+str(c[i])+'/-'
            display1(s,'static')
            time.sleep(2)
            
            
        
    if c=='y':
        a=[]
        b=[]
        c=[]
        d=[]
        import sqlite3
        conn = sqlite3.connect('test.db')
        cursor = conn.execute(" SELECT * from selected_items ")
        for row in cursor:
            a.append(row[0])
            b.append(row[1])
            c.append(row[2])
            d.append(row[3])
        for i in range(len(a)):
            s='cart'+' '+str(a[i])+' '+str(b[i])+' '+str(c[i])+' '+str(d[i])
            client.send(s)
        global continue_reading
        print "Ctrl+C captured, ending read."
        continue_reading = False
    if c=='n':
        return

def display1(text,id):
    char_lcd.display_init(text,id)
# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)
#client initialization
host=raw_input("enter ip address :")
port=input("enter port number :")
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()    

# Welcome message
print "Welcome to the Smart Shopping Cart"
# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    time.sleep(1)
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        text=[]
        k=str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])
        k2=k[0:4]
        a=testdb.database()
        a.create()
        m=a.check(k2)
        try:
            if m=='no':
                client.send(k2)
                reply= client.recv(1024)
                print reply
                text=reply.split(' ')
                a.insert(text)
                display1('ITEM: '+text[1]+'\n'+'Price : Rs'+text[2]+'/-','static')
            if m=='yes':
                client.send(k2)
                reply= client.recv(1024)
                text=reply.split(" ")
                display1('deleted: '+text[1],'scroll')
        except:
            GPIO.cleanup()
            pass
            

    
   
    
    

