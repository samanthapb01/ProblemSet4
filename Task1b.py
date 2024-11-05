#Import arc.py
import arcpy

# Set local variables
in_features = "V:/ENV859_PS4/Data/streams.shp"
out_features = "V:/ENV859_PS4/Scratch/StrmBuff1km.shp"

# Buffer the stream features
buff_dist = "1000 meters"
arcpy.Buffer_analysis(in_features,out_features,buff_dist,'','','ALL')

#Display messages, warnings, and errors
print(arcpy.GetMessages())