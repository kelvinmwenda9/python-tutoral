import re

# Regular expression to match lines with the text "INFO RecordUpdateProcessor - Finished processing"
finished_processing_regex = re.compile(r"INFO RecordUpdateProcessor - Finished processing")

# Regular expression to match lines with the text "RecordUpdateProcessor - Processing jobActivity"
processing_job_activity_regex = re.compile(r"RecordUpdateProcessor - Processing jobActivity")

# Regular expression to match lines with the text "SyncService - Start"
sync_service_start_regex = re.compile(r"SyncService - Start")

# Regular expression to match lines with the text "SyncService - End"
sync_service_end_regex = re.compile(r"SyncService - End")

# Open the log file in read mode
with open('C:/Users/TW/Downloads/15.11.2022_11.50.28.133_log_dump.txt') as logfile:
    # Read all lines from the log file
    lines = logfile.readlines()

    # Initialize the total time spent waiting for this step to 0
    total_time_spent_waiting_for_this_step = 0

    # Initialize the start and end timestamps for the SyncService
    sync_service_start = 0
    sync_service_end = 0

    # Iterate over all lines in the log file
    for line in lines:
        # Check if the line matches the "INFO RecordUpdateProcessor - Finished processing" regex
        if finished_processing_regex.match(line):
            # Find the previous line that matches the "RecordUpdateProcessor - Processing jobActivity" regex
            for i in range(lines.index(line) - 1, 0, -1):
                if processing_job_activity_regex.match(lines[i]):
                    # Get the timestamps from the two lines
                    finished_processing_timestamp = line.split(" ")[0]
                    processing_job_activity_timestamp = lines[i].split(" ")[0]

                    # Calculate the difference in timestamps
                    time_spent_waiting = finished_processing_timestamp - processing_job_activity_timestamp

                    # Add the difference to the total time spent waiting for this step
                    total_time_spent_waiting_for_this_step += time_spent_waiting

                    # Move on to the next line
                    break

        # Check if the line matches the "SyncService - Start" regex
        elif sync_service_start_regex.match(line):
            # Get the timestamp from the line
            sync_service_start = line.split(" ")[0]

        # Check if the line matches the "SyncService - End" regex
        elif sync_service_end_regex.match(line):
            # Get the timestamp from the line
            sync_service_end = line.split(" ")[0]

    # Calculate the total time between "SyncService - Start" and "SyncService - End"
    total_sync_time = sync_service_end - sync_service_start

    # Calculate the percentage of time spent waiting for this step
    percentage = (total_time_spent_waiting_for_this_step / total_sync_time) * 100

    # Print the percentage
    if total_sync_time == 0:
        print("Cannot calculate percentage because total sync time is zero.")
    else:
        print("Percentage of time spent waiting for the sync to start: {:.2f}%".format((total_time_spent_waiting_for_sync_to_start / total_sync_time) * 100))
        # print("Percentage of time spent waiting for the sync to start: {:.2f}%".format((total_time_spent_waiting_for_sync_to_start / total_sync_time) * 100))
