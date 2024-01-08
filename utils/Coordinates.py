class Coordinates:
    @staticmethod
    def decimal_coords(self, coords, ref):
        decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
        if ref == "S" or ref == "W":
            decimal_degrees = -decimal_degrees
        return decimal_degrees

    @staticmethod
    def image_coordinates(self, img):
        print("has exif", img.has_exif)
        if not img.has_exif:
            raise ValueError("Image does not contain any EXIF data.")
        print(img.gps_latitude, img.gps_latitude_ref)
        print(img.gps_longitude, img.gps_longitude_ref)
        try:
            coords = (Coordinates.decimal_coords(self, img.gps_latitude, img.gps_latitude_ref),
                      Coordinates.decimal_coords(self, img.gps_longitude, img.gps_longitude_ref))
            return coords
        except AttributeError:
            print('No Coordinates')
