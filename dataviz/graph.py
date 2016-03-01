
from parse import parse, MY_FILE
from collections import Counter
import matplotlib.pyplot as plt
import numpy

def visualize_days(parsed_data):
    """visualize data by day of week"""
    counter = Counter(item['DayOfWeek'] for item in parsed_data)
    data_list = [
    counter["Monday"],
    counter["Tuesday"],
    counter["Wednesday"],
    counter["Thursday"],
    counter["Friday"],
    counter["Saturday"],
    counter["Sunday"]
    ]

    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])
    # with that y-axis data, assign it to a matplotlib plot instance
    plt.plot(data_list)
    # Assign labels to the plot
    plt.xticks(range(len(day_tuple)), day_tuple)
    # save the plot!
    plt.savefig("Days.png")
    # close plot file
    plt.clf()

def visualize_type(parsed_data):
    """Visualize data by category in a bar graph"""
    counter = Counter(item['Category'] for item in parsed_data)
    
    width = 0.5 # Width of each bar
    labels = tuple(counter.keys())
    xlocations = numpy.arange(len(labels)) + 0.5
    plt.bar(xlocations, counter.values(), width=width)
    plt.xticks(xlocations + width / 2, labels, rotation=90)
    # Give some more room so the labels aren't cut off in the graph
    plt.subplots_adjust(bottom = 0.4)
    # Make the overall graph/figure larger
    plt.rcParams['figure.figsize'] = 12, 8

    plt.savefig("Types.png")
    plt.clf()

if __name__ == "__main__":
    parsed_data = parse(MY_FILE, ',')
    # visualize_days(parsed_data)
    visualize_type(parsed_data)
    

