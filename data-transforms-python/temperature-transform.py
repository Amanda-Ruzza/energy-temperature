# Cleans up and transforms the raw temperature tables into a CSV file for BigQuery
import logging
import csv
import sys, getopt
import os
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# This the function where we want to entry the script
"""
To execute this script, input this on the CLI from the current directory where the script is located:
    python temperature-transform.py -i <input_file.csv> -o <output_file.csv>
"""

def main(argv):
    inputfile = ''
    outputfile = ''
    
    try:
       opts, args = getopt.getopt(argv[1:],"hi:o:c:",["ifile=","ofile="])
    except getopt.GetoptError:
       print (f"{argv[0]} -i <inputfile> -o <outputfile> ")
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
           print (f"{argv[0]} -i <inputfile> -o <outputfile> ")
           sys.exit()
       elif opt in ("-i", "--ifile"):
           # get the location of this script
            script_directory = os.path.dirname(os.path.abspath(__file__))
            # build the full path to the input file location
            inputfile = os.path.join(os.path.dirname(script_directory), "raw-files", arg)

       elif opt in ("-o", "--ofile"):
           # get the path of the script's directory and send the 'outfile' to the original 'raw-files' directory
           script_directory = os.path.dirname(os.path.abspath(__file__))
           outputfile = os.path.join(os.path.dirname(script_directory), "raw-files", arg)
       

    logger.info('Input file is: ' + str(inputfile))
    parse_raw_csv(inputfile, outputfile)
    logger.info('Output file is: ' + str(outputfile))

def parse_raw_csv(input_file_name, output_file_name):
    # Initialize empty lists for each column
    station_id = [] # string type
    date = [] #integer type
    weather_element = [] # string type
    weather_el_data_val = [] # integer type
    measurement_flag = [] # string type
    quality_flag = [] # string type
    source_flag = [] # string type
    obs_time = [] #integer:  4-character time of observation in hour-minute format (i.e. 0700 =7:00 am)


    with open(input_file_name, 'r') as infile:
        csv_reader = csv.reader(infile)
        next(csv_reader)
        for row in csv_reader:
            # Append each value to the respective column list
            station_id.append(row[0])
            date.append(int(row[1]))
            weather_element.append(row[2])
            weather_el_data_val.append(int(row[3]))
            measurement_flag.append(row[4])
            quality_flag.append(row[5])
            # source_flag.append(row[6]) # is the source flag for the first day of the month - I don't need this original column

   # Column transformations:
    station_id = list(filter(lambda usa: 'US' in usa, station_id))

    with open(output_file_name, 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        # Outfile headers: #Don't need headers for BigQuery
        # csv.writer.writerow(["station_id", "date", "wx_elm", "wx_elm_dt_val", "mmt_flag", "q_flag"])
        for i in range(len(station_id)):
            csv_writer.writerow([station_id[i],date[1]])




def convert_dates():
    pass

if __name__ == '__main__':
  main(sys.argv)
  logging.getLogger().setLevel(logging.INFO)