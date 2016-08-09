# -*- coding: utf-8 -*-

import arcpy
from arcpy import env

#Fields
'''ProductName','Sensor Name','Sensor ID','Acquisition Date','Orbit ID','Sun Elevation'
            ,'Sun Azimuth','Satellite Elevation','Satellite Azimuth','Cloud Cover','OffNadir','Archive Type','Archive Path',
             'Scene Path','Scene Row','GroupName',row col bands format pixelType size sacle '''

fieldName= ['SensorName','SensorID','AcquisitionDate','OrbitID','SunElevation','SunAzimuth'
	,'SatelliteElevation','SatelliteAzimuth','CloudCover','OffNadir','ArchiveType','ArchivePath','Row',
		 'Col','BandCount','DataFormat','PixelType','ImageSize', 'ScenePath','SceneRow','PixelSize']
fieldType= ['TEXT','TEXT','DATE','TEXT','FLOAT','FLOAT','FLOAT','FLOAT','FLOAT','FLOAT','TEXT','TEXT','SHORT',
			'SHORT','SHORT','TEXT','TEXT','DOUBLE','TEXT','TEXT','DOUBLE']
fieldLength=[50,50,'',50,'','','','','','',50,300,'','','',50,50,'',50,50,'']
mosaicDataSetName= 'GF'
env.workspace=r"C:\Users\zhongren\Desktop\Temp\test.gdb"

print("fedldName length:"+str(len(fieldName)))
print("fieldType length:"+str(len(fieldType)))
print("fieldLength length:" + str(len(fieldLength)))

for index,value in enumerate(fieldName):
	print('add field'+ " "+ value)
	arcpy.AddField_management(mosaicDataSetName,value,fieldType[index],'','',fieldLength[index])
	arcpy.AddField_management("GF",'SensorName','TEXT','','',50)
print('finish')
