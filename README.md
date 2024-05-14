# SmartSearch
This project has been developed as part of the course "Advanced Software Engineering" at the BHT.
It is a commandline tool containing the basic functionality of searching for one or more search patterns inside a raw 
text string, a text file or a directory containing several txt-files.
As can be seen in the UML diagrams and the DDD files, the vision of the project is to provide a tool that can be used
to search for information in a smart way by using different search algorithms and NLP techniques.

This tool has been developed and tested using Python 3.9.

## Installation
To install this commandline tool, execute the following commands in your terminal:

```bash
git clone https://github.com/bogdankostic/SmartSearch.git
cd SmartSearch
sudo -H ./install.sh
````
## Usage
After installation, you can use this tool directly from the commandline by executing the following command:

```bash
 search [-h] [-n] [-i] SEARCH_PATTERN [SEARCH_PATTERN ...] TEXT_INPUT
```

**Positional Arguments:**
- SEARCH_PATTERN – *Search pattern to search for in the provided text inputs*
- TEXT_INPUT – *Raw text, text file or directoy containing .txt-files*

**Optional Arguments:**
- -h / --help – *Show help message explaining how to use this tool*
- -n / --naive – *Use naive string matching algorithm instead of Boyer-Moore algorithm*
- -i / --case-insensitive – *Perform case-insensitive search*

### Output
Each match is printed on a new line with the following tab-seperated formats:

#### Format for single text files and raw text input
SEARCH_PATTERN \t POSITION_IN_TEXT/FILE

#### Format for directories containing txt-files
FILE_NAME \t SEARCH_PATTERN \t POSITION_IN_FILE


## Software Engineering
### 1) Git

Throughout the project, Git and GitHub were used as tools for version control.
The commit history can be found [here](https://github.com/bogdankostic/SmartSearch/commits/main/).

### 2) UML

The directory [`uml`](https://github.com/bogdankostic/SmartSearch/tree/main/uml) contains the following UML
diagrams as images and PlantUML files:

- Class Diagram
- Sequence Diagram
- Component Diagram

### 3) Domain Driven Design

The event storming, the core domain diagram, and the relationship mapping can be found in the
[`domain_driven_design.pdf`](https://github.com/bogdankostic/SmartSearch/blob/main/domain_driven_design.pdf) file.

### 4) Metrics

Code Metrics are tracked on [Coveralls](https://coveralls.io/github/bogdankostic/SmartSearch) for test coverage
and [SonarCloud](https://sonarcloud.io/project/overview?id=bogdankostic_SmartSearch) for code quality.

#### Metric badges:

[![Coverage Status](https://coveralls.io/repos/github/bogdankostic/SmartSearch/badge.svg?branch=main)](https://coveralls.io/github/bogdankostic/SmartSearch?branch=main)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=bogdankostic_SmartSearch&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=bogdankostic_SmartSearch)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=bogdankostic_SmartSearch&metric=bugs)](https://sonarcloud.io/summary/new_code?id=bogdankostic_SmartSearch)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=bogdankostic_SmartSearch&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=bogdankostic_SmartSearch)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=bogdankostic_SmartSearch&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=bogdankostic_SmartSearch)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=bogdankostic_SmartSearch&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=bogdankostic_SmartSearch)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=bogdankostic_SmartSearch&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=bogdankostic_SmartSearch)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=bogdankostic_SmartSearch&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=bogdankostic_SmartSearch)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=bogdankostic_SmartSearch&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=bogdankostic_SmartSearch)

### 5) Clean Code Development

Examples of clean code development principles used in the project:

- Don't Repeat Yourself: The project uses functions and classes to avoid code duplication.  
  [**Example**](https://github.com/bogdankostic/SmartSearch/blob/5831045bd9997aa53ea210123ad02be4a78dd47d/src/matchers/base.py#L25):
  Input validation in `BaseMatcher`.
- Usage of type hints to specify the types of function arguments and return values.  
  [**Example**](https://github.com/bogdankostic/SmartSearch/blob/5831045bd9997aa53ea210123ad02be4a78dd47d/src/matchers/boyer_moore.py#L21)
- Usage of docstrings to document functions and classes.  
  [**Example**](https://github.com/bogdankostic/SmartSearch/blob/5831045bd9997aa53ea210123ad02be4a78dd47d/src/matchers/naive.py#L18)
- Usage of meaningful variable and function names.  
  [**Example**](https://github.com/bogdankostic/SmartSearch/blob/de067c87c02faebf42dcb562c5f0f391dcbe2ab2/src/matchers/boyer_moore.py#L50)
- Short functions that do one thing.  
  [**Example**](https://github.com/bogdankostic/SmartSearch/blob/5831045bd9997aa53ea210123ad02be4a78dd47d/src/matchers/boyer_moore.py#L76)

My personal clean code development cheat sheet can be found in
the [`clean_code_cheat_sheet.md`](https://github.com/bogdankostic/SmartSearch/blob/main/clean_code_cheat_sheet.md) file.

### 6 & 7) Build & Continuous Delivery

The project uses GitHub Actions for continuous integration and delivery. The workflow can be found
[here](https://github.com/bogdankostic/SmartSearch/blob/main/.github/workflows/build.yml). The workflow is triggered
on every push to the main branch and runs the tests, measures the test coverage, and uploads the coverage report to
Coveralls.

### 8) Unit Tests

The unit tests for the project can be found in the [`test`](https://github.com/bogdankostic/SmartSearch/tree/main/test)
directory.
The tests can be executed by running the following command:

```
pytest test/
```

### 9) IDE

Throughout the project, the PyCharm IDE was used. My favorite key shortcuts are:

- <kbd>⌘ Command</kbd> + <kbd>⇧ Shift</kbd> + <kbd>F</kbd>: Search in all files
- <kbd>⌘ Command</kbd> + <kbd>⇧ Shift</kbd> + <kbd>R</kbd>: Replace in all files
- <kbd>⌘ Command</kbd> + <kbd>/</kbd>: Comment/uncomment code
- <kbd>⌘ Command</kbd> + <kbd>K</kbd>: Commit changes
- <kbd>⌘ Command</kbd> + <kbd>⇧ Shift</kbd> + <kbd>K</kbd>: Push changes


### 10) Domain Specific Language

As the main use case for the SmartSearch application is to find information by executing search queries,
the Domain Specific Langauge for the SmartSearch project could be inspired by SQL or a similar query language.
An example of a query that would use most of the features of the DSL is:

```sql
SELECT 
    document
