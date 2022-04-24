import csv

header = ['Country', '2014', '2019']
data = [
    ['AUS', 324100, ]
]

with open('attendance.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)


