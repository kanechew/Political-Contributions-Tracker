# Technical Notes

## Table of Contents
1. [Introduction](TECHNICALNOTES.md#introduction)
2. [Naming Convention](TECHNICALNOTES.md#naming-convention)
3. [Design Considerations](TECHNICALNOTES.md#design-considerations)
    1. [Packages](TECHNICALNOTES.md#packages)
    2. [Abstraction & Encapsulation](TECHNICALNOTES.md#abstraction-&-encapsulation)
    3. [Choice of Data Structures](TECHNICALNOTES.md#choice-of-data-structures)
    4. [Choice of Algorithm](TECHNICALNOTES.md#choice-of-algorithm)
4. [Computational Efficiency](TECHNICALNOTES.md#computational-efficiency)
5. [Alternative Implementation](TECHNICALNOTES.md#alternative-implementation)

## Introduction
This document describes some of the key programming methodology and philosphy that are espoused and implemented in the python source code.

## Naming Convention

* Where applicable, naming convention for variables and functions adhere to PEP 8 - Style Guide for Python Code
* Inline Comments and docstrings are appended to aid code readability

## Design Considerations
There are several design considerations made during the formulation of the data problem and the eventual code implementation.

### Packages
* Absolute imports were used where applicable.

### Abstraction & Encapsulation
As part of Object Oriented Programming (OOP) methodology, the source code is partitioned into separate user-defined functions that are called within the `main()` function.

Since the two output files are not written in parallel, each output file can be written in separate functions. This aids in the debugging and testing of code to verify output file 1 and 2 indepedently.

### Choice of Data Structures
An important consideration for this data problem is the choice of data structures to store the variables from the input files.

Dictionaries of lists were chosen to store the relevant variables, with `cmte_id` as the key for every dictionary to avoid confusion.

At the same time, Dictionaries of lists provide greater flexibility and versatibility for future data processing needs. 

Two dictionaries of dictionaries were used to store the total and median transaction for each unqiue pair of `cmte_id` and `transaction_dt`.

### Choice of Algorithm
For the extraction of 5 relevant variable values `CMTE_ID`, `ZIP_CODE`, `TRANSACTION_DT` and `TRANSACTION_AMT`, it was tempting to use regular expressions to parse the lines of the inout file.

But since each line of text contains a fixed number of pipe delimiters, it is efficient to use simple string operations to extract substrings at fixed/regular intervals.

## Computational Efficiency
Though beyond the scope of this data problem, it is important to consider the performance(speed) and efficiency(resource utilization) of the algorithm that is implemented as the size of the dataset grows. 

For example, the size of the `itcont.txt` file from the 2016 archives is 3.56 GB and comprises of 7225 lines of records.

## Alternative Implementation
As the size of the dataset grows and the number of users increases, it might be advantageous to consider writing the data from the input file into a SQL database.

The process of database normalization will greatly reduce data redundancy and improve data integrity.

This is demonstrated by [PCDatabase.db](PCDatabase.db), which is populated by the `itcont.txt` file from User Test Case 6. In this SQL database, There are 4 separate tables. The first 3 tables store the unique values for `CMTE_ID`, `ZIP_CODE` and `TRANSACTION_DATE`. The fourth table stores each transaction as a new record. By use of foreign keys, the tables can be linked together to display relevant data to appropiate users.  



