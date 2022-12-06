# Given File 'amazonjobsdataset.csv'
# It is a dataset including information on amazon job opening around the world from June 2011 to March 2018. This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.
# Problem Statement :
# Find the country does Amazon need the most number of Java Developer?
# Print the Country(Country Shortcut as given in Dataset) and number of job opening as integer value
# Note :Here we will use the BASIC QUALIFICATIONS feature to find out whether Java is required for the job or not.Keyword is used is 'Java'.(Here case should not be changed).


# Output Format :


# Country NumberofJobs
# For example : US 40


import csv
with open('amazon_jobs_dataset.csv', encoding='utf8') as file_obj:
    file_data=csv.DictReader(file_obj, skipinitialspace=True)
    lst=list(file_data)
    dic={}
    for row in lst:
        a=row['BASIC QUALIFICATIONS']
        b=row['location'].split(",")[0]
        if "Java" in a:
            if b in dic.keys():
                dic[b]+=1
            else:
                dic[b]=1
                
count=0
country=""
for i in dic:
    if dic[i]>count:
        count=dic[i]
        country=i
print(country, count)