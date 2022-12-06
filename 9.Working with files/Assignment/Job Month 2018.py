# Given File 'amazonjobsdataset.csv'
# It is a dataset including information on amazon job opening around the world from June 2011 to March 2018. This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.
# Problem Statement :
# Find the month having most job openings in Year 2018 ?
# Print the month (Month Name i.e January, February, March) and Number of job opening as Integer Value
# Output Format :
# MonthName Count

## Open and read data file as specified in the question
## Print the required output in given format
import csv
count = 0
with open('amazon_jobs_dataset.csv') as file_obj:
    file_data = csv.DictReader(file_obj,skipinitialspace = True)
    file_list = list(file_data)
    l = []
    for row in file_list:
        val = row['Posting_date'].split()
        if '2018' in val:
            l.append(val)

dict = {}
for i in l:
    if i[0] in dict:
        dict[i[0]] += 1
    else:
        dict[i[0]] = 1
        
count = 0
monthName = 'January'
for i in dict:
    if dict[i] > count:
        count = dict[i]
        monthName = i
print(monthName,count)