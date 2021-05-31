import data

tours = dict(filter(lambda tour: tour[1]['departure'] == dep, data.tours.items()))

print(tours)