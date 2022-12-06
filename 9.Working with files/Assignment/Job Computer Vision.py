# Given File 'amazonjobsdataset.csv'
# It is a dataset including information on amazon job opening around the world from June 2011 to March 2018. This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.
# Problem Statement :
# What are the total number of job openings related to Computer Vision ?
# Note:For finding the job related to computer vision check the Job Title column.
# Print the count as the Integer Value
# Output Format :
# Count

import csv
with open('amazon_jobs_dataset.csv') as file_obj:
    file_data=csv.DictReader(file_obj, skipinitialspace=True)
    lst=list(file_data)
    count=0
    for row in lst:
        a=row['Title'].split()
        if 'Vision' in a:
            count+=1
print(count)

