import rasterio
from rasterio.transform import from_origin

def save_dataarray_as_geotiff(data_array, output_filename, resampling=Resampling.nearest):
    # Determine dimensions
    bands, rows, cols = data_array.shape
    
    # Define geotransform parameters
    # Assuming your data array represents a grid of pixels, adjust these parameters accordingly
    pixel_width = 0.01
    pixel_height = 0.01
    transform = from_origin(0, 0, pixel_width, pixel_height)

    # Define metadata
    metadata = {
        'count': bands,  # Number of bands
        'dtype': str(data_array.dtype),  # Data type
        'driver': 'GTiff',  # Output file format
        'height': rows,  # Number of rows
        'width': cols,  # Number of columns
        'transform': transform,  # Affine transformation parameters
        'crs': 'EPSG:4326',  # Coordinate reference system, adjust as needed
    }
    
    with rasterio.open(output_filename, 'w', **metadata) as dst:
        # Iterate over bands
        for band in range(bands):
            # Get the band data
            band_data = data_array[band, :, :]
            
            # Write the band data to the GeoTIFF file
            dst.write(band_data.astype(data_array.dtype), indexes=band + 1)