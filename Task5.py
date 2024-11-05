#Import arc.py
import arcpy

# Set input variables 
inputFeatureClass = arcpy.GetParameterAsText(0) 
inputField = arcpy.GetParameterAsText(1)

#Create point
pt = arcpy.Point(590000, 230000)

#Create cursor
cur = arcpy.da.SearchCursor(inputFeatureClass,['Shape@',inputField])

#for loop
for row in cur:
    recShape = row[0]
    if recShape.contains(pt):
        arcpy.AddMessage("The field's value is "+row[1])

#delete cursor
del cur