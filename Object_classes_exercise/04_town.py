class Town:
    def __init__(self, name: str):
        self.name = name
        self.latitute = '0°N'
        self.longitude = '0°E'

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longtitude):
        self.longitude = longtitude

    def __repr__(self):
        return f'Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}'