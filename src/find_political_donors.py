# Import Packages
# ---------------

from collections import defaultdict
from collections import OrderedDict
from datetime import datetime
import math
import statistics

# User Specified Input and Output Files
# -------------------------------------

input_file      = './input/itcont.txt'
output_file_1   = './output/medianvals_by_zip.txt'
output_file_2   = './output/medianvals_by_date.txt'

# Initialize Data Structures
# --------------------------

# Store list of individual contributions to each recipient by zip code
# Key: cmte_id, Value: short_zip_code
zip_dict1 = defaultdict(list)

# Store list of individual contributions to each recipient by transaction amount
# Key: cmte_id, Value: transact_amt
zip_dict2 = defaultdict(list)

# Store list of individual contributions to each recipient by date
# Key: cmte_id, Value: transact_dt
dt_dict1 = defaultdict(list)

# Store list of individual contributions to each recipient by transaction amount
# Key: cmte_id, Value: transact_amt
dt_dict2 = defaultdict(list)

# Store total transaction amount to each recipient by unique date
# Key1: cmte_id, Key2: trans_dt_ymd, Value: dt_trans_total
dt_dict3 = defaultdict(dict)

# Store median transaction amount to each recipient by unique date
# Key1: cmte_id, Key2: trans_dt_ymd, Value: dt_trans_median
dt_dict4 = defaultdict(dict)

# Function Definition
# -------------------

# earliest_date = '01011978'
# start_date = datetime.datetime.strptime(earliest_date, '%m%d%Y').date()

def check_date(date):
    """Return True if TRANS_DT is a valid date"""
    valid_date              = None          # Initial condition

    if date.isdigit():                      # Check if date string consist of all digits

        if len(date) == 8:                  # Check if date is of valid length
            try:
                new_date = datetime.strptime(date, '%m%d%Y').date()
                valid_date = True

                # Check if date is later than today or earlier than start_date
                # if new_date > datetime.date.today() or new_date < start_date:
                #    valid_date  = False
                # else:
                #    valid_date  = True

            except ValueError:
                valid_date = False
        else:
                valid_date = False
    else:
                valid_date = False

    return valid_date;

def check_zip(zip_code):
    """Return True if zip_code is valid"""
    valid_zip           = None  # initial condition

    # Check if zip code substring consist of all digits
    if zip_code.isdigit():

        if len(zip_code) >= 5 and len(zip_code) < 10:
            valid_zip   = True
        else:
            valid_zip   = False
    else:
            valid_zip   = False

    return valid_zip;

def process_output_1(lines_list):
    """Process lines in input text file and produce output text file 1"""
    text_file_1 = open(output_file_1, "w")
    for line in lines_list:

        groups = line.split('|')

        # Check 3 initial input conditions
        if not ('|'.join(groups[15:16])):                               # Check if OTHER_ID is empty
            if '|'.join(groups[0:1]):                                   # Check if CMTE_ID is empty
                if '|'.join(groups[14:15]):                             # Check if TRANS_AMT is empty

                    # Extract relevant substrings from line
                    cmte_id             = '|'.join(groups[0:1])
                    long_zip_code       = '|'.join(groups[10:11])
                    trans_dt            = '|'.join(groups[13:14])
                    trans_amt           = float('|'.join(groups[14:15]))

                    valid_zip           = check_zip(long_zip_code)      # Check for valid zip code
                    valid_date          = check_date(trans_dt)          # Check for valid date

                    if valid_zip and valid_date:

                        short_zip_code  = long_zip_code[:5]

                        zip_dict1[cmte_id].append(short_zip_code)
                        zip_dict2[cmte_id].append(trans_amt)
                        dt_dict1[cmte_id].append(trans_dt)
                        dt_dict2[cmte_id].append(trans_amt)

                    elif valid_zip:
                        short_zip_code  = long_zip_code[:5]

                        zip_dict1[cmte_id].append(short_zip_code)
                        zip_dict2[cmte_id].append(trans_amt)

                    elif valid_date:

                        dt_dict1[cmte_id].append(trans_dt)
                        dt_dict2[cmte_id].append(trans_amt)

                    else:
                        pass;                                           # Entire record is ignored

                    if valid_zip:

                        zip_trans_total = 0
                        zip_trans_count = 0
                        zip_list        = list()                        # Temporary list to calculate running median

                        for index, value in enumerate(zip_dict1[cmte_id]):
                            if value == short_zip_code:
                                zip_trans_total += (zip_dict2[cmte_id][index])
                                zip_trans_count += 1
                                zip_list.append(zip_dict2[cmte_id][index])

                        zip_trans_median = math.ceil(statistics.median(zip_list))

                        #print("%s|%s|%s|%s|%s \n" %(cmte_id, short_zip_code, zip_trans_median,
                        #                            zip_trans_count, int(zip_trans_total)))

                        text_file_1.write("%s|%s|%s|%s|%s \n" %(cmte_id, short_zip_code, int(zip_trans_median),
                                                                zip_trans_count, int(zip_trans_total)))
                    else:
                        pass;                                           # Do not write to file if zip code is invalid

    text_file_1.close()

def process_unique_total_median():
    """ Populate two dictionaries with unique transaction total and median by date"""
    for cmte_id in dt_dict1:

        unique_dates        = set(dt_dict1[cmte_id])

        for trans_dt in unique_dates:                               # For each unique date

            dt_trans_total  = 0                                     # Transaction Counter
            dt_list         = list()                                # Temporary list to calculate unique median

            for index, value in enumerate(dt_dict1[cmte_id]):

                if value == trans_dt:
                    dt_list.append(dt_dict2[cmte_id][index])
                    dt_trans_total += float(dt_dict2[cmte_id][index])

            dt_trans_median = math.ceil(statistics.median(dt_list))
            trans_dt_ymd    = datetime.strptime(trans_dt, '%m%d%Y').strftime('%Y%m%d')

            dt_dict3[cmte_id][trans_dt_ymd] = dt_trans_total
            dt_dict4[cmte_id][trans_dt_ymd] = dt_trans_median

def process_output_2():
    """Process lines in input text file and produce output text file 2"""
    text_file_2 = open(output_file_2, "w")

    for cmte_id in sorted(dt_dict3):
        for new_date in OrderedDict(sorted(dt_dict3[cmte_id].items())):

            dt_trans_total  = dt_dict3[cmte_id][new_date]
            dt_trans_median = dt_dict4[cmte_id][new_date]

            trans_dt_mdy    = datetime.strptime(new_date, '%Y%m%d').strftime('%m%d%Y')
            dt_trans_count  = dt_dict1[cmte_id].count(trans_dt_mdy)

            #print("%s|%s|%s|%s|%s" % (cmte_id, trans_dt_mdy, dt_trans_median, dt_trans_count, int(dt_trans_total)))
            text_file_2.write("%s|%s|%s|%s|%s \n" % (cmte_id, trans_dt_mdy, int(dt_trans_median),
                                                     dt_trans_count, int(dt_trans_total)))

    text_file_2.close()


# Main Function
# -------------

def main():

    with open(input_file) as filehandle:                    # Open input text file
        lines_list = filehandle.readlines()                 # Read each line into a list

    lines_list = [line.strip() for line in lines_list]      # Remove trailing whitespace characters

    process_output_1(lines_list)                            # Produce Output Text File 1

    process_unique_total_median()                           # Populate 2 dictionaries with unique transaction total/mean

    process_output_2()                                      # Produce Output Text File 1


if __name__ == '__main__':
  main()
