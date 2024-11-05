#Import arc.py
import arcpy

#Print catalog path
inputfile = arcpy.GetParameterAsText(0)
desc = arcpy.da.Describe(inputfile)
arcpy.AddMessage("The CatalogPath is "+desc["catalogPath"])

#Print max and min
extent = desc["extent"]
arcpy.AddMessage("XMin: "+str(round(extent.XMin, 1)))
arcpy.AddMessage("XMax: "+str(round(extent.XMax, 1)))
arcpy.AddMessage("YMin: "+str(round(extent.YMin, 1)))
arcpy.AddMessage("YMax: "+str(round(extent.YMax, 1)))

#Check dataset type
dataset_type = desc["datasetType"]
if dataset_type == "FeatureClass":
    arcpy.AddWarning("Shape Type: "+desc["shapeType"])
elif dataset_type == "RasterDataset":
    arcpy.AddWarning("Format: "+(desc["format"]))
    arcpy.AddWarning("# of rows: "+str(desc["height"]))
    arcpy.AddWarning("# of cols: "+str(desc["width"]))
else:
    arcpy.AddError(dataset_type)