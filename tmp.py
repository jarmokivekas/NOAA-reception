import gdal
import osr


data = np.random.rand(5,6)

lats = np.array([-5.5, -5.0, -4.5, -4.0, -3.5])
lons = np.array([135.0, 135.5, 136.0, 136.5, 137.0, 137.5])

xres = lons[1] - lons[0]
yres = lats[1] - lats[0]

ysize = len(lats)
xsize = len(lons)

ulx = lons[0] - (xres / 2.)
uly = lats[-1] - (yres / 2.)

driver = gdal.GetDriverByName('GTiff')
ds = driver.Create('test.tif', xsize, ysize, 1, gdal.GDT_Float32)

# this assumes the projection is Geographic lat/lon WGS 84
srs = osr.SpatialReference()
srs.ImportFromEPSG(4326)
ds.SetProjection(srs.ExportToWkt())

gt = [ulx, xres, 0, uly, 0, yres ]
ds.SetGeoTransform(gt)

outband = ds.GetRasterBand(1)
outband.WriteArray(data)

ds = None
