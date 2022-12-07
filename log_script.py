from pprint import pprint
import pandas as pd
import subprocess
import os
from time import time
# from google.colab import drive
from datetime import datetime 

# writing inline conditions - more efficient

with open('C:/Users/TW/Downloads/15.11.2022_11.50.28.133_log_dump.txt') as fp:
  lines = fp.readlines()

  # print(type(lines))
# ------------------------------------------------------------------
# All lines with text - 'INFO RecordUpdateProcessor - Finished processing'
  all_lines = []

# All lines with text - 'RecordUpdateProcessor - Processing jobActivity'
  all_lines2 = []

  for line in lines:
    # print(line)
    text = 'INFO RecordUpdateProcessor - Finished processing'
    text2 = 'RecordUpdateProcessor - Processing jobActivity'

    if text in line:
      all_lines.append(line)
    elif text2 in line:
      all_lines2.append(line)

    # lista = [all_lines.append(line) if text in line else all_lines2.append(line) if (text2 in line) else exit()]
    # print(all_lines)


  # print(all_lines)
  # print(all_lines2[1])

# ----------------------------------------------------------------
  # function to extract match lines and save in list

  # def getLinesWithMatch():
  #   logs = []
  #   for line in lines:
  #     if text in line:
  #       logs.append(line)
  #     else:
  #       exit()
  #   return logs

  # print(getLinesWithMatch())

  # ------------------------------------------------------------

  # Function to extract timestamp
  # print(all_lines)

  def getTimeStamp(new_line):
    # times = [time.strptime(dat[:19], '%Y-%m-%d %H:%M:%S') for dat in all_lines]
    # times = [datetime.strptime(dat[:19], '%Y-%m-%d %H:%M:%S') for dat in all_lines]
    times = []
    for x in new_line:
      list = datetime.strptime(x[:19], '%Y-%m-%d %H:%M:%S')
      # list = datetime.strptime(x[11:19], '%H:%M:%S%f')
      # timeVal = list.time()
      times.append(list)
      # times.append(timeStamp)
    return times

  # print(getTimeStamp(all_lines))
  list1 = getTimeStamp(all_lines)
  list2 = getTimeStamp(all_lines2)

  # print(list1[2], list2[2])
  # print(all_lines[1], all_lines2[1])

# Join - joins single list elements using str values
  # difference = ['|'.join([str(i), list2[i].strftime('%Y-%m-%d %H:%M:%S'), list1[i].strftime('%Y-%m-%d %H:%M:%S'), str((list1[i]-list2[i]).total_seconds())]) for i in range(min(len(list1), len(list2)))]
  # pprint(difference)


  # ==========================================ALTERNATIVE FUNCTION=================================

  total_time_spent_waiting_for_this_step = 0

  for i in range(min(len(list1), len(list2))):
    sum = (list1[i]-list2[i]).total_seconds()
    total_time_spent_waiting_for_this_step += sum

  print(total_time_spent_waiting_for_this_step)

  
  process_time = list1[-1] - list2[-1]
  print(list1[-1])
  print(list2[-1])
  print(process_time)

  # list1 , list2 , time difference

  # GET NUMBER OF LINES WITH VALUES
  # print(len(list1) , ' - ' , len(list2))

  #initialize a variable which will store the difference of two lists
  # -------------------------------------------------------------------------loop
  # result = []
  
  # for i, j in zip(list2,list1):
  #     result.append(i - j)
  # print(result)

  # for x in result:
  #   print(x)
    
  # for k in getTimeStamp():
  #   print(k)


  # find second 
  