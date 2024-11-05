#Import arc.py
import arcpy

#Set environment and overwrite ability
arcpy.env.workspace = "V:/ENV859_PS4/Data"
arcpy.env.overwriteOutput = True

# Set local variables
in_features = "streams.shp"

#Iterate through for loop
for distance in range(100,600,100):
    buff_dist = str(distance)+" meters"
    out_features = "V:/ENV859_PS4/Scratch/buff_"+str(distance)+"m.shp"
    arcpy.Buffer_analysis(in_features,out_features,buff_dist,'','','ALL')

#Display messages, warnings, and errors
print(arcpy.GetMessages())