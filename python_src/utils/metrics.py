import matplotlib.pyplot as plt
from data.date import Date
from data.client import Client
import statistics


def getAverage(list):
    sum_num = 0
    for t in list:
        sum_num += t

    avg = sum_num / len(list)
    return avg


def valuelabel(subPlot, weight, height):
    for i in range(len(weight)):
        subPlot.text(i+1, height[i], height[i], ha='center',
                 bbox=dict(facecolor='cyan', alpha=0.8))


def display_client_metrics(data):
    list_clients = data.clients
    list_of_ages = data.get_all(list_clients, Client.get_birth_date_year)

    age_avg = round(getAverage(list_of_ages), 2)

    age_moda = statistics.mode(list_of_ages)

    age_min = min(list_of_ages)

    age_max = max(list_of_ages)

    left_coordinates = [1, 2, 3, 4]
    heights = [age_avg, age_moda, age_max, age_min]
    bar_labels = ['Media', 'Moda', 'Max', 'Min']

    fig, axs = plt.subplots(2)
    fig.suptitle('Vertically stacked subplots')
    axs[0].bar(left_coordinates, heights, tick_label=bar_labels,
        width=0.6, color=['red', 'black'])
    axs[1].bar(left_coordinates, heights, tick_label=bar_labels,
        width=0.6, color=['red', 'black'])

    valuelabel(axs[0], left_coordinates, heights)
    valuelabel(axs[1], left_coordinates, heights)
    plt.show()

    # plt.bar(left_coordinates, heights, tick_label=bar_labels,
    #         width=0.6, color=['red', 'black'])

   

    # plt.xlabel('Idade')
    # plt.ylabel('Metricas')
    # plt.title("Client Metrics")
    

    # plt.show()
