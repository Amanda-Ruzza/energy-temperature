# Cleans up and transforms the raw temperature tables into a CSV file for BigQuery
import logging
import csv
import sys, getopt
import os
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Function for CLI arguments/script execution
"""
To execute this script, input this on the CLI from the current directory where the script is located:
    python temperature-transform.py -i <input_raw_file.csv> -t <input_raw_file.txt> -o <output_file.csv>
"""
def main(argv):
    inputfile_csv = ''
    inputfile_txt = ''
    outputfile_csv = ''
    
    try:
        opts, args = getopt.getopt(argv[1:], "i:o:t:", ["ifile=", "ofile=", "txtfile="])
    except getopt.GetoptError:
        print("python " + argv[0] + " -i <inputfile_csv> -o <outputfile_csv> -t <inputfile_txt>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("python " + argv[0] + " -i <inputfile_csv> -o <outputfile_csv> -t <inputfile_txt>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            script_directory = os.path.dirname(os.path.abspath(__file__))
            inputfile_csv = os.path.join(os.path.dirname(script_directory), "raw-files", arg)
        elif opt in ("-o", "--ofile"):
            script_directory = os.path.dirname(os.path.abspath(__file__))
            outputfile_csv = os.path.join(os.path.dirname(script_directory), "raw-files", arg)
        elif opt in ("-t", "--txtfile"):
            script_directory = os.path.dirname(os.path.abspath(__file__))
            inputfile_txt = os.path.join(os.path.dirname(script_directory), "raw-files", arg)
            
    logger.info('Input CSV file is:\n' + str(inputfile_csv))
    logger.info('Input TXT file is:\n' + str(inputfile_txt))
    csv_station_id, fmt_dates, weather_element, weather_element_data_val, measurement_flag, quality_flag = parse_temperatures(inputfile_csv)
    
    # Check if the inputfile_txt exists before parsing it
    if os.path.exists(inputfile_txt):
        txt_state, txt_station_name, txt_latitude, txt_longitude, txt_elevation, txt_station_id = parse_stations(inputfile_txt)
    else:
        print(f"File {inputfile_txt} not found. Skipping TXT file parsing.")
        txt_state, txt_station_name, txt_latitude, txt_longitude, txt_elevation, txt_station_id = [], [], [], [], [], []
        
    logger.info('Output file is:\n' + str(outputfile_csv))
    write_to_output_csv(outputfile_csv, fmt_dates, csv_station_id, txt_state, txt_station_name, txt_latitude, txt_longitude, weather_element, weather_element_data_val, measurement_flag, quality_flag)  # Call the write_to_output_csv function
    return

    # CSV Parsing:
def parse_temperatures(inputfile_csv):
    # Initialize empty lists for each column in the CSV file:
    csv_station_id = [] # string type
    date = [] #integer type
    weather_element = [] # string type
    weather_el_data_val = [] # integer type
    measurement_flag = [] # string type
    quality_flag = [] # string type
    source_flag = [] # string type
    # Convert empty strings to 'None'/'null' for BigQuery:
    convert_to_null = lambda val: None if val == '' else val

    with open(inputfile_csv, 'r') as infile:
        csv_reader = csv.reader(infile)
        next(csv_reader)
        for row in csv_reader:
            # Append each value to the respective column list
            if row[0].startswith('US'):
                csv_station_id.append(row[0].upper())
                date.append(int(row[1]))
                weather_element.append(row[2])
                weather_el_data_val.append(int(row[3]))
                measurement_flag.append(convert_to_null(row[4]))
                quality_flag.append(convert_to_null(row[5]))
            # source_flag.append(row[6]) # is the source flag for the first day of the month - I don't need this original column
        
    # Column transformations:
    # Covert dates from int to the YYYY-MM-DD format
    fmt_dates = list(map(lambda d_int: datetime.strptime(str(d_int), "%Y%m%d").strftime("%Y-%m-%d"), date))
    logger.info('Converted the raw integer dates into "YYYY-MM-DD" for BigQuery \n')
    logger.info('Parsed the raw CSV file \n')
    return csv_station_id, fmt_dates, weather_element, weather_el_data_val, measurement_flag, quality_flag
    

def parse_stations(inputfile_txt):
    # Initialize empty lists for each column in the TXT file:
    station_data = {} # string type
    txt_latitude = [] # float type
    txt_longitude = [] # float type
    txt_elevation = [] # float type [don't need this one on the output file]
    txt_state = [] # string type
    txt_station_name = [] # string type

    print(f"Attempting to open and read file: {inputfile_txt}")
    with open(inputfile_txt, 'r') as txtfile:
        csv_station_reader = csv.DictReader(txtfile, fieldnames=["station_id_st", "latitude", "longitude", "elevation", "state", "station_name" ], delimiter="\t")
        # Count each element per line
        for row in csv_station_reader:
    #         if row.isspace() == True:
    #             print("Found Spaces in rows")
    #         station_data[row["station_id_st"]] = row.values() # add the keys for each of the rows
    # print(station_data.keys())
    
            return(station_data)
    

    # TXT data transformations 

    # return txt_state, txt_station_name, txt_latitude, txt_longitude, station_data, txt_elevation


def write_to_output_csv(output_file_csv, fmt_dates, csv_station_id, txt_state, txt_station_name, txt_latitude, txt_longitude, weather_element, weather_el_data_val, measurement_flag, quality_flag):
    try:
        logger.debug('Writing to the output CSV file.')
        logger.debug(f'Length of csv_station_id: {len(csv_station_id)}')
        logger.debug(f'Length of fmt_dates: {len(fmt_dates)}')
        logger.debug(f'Length of measurement_flag: {len(measurement_flag)}')
        logger.debug(f'Length of quality_flag: {len(quality_flag)}')

        # Convert None values to 'null' for BigQuery
        measurement_flag = ['null' if val is None else val for val in measurement_flag]
        quality_flag = ['null' if val is None else val for val in quality_flag]

        with open(output_file_csv, 'w', newline='') as outfile:
            csv_writer = csv.writer(outfile)

            # csv_station_id, fmt_dates, measurement_flag, and quality_flag should have the same length
            for i in range(len(csv_station_id)):
                csv_writer.writerow([csv_station_id[i], fmt_dates[i], measurement_flag[i], quality_flag[i]])

        logger.info('Writing to the output CSV file completed.')
    except Exception as e:
        logger.error(f'Error occurred during writing to the output CSV file: {e}')


if __name__ == '__main__':
  main(sys.argv)
  logging.getLogger().setLevel(logging.INFO)