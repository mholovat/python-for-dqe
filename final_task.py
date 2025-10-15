import sqlite3
from math import radians, sin, cos, sqrt, atan2

def haversine_distance(lat1, lon1, lat2, lon2):
    # Earth's radius in kilometers
    R = 6371.0

    # Convert degrees to radians
    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    # Difference in coordinates
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


def get_city_coordinates(name):
    conn = sqlite3.connect('cities.db')
    c = conn.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS cities(name TEXT, latitude REAL, longitude REAL)')
    coordinates = c.execute(f'''SELECT latitude, longitude FROM cities WHERE name = "{name}"''').fetchone()

    c.close()
    conn.commit()
    conn.close()

    return coordinates


def store_coordinates(name, city_latitude, city_longitude):
    conn = sqlite3.connect('cities.db')
    c = conn.cursor()

    c.execute(f"""INSERT INTO cities (name, latitude, longitude) VALUES ("{name}", {city_latitude}, {city_longitude})""")

    c.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    city1_name = input('Enter name for the first city: ')
    city2_name = input('Enter name for the second city: ')

    if get_city_coordinates(city1_name) == None:
        print(f'''We haven't' found the coordinates for {city1_name} in our database. Could you please provide these?''')
        city1_latitude = input('Latitude: ')
        city1_longitude = input('Longitude: ')
        store_coordinates(city1_name, float(city1_latitude), float(city1_longitude))
    else:
        city1_latitude, city1_longitude = get_city_coordinates(city1_name)

    if get_city_coordinates(city2_name) == None:
        print(f'''We haven't' found the coordinates for {city1_name} in our database. Could you please provide these?''')
        city2_latitude = input('Latitude: ')
        city2_longitude = input('Longitude: ')
        store_coordinates(city2_name, float(city2_latitude), float(city2_longitude))
    else:
        city2_latitude, city2_longitude = get_city_coordinates(city2_name)

    distance = haversine_distance(float(city1_latitude), float(city1_longitude),
                                  float(city2_latitude), float(city2_longitude))

    print(f'The distance between {city1_name} and {city2_name} is {distance}')