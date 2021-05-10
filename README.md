# Election Analysis

## Project Overview
A Colorado Board of Election employee provided election data and asked for an 
audit with the following tasks to be completed.

1. Calculate the total number of votes cast.
1. Get a comlete list of candidates who received votes.
1. Calculate the total nmber of votes each candidate received.
1. Calculate the percentage of votes each candidate received.
1. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.1, Visual Studio Code 1.55.0

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.

- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
    
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
    

## Challenge Overview
The challege assignment was to add an analysis of the data on the 
county level. The county results needed to include:
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

The challenge included three deliverables:
- Deliverable 1: The Election Results Printed to the Command Line
- Deliverable 2: The Election Results Saved to a Text File
- Deliverable 3: A written Analysis of the Election Audit (README.md)


## Challenge Summary
The analysis of the election county data shows that:
- Jefferson had 10.5% of the vote and 38,855 number of votes.
- Denver had 82.8% of the vote and 306,055 number of votes.
- Arapahoe had 6.7% of the vote and 24,801 number of votes.
- Denver was the county witht the highest turnout.

The analysis for the county data was performed by utiizing "for loops" and "if statements". Below is how the code was organized:


![Code for County Analyis](https://github.com/ClayMack/Election_Analysis/blob/main/Resources/VS%20Code%20screenshot.png)




Deliverable 1:


![Deliverable 1 Screenshot](https://github.com/ClayMack/Election_Analysis/blob/main/Resources/Challenge%20Deliverable%201.png)

Deliverable 2:


![Deliverable 2 Screenshot](https://github.com/ClayMack/Election_Analysis/blob/main/Resources/Challenge%20Deliverable%202.png)


## Comments: 

This specific analysis was only for the three unique counties and candidates 
that were provided. This script can be used for any election race over multiple 
counties.  For example, if you wanted to do the entire state of Colorado, all 
that would be required is upating the spreadsheet in the resources folder with 
all county and candidate data. This would only work for elections that have
candidates running in the same race, e.g. Governer, Senate, State Rep. race. 
The county data analysis did not measure county turnout as a percent of registered voters. 
It was a measure of the number of votes by county compared to all votes in the analysis 

