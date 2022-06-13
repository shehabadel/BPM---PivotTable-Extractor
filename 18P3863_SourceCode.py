#!/usr/bin/env python
# coding: utf-8

# In[6]:


from xml.etree import ElementTree
import csv

# PARSE XML
xml = ElementTree.parse("D:\\nasa-cev-1-10-single-trace.xml")
root = xml.getroot()
traces = root.findall("trace")
# CREATE CSV FILE
csvfile = open("data.csv",'w',encoding='utf-8')
csvfile_writer = csv.writer(csvfile)

# ADD THE HEADER TO CSV FILE
csvfile_writer.writerow(["filename","conceptName","timestamp","nanotime"])

for trace in traces:
    
    for event in trace.findall("event"):
    
        if(event):
       
            timestamp = event.find('date').attrib['value']
            conceptName = event.find('.//string[@key="concept:name"]').attrib['value']
            filename = event.find('.//string[@key="apploc:filename"]').attrib['value']
            nanotime = event.find('.//string[@key="apprun:nanotime"]').attrib['value']
            csv_line = [filename,conceptName, timestamp,nanotime]
            print(csv_line)
            csvfile_writer.writerow(csv_line)
csvfile.close()


# In[ ]:





# In[ ]:




