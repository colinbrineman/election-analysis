# TITLE
Module 3 Challenge: Using Python to Audit Election Results

## AUTHOR
Colin Brineman, M.A.

## OVERVIEW

### Primary objective
The primary objective of the Module 3 challenge was to help Tom, a Colorado Board of Elections employee, to write a Python script to audit results from a recent U.S. Congress election in Colorado, so that the election commission can certify the results of the election.

### Secondary objective
The secondary objective of this challenge was to help Tom to provide Seth, his manager,  with a Python script that can be easily repurposed to audit other elections in the state of Colorado, from the local level up to U.S. Senate races.

### Skills employed
The skills employed in the course of this challenge included but were not limited to:
- cloning and updating a Github repository from the command line;
- writing a Python script in Visual Studio Code; and
- learning how to work with different data types, create decision and repetition statements, and read and write files in Python.

### Deliverables
The deliverables for this challenge were:
- a Python script to audit election data,
- a properly formatted election results text file, and
- a written analysis of the findings of the audit.

## RESULTS
See: [Colorado Congressional Election Results](/resources/election_analysis.txt).

### Total Results
- Total Votes: 369,711

### County Results
- Jefferson: 10.5% (38,855)
- Denver: 82.8% (306,055)
- Arapahoe: 6.7% (24,801)

### Largest County Results
- Largest County: Denver
- Largest County Votes: 306,055
- Largest County Percentage: 82.8%

### Candidate Results
- Charles Casper Stockham: 23.0% (85,213)
- Diana DeGette: 73.8% (272,892)
- Raymon Anthony Doane: 3.1% (11,606)

### Winning Candidate Results
- Winning Candidate: Diana DeGette
- Winning Candidate Votes: 272,892
- Winning Candidate Percentage: 73.8%

## ANALYSIS

## Using Python to audit future elections
The analyst could tell Tom and Seth to relay to the election commission that there are at least 3 advantages to using this Python script to audit elections, as opposed to the common practice of using Excel:
1. a Python script precludes the auditor from opening the election data spreadsheet in a spreadsheet editor, thus minimizing the likelihood of the auditor accidentally corrupting the underlying data;
2. a Python script can be easily modified to audit multiple elections, simply by changing the directories of the election data spreadsheet and election analysis text files, that is to say, by altering only two lines of code; and
3. a Python script reads over a data spreadsheet to retrieve unique values for fields such as counties and candidates, as well as the values for each row, and so the analyst does not even need to examine the election data spreadsheet, except to ensure it has not been corrupted and to identify column locations, thus minimizing the likelihood of the auditor accidentally ommitting values from the audit.

## Proposals for modifying Python audit script
The script could be modified in at least 2 ways:
1. adding a section presenting the results for each candidate in each county,
2. removing redundant values removing the largest county and winning candidate results sections, instead identifying the relevant county and candidate with an asterisk and a note.
