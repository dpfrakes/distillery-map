def format_coordinates(latitude, longitude):
    lat_deg = int(latitude)
    lat_min = abs(int((latitude % 1) * 60))
    lat_sec = abs(int((((latitude % 1) * 60) % 1) * 60))
    lng_deg = int(longitude)
    lng_min = abs(int((longitude % 1) * 60))
    lng_sec = abs(int((((longitude % 1) * 60) % 1) * 60))
    return f'{lat_deg}°{lat_min}\'{lat_sec}" {lng_deg}°{lng_min}\'{lng_sec}" '
