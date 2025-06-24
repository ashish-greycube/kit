def calculate_trip_km(self, method):
    if self.last_odometer and self.odometer:
        trip_km = self.odometer - self.last_odometer
        self.custom_trip_km = trip_km