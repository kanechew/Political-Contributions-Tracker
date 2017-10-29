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
As part of Object Oriented Programming (OOP) methodology, the source code is partitioned into separate user-defined functions that are called within the 'main()' function.

### Choice of Data Structures
An important consideration for this data problem is the choice of data structures to store the variables from the input files.

Dictionaries of lists were chosen to store the relevant variables, with 'cmte_id' as the key for every dictionary to to avoid confusion.

At the same time, Dictionaries of lists provide greater flexibility and versatibility for future data processing needs. 

Since the two output files are not written in parallel, 

### Choice of Algorithm


