#Import arc.py
import arcpy

#Set environment and overwrite ability
arcpy.env.workspace = "V:/ENV859_PS4/Data"
arcpy.env.overwriteOutput = True

# Set local variables
in_features = "streams.shp"
out_features = arcpy.GetParameterAsText(1)

# Buffer the stream features
buff_dist = arcpy.GetParameterAsText(0)+" meters"
arcpy.Buffer_analysis(in_features,out_features,buff_dist,'','','ALL')

#Display messages, warnings, and errors
print(arcpy.GetMessages())