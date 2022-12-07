from pprint import pprint
import pandas as pd
import subprocess
import os
from time import time
# from google.colab import drive
from datetime import datetime 

# writing inline conditions - more efficient

# with open('C:/Users/TW/Downloads/15.11.2022_11.50.28.133_log_dump.txt') as fp:
#   lines = fp.readlines()
start_times = []
end_times = []
# open the log file in read-only mode
with open('C:/Users/TW/Downloads/15.11.2022_11.50.28.133_log_dump.txt') as fp:
       lines = fp.readlines()

    # iterate over each line in the log file
       for line in lines:
        # check if the line contains the start or end timestamp
        if "SyncService - Start" in line:
        # extract the timestamp and convert it to a datetime object
            start_time = datetime.strptime(line.split()[1], '%H:%M:%S,%f')
            # add the timestamp to the list of start times
            start_times.append(start_time)
        elif "SyncService - End" in line:
        # extract the timestamp and convert it to a datetime object
            end_time = datetime.strptime(line.split()[1], '%H:%M:%S,%f')
            # add the timestamp to the list of end times
            end_times.append(end_time)

  # compute the total time spent waiting for the sync to start
        total_time_spent_waiting_for_sync_to_start = 0
        for i in range(min(len(start_times), len(end_times))):
    # compute the time difference between the start and end timestamps
            time_diff = (end_times[i] - start_times[i]).total_seconds()
            print(time_diff)
            # add the time difference to the total time spent waiting for the sync to start
            total_time_spent_waiting_for_sync_to_start += time_diff

        total_sync_time = 0
        for i in range(len(end_times)):
            # compute the time difference between the start and end timestamps
            time_diff = (end_times[i] - start_times[i]).total_seconds()
            # add the time difference to the total sync time
            total_sync_time += time_diff

  # print the total time spent waiting for the sync to start
        if total_sync_time == 0:
            print("Cannot calculate percentage because total sync time is zero.")
        else:
            print("Percentage of time spent waiting for the sync to start: {:.2f}%".format((total_time_spent_waiting_for_sync_to_start / total_sync_time) * 100))
        # print("Percentage of time spent waiting for the sync to start: {:.2f}%".format((total_time_spent_waiting_for_sync_to_start / total_sync_time) * 100))