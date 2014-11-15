import csv, sys, argparse
import pandas as pd
import geocoder
from geopy.geocoders import Nominatim
from tempfile import NamedTemporaryFile
import shutil

the_csv_file = '../Lukas_Project/taxonomies_1_test.csv'
tempfile = NamedTemporaryFile(delete=False)
target_csv_file = '../Lukas_Project/target_taxonomies_1.csv'
    
with open(the_csv_file, 'rb') as file_input, open(target_csv_file, 'wb') as file_output :
    reader = csv.reader(file_input, skipinitialspace=True)
    writer = csv.writer(file_output, skipinitialspace=True)
    totalrows = 0
    try:
        #next(reader)
        for line in reader:
            province = line[6]
            latitude = line [9]
            longitude = line [10]
            totalrows += 1
            print totalrows
            if province == 'Indonesia':
                print ('Indonesia is not province')
                line[9] = lat_coordinate
                line[10] = long_coordinate 
                writer.writerow(line)
            elif province == '' :
                print ('location not defined')
                line[9] = lat_coordinate
                line[10] = long_coordinate
                writer.writerow(line)
            else :    
                province = province             
                geolocator = Nominatim()
                #location = geolocator.geocode(province)
                g = geocoder.google(province)
                if g != None :
                    #lat_coordinate = location.latitude
                    #long_coordinate = location.longitude
                    lat_coordinate = g.lat
                    long_coordinate = g.lng
                    print ('latitude : ', line[9], '-- longitude : ', line[10])
                    print ('province : ', province,' -- longitude : ', long_coordinate, ' -- latitude : ', lat_coordinate)
                    line[9] = lat_coordinate
                    line[10] = long_coordinate
                    writer.writerow(line)
                    #Neutralize the value
                    lat_coordinate = None
                    long_coordinate = None
                else :
                    next(reader)
                    writer.writerow(line)
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (the_csv_file, reader.line_num, e))