FROM 
    document_idx
WHERE 
    exact_search('software engineering')
    AND semantic_search('How to construct a DSL?', similarity = 0.8)
    AND meta.year >= 2021 
```

This query would search for documents that contain the exact phrase 'software engineering',
documents that are semantically similar to 'How to construct a DSL?' with a similarity threshold of 80%,
and documents that have the meta field `'year'` greater than or equal to 2021.

### 11) Functional Programming
The project follows aspects of functional programming, for example:
- Final data structures: data structures used are immutable, for example tuples (see [here](https://github.com/bogdankostic/SmartSearch/blob/90e9db1ce8db1d9f47793ab3f73deb82c3686996/src/matchers/boyer_moore.py#L47)).
- Side-effect free functions: functions are designed to be side-effect free, for example the `search` function in the `NaiveMatcher` class (see [here](https://github.com/bogdankostic/SmartSearch/blob/90e9db1ce8db1d9f47793ab3f73deb82c3686996/src/matchers/naive.py#L17)).
- Anonymous functions: lambda functions are used to define a `defaultdict` (see [here](https://github.com/bogdankostic/SmartSearch/blob/90e9db1ce8db1d9f47793ab3f73deb82c3686996/src/matchers/boyer_moore.py#L87)).

There was no need for higher-order functions and using functions as parameters and return values in the project, so I 
created the file [`functional_programming.py`](https://github.com/bogdankostic/SmartSearch/blob/main/functional_programming.py)
to demonstrate these aspects of functional programming.
