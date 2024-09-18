#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File Name: River Length Calculation
    Author: Ifeoma Okonye
    Description: Calculate total stream length in specifed ecoregion
    Date Created: 09/11/2024
    Python Version: 3.9.16
"""

# Import arcpy module and allow overwrites
import arcpy
arcpy.env.overwriteOutput = True

# Set current workspace
arcpy.env.workspace = "C:\\Users\\ifeom\\OneDrive - Kansas State University\Courses\\6. Fall 24\\GEOG728 - Python\\GitHub\\firstpythonscript-Iphy16\\GIS Project\\ExerciseData.gdb"


# Perform Geoprocessing
selectEcoregion = arcpy.management.SelectLayerByAttribute('ks_ecoregions', 'NEW_SELECTION', "US_L3NAME = 'Flint Hills'")

# Calculate Buffer
arcpy.analysis.Buffer(selectEcoregion, 'ecoregionBuffer', '10 Kilometers', 'Full', 'ROUND', 'ALL')

# Clip Features
arcpy.analysis.Clip('ks_major_rivers', 'ecoregionBuffer','RiverClip')

# Add new field and populate attribute
arcpy.management.AddGeometryAttributes('RiverClip', 'LENGTH', 'MILES_US')

arcpy.management.AddField('RiverClip', 'Type', 'TEXT', 10,'','','Type', 'NULLABLE', 'NON_REQUIRED')
arcpy.management.CalculateField('RiverClip', 'Type', "'River'", expression_type='PYTHON3')

# Calculate Stream length
arcpy.gapro.SummarizeAttributes('RiverClip', 'sumRiverLen', ['Type'], [['LENGTH', 'SUM']]) #when there are square brackets, its a list



#################################################################################################################################
# Method 2
#################################################################################################################################

# Import arcpy module and allow overwrites
#import arcpy
#arcpy.env.overwriteOutput = True

# arcpy.env.workspace = r'C:\Users\ifeom\OneDrive - Kansas State University\Courses\6. Fall 24\GEOG728 - Python\GitHub\firstpythonscript-Iphy16\GIS Project\ExerciseData.gdb'


## Option 2 if i dont want to create a new variable
# Perform Geoprocessing
#arcpy.Select_analysis('ks_ecoregions', 'outSelect', "US_L3NAME = 'Flint Hills'")

# Calculate Buffer
# arcpy.analysis.Buffer(selectEcoregion, 'ecoregionBuffer', '10 Kilometers', 'Full', 'ROUND', 'ALL')

# Clip Features
# arcpy.analysis.Clip('ks_major_rivers', 'ecoregionBuffer','RiverClip')

# Calculate Length in Miles
# arcpy.management.CalculateField('RiverClip', 'Length_Mi', '!Shape_Length!*0.000621371', "", "", "Float")

# Summarize Length in Miles
# arcpy.Statistics_analysis('RiverClip', "outStats1", [["Length_Mi", "SUM"]])
