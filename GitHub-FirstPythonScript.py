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

#another way to import your workspace is to add an "r" in front of your directory and make the path a string by adding '', then your dont need to correct the backslash (\) to frontslash (/) or double backslash (\\).
# arcpy.env.workspace = r'C:\Users\ifeom\OneDrive - Kansas State University\Courses\6. Fall 24\GEOG728 - Python\GitHub\firstpythonscript-Iphy16\GIS Project\ExerciseData.gdb'


# Perform Geoprocessing
selectEcoregion = arcpy.management.SelectLayerByAttribute('ks_ecoregions', 'NEW_SELECTION', "US_L3NAME = 'Flint Hills'")

arcpy.analysis.Buffer('ks_ecoregions', 'ecoregionBuffer', '10 Kilometers', 'Full', 'ROUND', 'ALL')

riversClip = arcpy.analysis.Clip('ks_major_rivers', 'ecoregionBuffer','RiverClip')

# Add new field and populate attribute
arcpy.management.AddField('RiverClip', 'Type', 'TEXT', 10,'','','Type', 'NULLABLE', 'NON_REQUIRED')

arcpy.management.CalculateField('RiverClip', 'Type', "'River'", expression_type='PYTHON3')


# Calculate Stream length
## Set local variables

sumStreamLen = sumStreamLen = arcpy.gapro.SummarizeAttributes('RiverClip', 'sumRiverLen', ['Type'], [['Shape_Length', 'SUM']])
