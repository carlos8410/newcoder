FILE_PATH = ''
import urllib2
TARGET_URL = 'https://research.stlouisfed.org/fred2/data/CPIAUCSL.txt'
Headline_of_Data = "DATE          VALUE"

def main():
    """This function handles the actual logic of this script."""
    try:
        raw_data = urllib2.urlopen(TARGET_URL)
    except:
        print "Exception in reading data from target url \n%s" % TARGET_URL
    cpi_data = []
    for line in raw_data:
        if Headline_of_Data in line:
            break
    for line in raw_data:
        


    # Grab CPI/Inflation data.
    
    # Grab API/game platform data.

    # Figure out the current price of each platform.
    # This will require looping through each game platform we received, and
    # calculate the adjusted price based on the CPI data we also received.
    # During this point, we should also validate our data so we do not skew
    # our results.

    # Generate a plot/bar graph for the adjusted price data.

    # Generate a CSV file to save for the adjusted price data.