import os
import csv

#To use change the file_tag to be a unique name for these results and 
# the input and output paths

#Specify a unique tag for this set of results
file_tag = "results"

# Specify the folder path
input_path = "data"
output_path = "output"

with open(os.path.join(output_path, file_tag + ".csv"), "w") as output_file:
    output_writer = csv.writer(output_file, lineterminator="\n")
    output_writer.writerow(["Name", "Whole", "AF790", "AF488", "No. nuclei"])


    # Loop through each file in the folder
    for filename in os.listdir(input_path):
        file_path = os.path.join(input_path, filename)
        if os.path.isfile(file_path):  # Check if it's a file
            if "Results.csv" in filename:
                print(f"Processing file: {filename}")
                with open(file_path, "r", newline='') as csv_file:
                    results_reader = csv.reader(csv_file)
                    next(results_reader) #skip first row
                    new_row = [filename[3:8]]
                    for row in results_reader:
                        new_row.append(row[1])
                    try:
                        with open(file_path[:-4] + "_DAPI.csv", "r", newline='') as csv_file:
                            length = sum(1 for _ in csv_file) -1
                            new_row.append(length)
                    except FileNotFoundError:
                        print("Error: DAPI file not found for ", filename)
                        new_row.append("MISSING")
                    output_writer.writerow(new_row)
                    
