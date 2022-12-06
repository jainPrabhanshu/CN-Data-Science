# Given File amazonjobsdataset.csv (Please check Dataset preview name)
# It is a dataset including information on amazon job opening around the world from June 2011 to March 2018. This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.
# Problem Statement :
# Find number of job openings in Bangalore,IN and in Seattle,US?
# Print the Number of Job opening in Bangalore and Seattle as Integer value.
# Output Format :
# CountBangalore CountSeattle

import csv
countBangalore=0
countSeattle=0
with open('amazon_jobs_dataset.csv') as file_obj:
    file_data=csv.DictReader(file_obj, skipinitialspace = True)
    file_list=list(file_data)
    
    
    for row in file_list:
        add=row['location'].split()
        
        if ('Bangalore' in add):
            countBangalore+=1
            
        if ('Seattle' in add):
            countSeattle+=1         
print(countBangalore,countSeattle)

