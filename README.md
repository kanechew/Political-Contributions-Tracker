# Political-Contributions-Tracker

## Table of Contents
1. [Introduction](README.md#introduction)
2. [Getting Started](README.md#getting-started)
3. [Usage](README.md#usage)
4. [Input File](README.md#input-file)
5. [Output Files](README.md#output-files)
6. [User Test Cases](README.md#user-test-cases)
7. [Built With](README.md#built-with)
8. [Contributing](README.md#contributing)
9. [Author](README.md#author)
10. [License](README.md#license)
11. [Acknowledgements](README.md#acknowledgements)
11. [Links](README.md#links)
11. [FAQ](README.md#faq)

## Introduction
This program extracts and calculates individual contributions towards political campaigns from finance data downloaded from the Federal Election Commission.

## Getting Started

### Prerequistes

* Linux or Unix system
* If you are using a Windows system, consider tools such as Cygwin or Docker, or a free online IDE such as Cloud9

### Installation

* No installation required locally
* Download the Github folder to execute `run.sh`, `run_tests.sh` or `find_political_donors.py` locally

## Usage (For Mac)

Use a Terminal session to execute the `.sh` and `.py` files:

1. Open `Applications` folder
2. Open the `Utilities` folder
3. Open the `Terminal` application

To execute `run_tests.sh`
* Nagivate to folder `.\insight_testsuite`
* Execute the following command `~$ sh run_tests.sh`

To execute `run.sh`
* Nagivate to root folder
* Execute the following command `~$ sh run.sh`

To execute `find_political_donors.py`
* Nagivate to folder `.\src`
* Execute the following command `~$ python find_political_donors.py`

If you do not have the python statistics module installed, you would need to execute the following commands first:
* `~$sudo easy_install pip`
* `~$sudo python -m pip install statistics`

## Input File
The input file, `itcont.txt` is in pipe-demlimited format and conform to the data dictionary as described by the FEC.

* See [indiv_header_file.csv](indiv_header_file.csv) file for details of the header
* See [Links](README.md#links) for more information about input file format

If you want to run/test the program with a different input file, you need to edit the name and location of the input file within the `python find_political_donors.py`:

`
### User Specified Input and Output Files
# -------------------------------------
input_file      = 'itcont.txt'
`

## Output Files
Running the shell script will produce two .txt files:

* medianvals_by_zip.txt
* medianvals_by_date.txt

### medianvals_by_zip.txt
The program writes to the first output file named `medianvals_by_zip.txt`. 

#### Description
For each input file line, the running median of contributions, total number of transactions and total amount of contributions streaming in so far for that recipient and zip code is calcualted. The calculated fields is formatted into a pipe-delimited line and written to this ouput file in the same order as the input line appeared in the input file.

#### Format
The first output file medianvals_by_zip.txt should contain the same number of lines or records as the input data file minus any records that were ignored as a result of the [input file considerations](USERTESTCASES.md#input-file-considerations).

Each line of this file contain these fields:
* Recipient of the contribution (or CMTE_ID from the input file)
* 5-digit zip code of the contributor (or the first five characters of the ZIP_CODE field from the input file)
* Running median of contributions received by recipient from the contributor's zip code streamed in so far
* Total number of transactions received by recipient from the contributor's zip code streamed in so far
* Total amount of contributions received by recipient from the contributor's zip code streamed in so far

Note:
* Median and Total amount of contributions should be rounded to the whole dollar (drop anything below $.50 and round anything from $.50 and up to the next dollar)

## medianvals_by_date.txt
The program also writes to a second output file named `medianvals_by_date.txt`. 

### Description
Each line of this second output file lists every unique combination of date and recipient from the input file and then the calculated total contributions and median contribution for that combination of date and recipient.

### Format
The fields on each pipe-delimited line of medianvals_by_date.txt should be date, recipient, total number of transactions, total amount of contributions and median contribution. 

Each line of this file contain these fields:
* Recipient of the contribution (or CMTE_ID from the input file)
* Date of the contribution (or TRANSACTION_DATE from the input file)
* Median of contributions received by recipient on that date. 
* Total number of transactions received by recipient on that date
* Total amount of contributions received by recipient on that date

Note:
* Median and Total amount of contributions should be rounded to the whole dollar (drop anything below $.50 and round anything from $.50 and up to the next dollar)

### Differences between first and second output files
* Unlike the first output file, the second output file have lines sorted alphabetical by recipient and then chronologically by date.
* Also, unlike the first output file, every line in the medianvals_by_date.txt file is represented by a unique combination of day and recipient -- there should be no duplicates.

### User Test Cases


## Built With

* [PyCharm](https://www.jetbrains.com/pycharm/) - Python IDE
* [Cloud9](https://c9.io/) - Cloud Development Environment

## Contributing

N.A

## Author

* [Kane Chew](https://www.linkedin.com/in/kanechew/) 

## License

* This project is licensed under the GNU AGPL v3.0 License - see the [LICENSE.md](LICENSE) file for details

## Acknowledgements

* Folks from INSIGHT

## Links

* [Finance Data for U.S. Elections](http://classic.fec.gov/finance/disclosure/ftpdet.shtml)

* [Details of Input File Format](http://classic.fec.gov/finance/disclosure/metadata/DataDictionaryContributionsbyIndividuals.shtml)

## FAQ

* To find out about the programming methodology and source code - see the [TECHNICALNOTES.md](TECHNICALNOTES.md) file for details


