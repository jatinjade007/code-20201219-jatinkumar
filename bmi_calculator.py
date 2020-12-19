"""
bmi_calculator.py - bmi calculator assignment

Copyright (c) 2019-2020, Localytee, LLC

modification history
--------------------
01a,19dec20,jatin written

DESCRIPTION
This file contains assignment of BMI Calculator
"""

import os
import json

JSON_DATA = [
    {"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
    { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
    { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
    { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
    ]

"""
********************************************************************************
*
* convertCmToM - Helps to convert cm to m.
* 
* This function will helps to convert cm to m.
*
* RETURNS: Height in m.
*
* ERRNO: N/A
*
* SEE_ALSO: N/A.
"""    
def convertCmToM(heightInCm):
    heightInM = heightInCm/100
    return heightInM

"""
********************************************************************************
*
* bmiDataGet - Helps to get BMI Category and Health Risk.
* 
* This function will helps to get BMI Category and Health Risk via BMI.
*
* RETURNS: bmiCategory, healthRisk
*
* ERRNO: N/A
*
* SEE_ALSO: N/A.
"""    
def bmiDataGet(bmi):
    bmiCategory = None
    healthRisk = None
    if bmi <= 18.4:
        bmiCategory = "Underweight"
        healthRisk = "Malnutrition risk"
    elif (bmi >= 18.5 and bmi <= 24.9):
        bmiCategory = "Normal weight"
        healthRisk = "Low risk"
    elif (bmi >= 25 and bmi <= 29.9):
        bmiCategory = "Overweight"
        healthRisk = "Enhanced risk"
    elif (bmi >= 30 and bmi <= 34.9):
        bmiCategory = "Moderately obese"
        healthRisk = "Medium risk"
    elif (bmi >= 35 and bmi <= 39.9):
        bmiCategory = "Severely obese"
        healthRisk = "High risk"
    elif bmi >= 40:
        bmiCategory = "Very severely obese"
        healthRisk = "Very high risk"
    return bmiCategory, healthRisk

"""
********************************************************************************
*
* bmiCalculator - Helps to calculate bmi.
* 
* This function will helps to calculate bmi.
*
* RETURNS: JSON DATA with 3 new added coloumns.
*
* ERRNO: N/A
*
* SEE_ALSO: N/A.
"""    
def bmiCalculator(JSON_DATA):
    totalOverWeightPeople = 0
    for data in JSON_DATA:
        heightInM = convertCmToM(data["HeightCm"])
        bmi = data["WeightKg"] / (heightInM * heightInM)
        bmiCategory, healthRisk = bmiDataGet(bmi)
        if bmiCategory == "Overweight":
            totalOverWeightPeople += 1
        data["Bmi"] = round(bmi, 1)
        data[" BmiCategory"] = bmiCategory
        data["HealthRisk"] = healthRisk
    
    print (JSON_DATA)
    print ("Total number of overweight people :: " + str(totalOverWeightPeople))
    return JSON_DATA

"""
********************************************************************************
*
* jsonDataFromFiles - Helps to read and write json files.
* 
* This function will helps to read and write json files.
*
* RETURNS: N/A
*
* ERRNO: N/A
*
* SEE_ALSO: N/A.
"""    
def jsonDataFromFiles():
    root = os.getcwd()
    for path, subdirs, files in os.walk(root):
        for name in files:
            filename, extension = os.path.splitext(name)
            if extension == '.json':
                # Opening JSON file
                f = open(root+'/'+name, 'r+')
                data = json.load(f)
                print (data)
                modified_data = bmiCalculator(data)

                f = open(root+'/'+name, 'w')
                json.dump(modified_data, f)

jsonDataFromFiles()