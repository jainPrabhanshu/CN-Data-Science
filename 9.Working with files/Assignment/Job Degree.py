# Given File 'amazonjobsdataset.csv'
# It is a dataset including information on amazon job opening around the world from June 2011 to March 2018. This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.
# Problem Statement :
# Find the number of job openings are present if applicant have Bachelor degree?
# Print the count as Integer value
# Note : Here we will use the BASIC QUALIFICATIONS feature to find out whether bachelor degree for Job is required or not. Keywords that can be used are 'Bachelor', 'BS' and 'BA'.
# Output Format :
# Count

## Open and read data file as specified in the question
## Print the required output in given format
import csv
with open('amazon_jobs_dataset.csv') as file_obj:
    file_data = csv.DictReader(file_obj,skipinitialspace = True)
    file_list = list(file_data)
count = 0
for row in file_list:
    val = row['BASIC QUALIFICATIONS']
    if ('Bachelor' in val) or ('BA' in val) or ('BS' in val):
        count += 1
print(count)
        