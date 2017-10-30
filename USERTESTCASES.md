# User Test Cases

## Table of Contents
1. [Introduction](USERTESTCASES.md#introduction)
2. [Construction](USERTESTCASES.md#construction)
3. [Path](USERTESTCASES.md#path)
4. [Test Validation](USERTESTCASES.md#test-validation)
5. [Test Variables](USERTESTCASES.md#test-variables)
6. [Test Values](USERTESTCASES.md#test-values)

## Introduction
This document describes the extended user test cases for the validation of the python program.

## Construction
Except for Test Case 6, each test case focuses on one input file consideration.

Test Case 6 specifically tests the functionality of the program to write the second output file accurately. 

## Path
The input file and expected output files for each test case are stored in separate folders within the `insight_testsuite` folder.

### Example
Files for Test Case 1 are found in './insight_testsuite/tests/usertest_1'.

## Test Validation
The test cases are validated by executing the 'run_tests.sh' file, located in `./insight_testsuite`.

## Test Variables

| Test Case | Row Count | Test Variables | Input Consideration      |
| ----------| ----------| -------------- | -------------------------| 
|  1        | 7         | other_id       | Empty or Not             |           
|  2        | 14        | trans_dt       | Date Validty             |             
|  3        | 14        | zip_code       | Between 5 to 9 digits    |           
|  4        | 7         | cmte_id        | Empty or 9-character alpha-numeric code |
|  5        | 7         | trans_amt      | Empty, Integer or Float  |          
|  6        | 13        | Multiple       | Multiple                 |         

## Test Values
The test values are collated in [Test Values](test-values.pdf)
