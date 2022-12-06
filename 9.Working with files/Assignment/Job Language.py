# Given File 'amazonjobsdataset.csv'
# It is a dataset including information on amazon job opening around the world from June 2011 to March 2018. This dataset is collected using Selenium and BeautifulSoup by scraping all of the jobs for Amazon job site.
# Problem Statement :
# Among Java, C++ and Python, which of the language has more job openings in India for Bachelor Degree Holder?
# Print the Language(i.e Java,C++,Python) and number of job opening as integer value.
# Note : Here we will use the BASIC QUALIFICATIONS feature to find out whether bachelor degree for Job is required or not. Keywords that can be used are 'Bachelor', 'BS' and 'BA' and we will use the BASIC QUALIFICATIONS feature to find out whether Language is required for the job or not.Keywords that is used for language searching are 'Java','C++' or 'Python'.(There case should not be changed).
# Output Format :
# Language Count


import csv
with open('amazon_jobs_dataset.csv', encoding='utf8') as file_obj:
    file_data=csv.DictReader(file_obj, skipinitialspace=True)
    lst=list(file_data)
count=0
dic={}
dic['Java']=0
dic['C++']=0
dic['Python']=0
for row in lst:
    loc=row['location'].strip().split(",")
    a=row['BASIC QUALIFICATIONS']
    if 'Java' in a and ("Bachelor" in a or "BA" in a or "BS" in a) and (loc[0]=='IN'):
        dic['Java']+=1
    elif 'C++' in a and ("Bachelor" in a or "BA" in a or "BS" in a) and (loc[0]=='IN'):
        dic['C++']+=1
    elif 'Python' in a and ("Bachelor" in a or "BA" in a or "BS" in a) and (loc[0]=='IN'):
        dic['Python']+=1
count=0
language=""
for i in dic.keys():
    if count<dic[i]:
        count=dic[i]
        language=i
print(language, count)