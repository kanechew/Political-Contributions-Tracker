# Technical Notes

## Table of Contents
1. [Introduction](TECHNICALNOTES.md#introduction)
2. [Naming Convention](TECHNICALNOTES.md#naming-convention)
3. [Design Considerations](TECHNICALNOTES.md#design-considerations)
    1. [Packages](TECHNICALNOTES.md#packages)
    2. [Abstraction & Encapsulation](TECHNICALNOTES.md#abstraction-&-encapsulation)
    3. [Choice of Data Structures](TECHNICALNOTES.md#choice-of-data-structures)
    4. [Choice of Algorithm](TECHNICALNOTES.md#choice-of-algorithm)
4. [Input Considerations](TECHNICALNOTES.md#input-considerations)
5. [Computational Efficiency](TECHNICALNOTES.md#computational-efficiency)
6. [Alternative Implementation](TECHNICALNOTES.md#alternative-implementation)

## Introduction
This document describes some of the key programming methodology and philosphy that are espoused and implemented in the python source code.

## Naming Convention
Where applicable, naming convention for variables and functions adhere to PEP 8 - Style Guide for Python Code

Inline Comments and docstrings are appended to aid code readability.

## Design Considerations
There are several design considerations made during the formulation of the data problem and the eventual code implementation.

### Packages
Absolute imports were used where applicable.

### Abstraction & Encapsulation
As part of Object Oriented Programming (OOP) methodology, the source code is partitioned into separate user-defined functions that are called within the `main()` function.

Since the two output files are not written in parallel, each output file can be written in separate functions. This aids in the debugging and testing of code to verify output file 1 and 2 indepedently.

### Choice of Data Structures
An important consideration for this data problem is the choice of data structures to store the variables from the input files.

Dictionaries of lists were chosen to store the relevant variables, with `cmte_id` as the key for every dictionary to to avoid confusion.

At the same time, Dictionaries of lists provide greater flexibility and versatibility for future data processing needs. 

Two dictionaries of dictionaries were used to store the total and median transaction for each unqiue pair of `cmte_id` and `transaction_dt`

### Choice of Algorithm
For the extraction of 5 relevant variable values `CMTE_ID`, `ZIP_CODE`, `TRANSACTION_DT`, `TRANSACTION_AMT`and `OTHER_ID`, it was tempting to use regular expressions to parse the lines of the inout file.

But since each line of text contains a fixed number of pipe delimiters, it is efficient to use simple string operations to extract substrings at fixed/regular intervals.

## Input Considerations

## Computational Efficiency

## Alternative Implementation



