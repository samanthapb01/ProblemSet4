#Import arc.py
import arcpy

#Set environment and overwrite ability
arcpy.env.workspace = "V:/ENV859_PS4/Data"
arcpy.env.overwriteOutput = True

# Set local variables
in_features = "Roads.shp"

#Multi-value string
road_class_string = "0;201;203"
road_class = road_class_string.split(";")

#for loop
for roadtype in road_class:
    where_clause = "ROAD_TYPE = "+roadtype
    out_features = "V:/ENV859_PS4/Scratch/road_"+roadtype+".shp"
    arcpy.Select_analysis(in_features,out_features,where_clause)