# User Test Cases

## Table of Contents
1. [Introduction](USERTESTCASES.md#introduction)
2. [Construction](USERTESTCASES.md#construction)
3. [Path](USERTESTCASES.md#path)
4. [Test Validation](USERTESTCASES.md#test-validation)
5. [Test Variables](USERTESTCASES.md#test-variables)
6. [Test Values](USERTESTCASES.md#test-values)
7. [Input File Considerations](USERTESTCASES.md#input-file-considerations)

## Introduction
This document describes the extended user test cases for the validation of the python program.

## Construction
Except for Test Case 6, each test case focuses on one input file consideration.

Test Case 6 specifically tests the functionality of the program to write the second output file accurately. 

## Path
The input file and expected output files for each test case are stored in separate folders within the `insight_testsuite` folder.

### Example
The respective files for Test Case 1 are found in `./insight_testsuite/tests/usertest_1`.

## Test Validation
The test cases are validated by executing the `run_tests.sh` file, located in `./insight_testsuite`.

## Test Variables

| Test Case | Row Count | Test Variables | Input Consideration      |
| ----------| ----------| -------------- | -------------------------| 
|  1        | 7         | OTHER_ID       | Empty or Not             |           
|  2        | 14        | TRANSACTION_DT | Date Validity             |             
|  3        | 14        | ZIP_CODE       | Between 5 to 9 digits    |           
|  4        | 7         | CMTE_ID        | Empty or 9-character alpha-numeric code |
|  5        | 7         | TRANSACTION_AMT| Empty, Integer or Float  |          
|  6        | 13        | Multiple       | Multiple                 |         

## Test Values
The test values are collated in [Test-Values.pdf](Test-Values.pdf).

## Input File Considerations
The following considerations were given as part of the data problem:

### OTHER_ID
* Because we are only interested in individual contributions, we only want records that have the field, OTHER_ID, set to empty * If the OTHER_ID field contains any other value, ignore the entire record and don't include it in any calculation
    
### TRANSACTION_DT
* If TRANSACTION_DT is an invalid date (e.g., empty, malformed), you should still take the record into consideration when outputting the results of `medianvals_by_zip.txt` but completely ignore the record when calculating values for `medianvals_by_date.txt`

* The transactions noted in the input file are not in any particular order, and in fact, can be out of order chronologically
    
### ZIP_CODE
* While the data dictionary has the ZIP_CODE occupying nine characters, for the purposes of the challenge, we only consider the first five characters of the field as the zip code
* If ZIP_CODE is an invalid zipcode (i.e., empty, fewer than five digits), you should still take the record into consideration when outputting the results of `medianvals_by_date.txt` but completely ignore the record when calculating values for `medianvals_by_zip.txt`
    
### Other Considerations
* If any lines in the input file contains empty cells in the CMTE_ID or TRANSACTION_AMT fields, you should ignore and skip the record and not take it into consideration when making any calculations for the output files
* Except for the considerations noted above with respect to CMTE_ID, ZIP_CODE, TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID, data in any of the other fields (whether the data is valid, malformed, or empty) should not affect your processing. That is, as long as the four previously noted considerations apply, you should process the record as if it was a valid, newly arriving transaction. (For instance, campaigns sometimes retransmit transactions as amendments, however, for the purposes of this challenge, you can ignore that distinction and treat all of the lines as if they were new)
* For the purposes of this challenge, you can assume the input file follows the data dictionary noted by the FEC for the 2015-current election years


