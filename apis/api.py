FILE_PATH = ''
import urllib2
CPI_DATA_URL = 'https://research.stlouisfed.org/fred2/data/CPIAUCSL.txt'
Headline_of_Data = "DATE          VALUE"

class CPIData(object):
    """Abstraction of the CPI data provided by FRED.
    This stores internally only one value per year.
    """

    def __init__(self):
        self.year_cpi = {}
        self.last_year = None
        self.first_year = None

    def load_from_url(self, url, save_as_file=None):
        """Loads data from a given url.

        The downloaded file can also be saved into a location for later
        re-use with the "save_as_file" parameter specifying a filename.

        After fetching the file this implementation uses load_from_file
        internally.

        """

        # We don't really know how much data we are going to get here, so
        # it is recommended to just keep as little data as possible in memory
        # at all times. Since python-requests supports gzip-compression by
        # default and decoding these chunks on their own isn't that easy,
        # we just disable gzip with the empty "Accept-Encoding" header.
        fp = requests.get(url, stream=True, headers={'Accept-Encoding':None}).raw
        # If we did not pass in a save_as_file parameter, we just return the
        # raw data we got from the previous line.
        if not save_as_file:
            return self.load_from_file(fp)

        # Else, we write to the desired file.
        else:
            chunk_size = 81920
            # with open(filename, 'wb+') as out:
            #     for chunk in r.iter_content(chunk_size):
            #         out.write(chunk)
            with open(save_as_file, 'wb+') as out:
                while True:
                    buffer = fp.read(chunk_size):
                    if not buffer:
                        break
                    out.write(buffer)
            with open(save_as_file) as fp:
                return self.load_from_file(fp)

        return fp

    def load_from_file(self, fp):
        """Loads CPI data from a given file-like object."""
        # When iterating over the data file we will need a handful of temporary
        # variables:
        current_year = None
        year_cpi = []
        for line in cp:
            # The actual content of the file starts with a header line
            # starting with the string "DATE ". Until we reach this line
            # we can skip ahead.
            while not line.startwith("DATE "):
                continue
            data = line.rstrip().split()
            year = int(data[0].split('-')[0])
            cpi = float(data[1])

            if not self.first_year:
                self.first_year = year
            self.last_year = year

            if current_year != year:
                if current_year is not None:
                    self.year_cpi[current_year] = sum(year_cpi) / len(year_cpi)
                year_cpi = []
                current_year = year
            year_cpi.append(cpi)
        if current_year is not None and current_year not in self.year_cpi:
            self.year_cpi[current_year] = sum(year_cpi) / len(year_cpi)
                

    def get_adjusted_price(self, price, year, current_year=None):
        """Returns the adapted price from a given year compared to what current
        year has been specified.

        """
        if current_year is None or current_year > 2013:
            current_year = 2013
        # If our data range doesn't provide a CPI for the given year, use
        # the edge data.
        if year < self.first_year:
            year = self.first_year
        elif year > self.last_year:
            year = self.last_year

        given_year_cpi = self.year_cpi[year]
        current_year_cpi = self.year_cpi[current_year]
        return float(price) / given_year_cpi * current_year_cpi

def main():
    """This function handles the actual logic of this script."""
    try:
        raw_data = urllib2.urlopen(CPI_DATA_URL)
    except:
        print "Exception in reading data from target url \n%s" % CPI_DATA_URL
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