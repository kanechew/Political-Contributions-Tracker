# Technical Notes

## Table of Contents
1. [Introduction](README.md#introduction)
2. [Naming Convention](README.md#challenge-summary)
3. [Design Considerations](README.md#details-of-challenge)
4. [](README.md#input-file)
5. [Output files](README.md#output-files)
6. [Example](README.md#example)
7. [Writing clean, scalable and well-tested code](README.md#writing-clean-scalable-and-well-tested-code)
8. [Repo directory structure](README.md#repo-directory-structure)
9. [Testing your directory structure and output format](README.md#testing-your-directory-structure-and-output-format)
10. [Instructions to submit your solution](README.md#instructions-to-submit-your-solution)
11. [FAQ](README.md#faq)

## Introduction


## Naming Convention
Where applicable, naming convention for variables and functions adhere to PEP 8 - Style Guide for Python Code

Inline Comments and docstrings are appended to aid code readability.

## Design Considerations

### Packages
Absolute imports were used where applicable.

### Abstraction & Encapsulation
As part of Object Oriented Programming (OOP) methodology, the source code is partitioned into separate user-defined functions that are called within the `main()` function.

Since the two output files are not written in parallel, each output file can be written in separate functions. This aids in the debugging and testing of code to verify output file 1 and 2 indepedently.

### Choice of Data Structures
An important consideration for this data problem is the choice of data structures to store the variables from the input files.

Dictionaries of lists were chosen to store the relevant variables, with `cmte_id` as the key for every dictionary to to avoid confusion.

At the same time, Dictionaries of lists provide greater flexibility and versatibility for future data processing needs. 

Two dictionaries of dictionaries were used to store the total and median transaction for each unqiue pair of 'cmte_id' and 'transaction_dt'

### Choice of Algorithm
For the extraction of 5 relevant variable values 'CMTE_ID, ZIP_CODE, TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID', it was tempting to use regular expressions to parse the lines of the inout file.

But since each line of text contains a fixed number of pipe delimiters, it is efficient to use simple string operations to extract substrings at fixed/regular intervals.

## Input Considerations

## Computational Efficiency

## Database Implementation



