# Given File 'amazonjobsdataset.csv'
# It is a dataset including information on amazon job opening around the world from June 2011 to March 2018. This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.
# Problem Statement :
# Find the number of job openings in Canada?
# Print the count as the Integer Value
# Note: Here you should analyse the country code in location feature.( you can use dictionary for analyse part ).
# Output Format :
# Count

## Open and read data file as specified in the question
## Print the required output in given format
import csv
count = 0
with open('amazon_jobs_dataset.csv') as file_obj:
    file_data = csv.DictReader(file_obj,skipinitialspace = True)
    file_list = list(file_data)

for row in file_list:
    add = row['location'].split(",")
        
    # if ('CA' in add):
    if row['location'].startswith("CA"):
        count+=1
print(count)    