import os
import csv

#Specify a unique tag for this set of results
file_tag = "results"

# Specify the folder path
input_path = "data"
output_path = "output"

with open(os.path.join(output_path, file_tag + "_DAPI.csv"), "w") as output_dapi, open(os.path.join(output_path, file_tag + ".csv"), "w") as output_area:
    dapi_writer = csv.writer(output_dapi)
    area_writer = csv.writer(output_area)
    area_writer.writerow(["Name", "Whole", "AF790", "AF488"])


    # Loop through each file in the folder
    for filename in os.listdir(input_path):
        file_path = os.path.join(input_path, filename)
        if os.path.isfile(file_path):  # Check if it's a file
            print(f"Processing file: {filename}")
            if "_DAPI.csv" in filename:
                with open(file_path, "r", newline='') as csv_file:
                    length = sum(1 for _ in csv_file) -1
                    dapi_writer.writerow([filename[3:8], length])
            elif "Results.csv" in filename:
                with open(file_path, "r", newline='') as csv_file:
                    results_reader = csv.reader(csv_file)
                    next(results_reader) #skip first row
                    new_row = [filename[3:8]]
                    for row in results_reader:
                        new_row.append(row[1])
                    area_writer.writerow(new_row)
                    
