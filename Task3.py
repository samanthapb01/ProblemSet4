#Import arc.py and sys
import arcpy
import sys

#Set environment and overwrite ability
arcpy.env.workspace = "V:/ENV859_PS4/Data"
arcpy.env.overwriteOutput = True

#Check product version
if arcpy.CheckProduct("ArcInfo") != "Available":
    msg = 'ArcGIS for Desktop Advanced license not available'
    print(msg)
    sys.exit(msg)

# Use the ListFeatureClasses function to return a list of shapefiles
featureclasses = arcpy.ListFeatureClasses("BMR*")
print(featureclasses)

#Set up for loop and split analysis
for feature in featureclasses:
    arcpy.CreateFolder_management("V:/ENV859_PS4/Scratch", feature[:-4])
    arcpy.analysis.Split(feature, "TriCounties.shp", "CO_NAME", "V:/ENV859_PS4/Scratch/"+feature[:-4])