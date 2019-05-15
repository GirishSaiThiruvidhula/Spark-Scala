import os
import sys
import xml.etree.ElementTree as ET

#xml_str='<xml><a id="10"><c><b>10</b></c></a><a id="20"><b>10</b></a></xml>'
xml_str=""

root=ET.fromstring(xml_str)
def add_attrib(data,temp):
	for key in data.keys():
		temp[key]=data[key]
	
	return temp

def parse_xml(root):
	d={}
	for child in root:
		if(len(child.getchildren())):
			temp=parse_xml(child)
			if(len(child.attrib.keys())>0):
				temp=add_attrib(child.attrib,temp)
			if(child.tag in d.keys()):
				if(isinstance(d[child.tag],dict)):
					d[child.tag]=[d[child.tag],temp]
				elif(isinstance(d[child.tag],list)):
				   d[child.tag].append(temp)
			else:
				d[child.tag]=temp
			
		else:
			if(child.tag in d.keys()):
				if(isinstance(d[child.tag],str)):
					d[child.tag]=[d[child.tag],child.text]
				if(isinstance(d[child.tag],list)):
					d[child.tag].append(child.text)
			else:
				d[child.tag]=child.text
	return d

dict=parse_xml(root)
print(dict)
