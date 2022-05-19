# bdc3_data_table
Scripts for transforming the manually-scraped BDC3 

## Introduction
This script transforms a CSV of study metadata into a JSON file that populates the [BioData Catalyst Studies](https://biodatacatalyst.nhlbi.nih.gov/resources/data/studies/) or [COVID-19](https://biodatacatalyst.nhlbi.nih.gov/covid-19/) tables.

## Requirements
This repo requires Python 3.6+ and a command line tool

## Instructions

- Clone this repository onto your local machine
- bring the CSV file(s) into the `inputs` folder
- set the values for `input_filepath`, `table_type`, and `output_filepath`
- run the script at the command line with `python3 study_table.py`
