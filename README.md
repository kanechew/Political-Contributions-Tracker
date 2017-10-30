# Political-Contributions-Tracker

## Table of Contents
1. [Introduction](README.md#introduction)
2. [Getting Started](README.md#getting-started)
3. [Usage](README.md#usage)
4. [Input File](README.md#input-file)
5. [Output Files](README.md#output-files)
6. [Example](README.md#example)
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

* No local installation required. 
* Download the Github folder to execute `run.sh`, `run_tests.sh` or `find_political_donors.py` locally.

## Usage (For Mac)

To execute `run_tests.sh`
1. Open Terminal Application
2. Nagivate to folder `.\insight_testsuite`
3. Execute the following command `$ sh run_tests.sh`

To execute `run.sh`
1. Open Terminal Application
2. Nagivate to root folder
3. Execute the following command `$ sh run.sh`

## Input File
The input file, `itcont.txt` is in pipe-demlimited format and conform to the data dictionary as described by the FEC.

See [indiv_header_file.csv](headerfile) file for details of the header.

For more details on the file format:
http://classic.fec.gov/finance/disclosure/metadata/DataDictionaryContributionsbyIndividuals.shtml

## Output Files
Running the shell script will produce two .txt files:

* medianvals_by_zip.txt
* medianvals_by_date.txt

### medianvals_by_zip.txt

#### Description

#### Format

#### Test Sample

## medianvals_by_date.txt

### Description

### Format

### Test Sample

## Built With

* [PyCharm](https://www.jetbrains.com/pycharm/) - Python IDE
* [Cloud9](https://c9.io/) - Cloud Development Environment

## Contributing

N.A

## Author

* Kane Chew

## License

* This project is licensed under the GNU AGPL v3.0 License - see the [LICENSE.md](LICENSE) file for details

## Acknowledgements

* Folks from INSIGHT

## Links

* [Finance Data for U.S. Elections](http://classic.fec.gov/finance/disclosure/ftpdet.shtml)

## FAQ

* To find out about the programming methodology and source code - see the [TECHNICALNOTES.md](TECHNICALNOTES) file for details


