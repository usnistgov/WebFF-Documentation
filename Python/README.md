# WebFF-Documentation

The Python directory contains:
- The WebFF Python module containing all Excel to XML data translator functions
- The Python data translation scripts for converting force-field data in the Excel templates to an XML document 
- The Python data translation scripts for converting force-field data in XML format to common force-field formats  

## WebFF Input

File Name | Function
--------- | --------
Class1_Excel_to_XML.py | Python script to translate data from WebFF-Class1-DataTemplate.xlsx to XML format 
Class2_Excel_to_XML.py | Python script to translate data from WebFF-Class2-DataTemplate.xlsx to XML format
CoarseGrained_Excel_to_XML.py | Python script to translate data from WebFF-CoarseGrained-DataTemplate.xlsx to XML format

## WebFF Module

File Name | Function
--------- | --------
WebFF.py | Python module containing all Excel to XML data translator functions

## WebFF Output

File Name | Function
--------- | --------
XML_to_frc.py | Python script to XML force-field data to .frc (Legacy Biosym) format 
XML_to_params.py | Python script to XML force-field data to .params (Vega) format 

