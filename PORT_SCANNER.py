#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:04:26 2020

@author: swapnil
"""

import socket as sp
import time 
target_name=str(input("Input target Site/Name : "))
target_ip=sp.gethostbyname(target_name)
port_list=[]
print("Scanning Range in between 0-65535")
i=int(input("ENTER STARTING RANGE : "))
j=int(input("ENTER ENDING RANGE : "))
print("Scanning in Progress...")
start_time=time.time()
print("\nTarget_NAME :",target_name,"\nTarget_IP :",target_ip)
      
for k in range(i,j+1):
      port=k
      
      try:
          sock=sp.socket(sp.AF_INET,sp.SOCK_STREAM)
          sock.settimeout(1)
          sock.connect((target_ip,port))
          print("PORT :",port," OPEN")
          port_list.append(port)
          sock.close();
    
      except:
          print("PORT :",port," CLOSE")
                
print("PORT SCANNING COMPLETE !!")
stop_time=time.time()
time_total=stop_time-start_time
print("Time Taken : ",round(time_total,2), "Seconds...")
print("ALL OPEN PORTS ARE : ")
for i in port_list:
 print(i)    
