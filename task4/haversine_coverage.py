from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lng1, lat2, lng2):
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert latitude and longitude from degrees to radians
    lat1, lng1, lat2, lng2 = map(radians, [lat1, lng1, lat2, lng2])

    # Calculate the differences in coordinates
    dlat = lat2 - lat1
    dlng = lng2 - lng1

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlng / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Distance in kilometers
    distance = R * c

    return distance

def calculate_coverage(locations, shoppers):
    coverage_list = []

    for shopper in shoppers:
        if not shopper['enabled']:
            continue

        covered_zones = 0

        for location in locations:
            distance = haversine(shopper['lat'], shopper['lng'], location['lat'], location['lng'])
            if distance < 10:
                covered_zones += 1

        coverage_percentage = (covered_zones / len(locations)) * 100
        coverage_list.append({'shopper_id': shopper['id'], 'coverage': coverage_percentage})

    # Sort the coverage list in descending order
    sorted_coverage = sorted(coverage_list, key=lambda x: x['coverage'], reverse=True)

    return sorted_coverage

# Example usage
locations = [
    {'id': 1000, 'zip_code': '37069', 'lat': 45.35, 'lng': 10.84},
    {'id': 1001, 'zip_code': '37121', 'lat': 45.44, 'lng': 10.99},
    {'id': 1001, 'zip_code': '37129', 'lat': 45.44, 'lng': 11.00},
    {'id': 1001, 'zip_code': '37133', 'lat': 45.43, 'lng': 11.02},
]

shoppers = [
    {'id': 'S1', 'lat': 45.46, 'lng': 11.03, 'enabled': True},
    {'id': 'S2', 'lat': 45.46, 'lng': 10.12, 'enabled': True},
    {'id': 'S3', 'lat': 45.34, 'lng': 10.81, 'enabled': True},
    {'id': 'S4', 'lat': 45.76, 'lng': 10.57, 'enabled': True},
    {'id': 'S5', 'lat': 45.34, 'lng': 10.63, 'enabled': True},
    {'id': 'S6', 'lat': 45.42, 'lng': 10.81, 'enabled': True},
    {'id': 'S7', 'lat': 45.34, 'lng': 10.94, 'enabled': True},
]

result = calculate_coverage(locations, shoppers)
print(result)