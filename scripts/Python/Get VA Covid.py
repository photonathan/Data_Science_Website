# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 14:52:30 2021

@author: MDNat
"""

import re
import requests
import xml.etree.ElementTree as ET
from datetime import date, datetime
import pandas as pd
from getpass import getpass
from sqlalchemy import create_engine
from sodapy import Socrata
import mysql.connector
from mysql.connector import errorcode
# Test to add table to MySQL
results = client.get_all("bre9-aqqr")#, report_date = '2021-03-08')
results_df = pd.DataFrame.from_records(results)
results_df.to_sql('virginia', con=engine, index=False, if_exists='replace')
df2 = pd.read_sql('virginia', con=engine)

# Uses SodaPy
MyAppToken = Sys.getenv('VA_APP_TOKEN')
client = Socrata("data.virginia.gov", MyAppToken)
# See the datasets avaiable
client.datasets(limit=1)
all_results = client.get_all("bre9-aqqr", report_date ='2021-03-09')
arlington_results = client.get("bre9-aqqr", locality = 'Arlington')
results = client.get("bre9-aqqr")#, report_date = '2021-03-08')
results_df = pd.DataFrame.from_records(results)

all_results_df = pd.DataFrame.from_records(all_results)
arlington_results_df = pd.DataFrame.from_records(arlington_results)

# MySQL
engine = create_engine(f'mysql+mysqldb://{input("Enter username: ")}:{getpass("Enter password: ")}@localhost/covid', echo=False)
# columns = ('Report Date', 'FIPS', 'Locality', 'Virginia Health District', 'Total Cases', 'Hospitalizations', 'Deaths')
#df[["CounterID", "Name", "Latitude", "Longitude", "Region", 'RegionID']] = df[["CounterID", "Name", "Latitude", "Longitude", "Region", 'RegionID']].astype('string')

conn = engine.connect()
conn.execute("create database covid")
# Creates the table locality_arlington in the covid database, use if_exists='append' to insert new values into the table
arlington_results_df.to_sql('locality_arlington', con=engine, index=False)
# Reads the table
df2 = pd.read_sql('locality_arlington', con=engine)
results_df.to_sql('locality_arlington', con=engine, index=False)


# Regular request
url = 'https://data.virginia.gov/resource/bre9-aqqr.json'
headers = {'x-api-key': Sys.getenv('VA_APP_TOKEN')}
# parameters: {"report_date": 2021-03-09,"fips","locality","vdh_health_district","total_cases","hospitalizations","deaths"}
params = {'report_date': '2021-03-08', 'locality': 'Arlington'}
request = requests.get(url, headers=headers, params = params)
request.text
# Not formatted properly, this step is easier using SodaPy
df = pd.DataFrame.from_records(request.text)


def GetVACovidData():
    requestData = {'method': 'report_date'}
        #TODO: Add except for non-200 response
    # Convert response to a string
    xml_data = response.text
    # Clean the data
    clean_xml_data = re.sub(r'[\n|\t]', '', xml_data)
    # Cast the string to an XML element
    tree = ET.fromstring(clean_xml_data)
    # Create the empty dictionary to put the data in
    #CountInDateRangeDict = {}
    # Parse the GetCountInDateRange XML file for the count and date and save CountInDateRangeDict
    for type_tag in tree.findall('count'):
        count = type_tag.get('count')
        date = type_tag.get('date')
        # Converts counter date to a datetime object
        date = datetime.strptime(date, '%m/%d/%Y').date()
        direction = type_tag.get('direction')
        #name = type_tag.get('name')
        single_tuple = (counterID, date, direction, count)
        CountInDateRangeList.append(single_tuple)
        #CountInDateRangeDict[date] = count
        #print(count + ' ' + date + ' ' + counterID)
    return CountInDateRangeList

