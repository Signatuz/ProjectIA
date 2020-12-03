import csv
from csv import reader

colors = ['BLACK', 'BLUE', 'BROWN', 'GOLD', 'GREEN', 'GREY', 'ORANGE', 'PINK', 'PURPLE', 'RED', 'SILVER', 'WHITE', 'YELLOW', 'IVORY', 'BLACK/BLUE']

stop_words = ['SET', 'PACK', 'SMALL', 'LARGE', 'JUMBO', 'OF']

categories = ['MINT', 'ROSEMARY', 'BASIL', 'CHIVES', 'PARSLEY', 'THYME', 'BOXES', 'BOX']


def write(row):
    with open('datanew.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)


def read():
    with open('data.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            filtered_row = []
            for r in row:
                for word in r.split(' '): 
                    if word in categories: 
                        r = r.replace(word, '').replace('  ', ' ')
                    if word in colors: 
                        r = r.replace(word, '').replace('  ', ' ') 
                    if word in stop_words: 
                        r = r.replace(word, '').replace('  ', ' ') 

                filtered_row.append(r)
            write(filtered_row)


read()