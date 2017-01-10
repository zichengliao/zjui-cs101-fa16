import sys
import requests
import os


def grab_stdin(text=sys.stdin):
    '''Get input stations from stdin.'''
    stns = []
    locx = []
    locy = []
    for line in text:
        try:
            elems = line.split()
            stns.append(elems[0])
            locx.append(float(elems[1]))
            locy.append(float(elems[2]))
            pass  # YOUR CODE HERE
        except:
            print('Could not parse line \n\t"%s"'%line)
    return stns, locx, locy

def grab_forecast_data():
    '''Get raw data as HTML string from the NOAA website.'''
    url = 'http://www.nws.noaa.gov/mdl/gfslamp/lavlamp.shtml'
    page_file = ".forecast.txt"
    if not os.path.isfile(page_file):
        page = requests.get(url)
        
        ## YOUR CODE HERE
        
        f = open(page_file,'w')
        f.write(page.text)
        f.close()
        return page.text
    else:
        f = open(page_file,'r')
        data = f.read()
        f.close()
        return data
    
    #pass  # YOUR CODE HERE

def get_station_temp(temp_data, stn):
    '''We have a list of Illinois stations from the sites loaded previously.
       We need to load the data for each of those sites and store these data 
       locally.  There are a lot of data included here, but we are only 
       interested in one:  the current temperature, located at the index
       offset 169 and of length 2 (found by examination).
    '''
    tag_start = temp_data.find(stn)
    if tag_start == -1:
        T = float('NaN')
        return T
    tag_end = tag_start + 1720 #each text block is 1720 characters long
    T = float(temp_data[tag_start+169:tag_start+172])
    return T

stns, locx, locy = grab_stdin()
temp_data = grab_forecast_data()
for stn,lon,lat in zip(stns, locx, locy):
    temp = get_station_temp(temp_data, stn)
    try:
        print('%s\t%f\t%f\t%f'%(stn,lon,lat,temp))
    except:
        pass