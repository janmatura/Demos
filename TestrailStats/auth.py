#
# Testrail - Testcases props distribution monitor
#
# Makes a chart of Priority/Sprint dostribution through all cases at a project
# Specify the project_id below

import testrail as tr
import pandas as pd

url = 'https://mluvii.testrail.io/'
user = 'qa@mluvii.com'
passw = 'Mluvii53533*'

client = tr.APIClient(url)
client.user = user
client.password = passw
project_id = 5  # QA_MLUVII_3.0

try:
    suitesArr = []
    suites = client.send_get(f'get_suites/{project_id}')

    for i in suites:
        suitesArr.append(i['id'])
    print(f'SuitesArray: {suitesArr};')
except: print('Suites not workin')

try:
    offset = 0
    limit = 250
    casesJson = None
    while True:

        cases = client.send_get(f'get_cases/5&suite_id=622&offset={offset}')['cases']

        if casesJson is None:
            casesJson = cases
        else:
            casesJson = casesJson + cases

        sum = len(cases)
        offset = offset + limit

        if sum != limit:
            break

except Exception as e:
    print(f'Cases API export not workin - {e}')

try:
    labels = ['0', '1', '2', '3', '4'] # Priorities
    indexes = ['1', '2', '3', '4'] # Sprints


    propDistribution = pd.DataFrame( data=None, index=indexes, columns=labels)
    for i in labels:
        propDistribution[i] = 0

    for testcase in casesJson:
        index = str(testcase['custom_sprint'])
        label = str(testcase['priority_id'])
        try:
            propDistribution.at[index, label] += 1
        except Exception as e: print(f'Counting DataFrame Values Exception: {e}')

except Exception as e:
    print(f'Dataframe creation not workin - {e}')

propDistribution = propDistribution.rename(columns={'0':'Minor', '1':'Low', '2':'Medium', '3':'High', '4':'Critical'})
propDistribution = propDistribution.rename(index={'1':'ABC', '2':'A', '3':'B', '4':'C'})


print(f'\n ================== \n Sprint / Priority distribution:\n{propDistribution}')

print(f'\n ================== \n Sum by Priority:\n{propDistribution.sum(axis=0)}')

print(f'\n ================== \n Sum by Sprints:\n{propDistribution.sum(axis=1)}')

print(f'\n ================== \n All Cases count: {len(casesJson)}')


