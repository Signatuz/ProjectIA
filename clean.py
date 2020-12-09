import csv
from csv import reader

colors = ['BLACK', 'BLUE', 'BROWN', 'GOLD', 'GREEN', 'GREY', 'ORANGE', 'PINK', 'PURPLE', 'RED', 'SILVER', 'WHITE', 'YELLOW', 'IVORY', 'BLACK/BLUE']

stop_words = ['SET', 'PACK', 'SMALL', 'LARGE', 'JUMBO', 'OF', '&', 'IN', 'SET/10', ' DOLLY', 'GIRL', 'CIRCUS', 'PARADE', 'BAKE', 'CAKE', 'A', 'IN',
             'TIN' 'STRONGMAN', 'SKULLS','SPACEBOYS', 'GIRAFFE', 'REVOLVER', 'SET/2','SET/3','SET/4','SET/5','SET/7','SET/8','SET/9', 'OF4','500g']

categories = ['DINOSAURS','BALLOONS','MINT', 'ROSEMARY', 'BASIL', 'CHIVES', 'PARSLEY', 'THYME', 'BOXES', 'BOX',"50'S", 'POLKADOT', 'RETROSPOT',
             'ANIMALS', 'AND', 'NATURE','HORSE','PONY','BUFFALO', 'BILL','TOMATO','CARROT']

Design = ['GINGHAM', 'BUTTERFLY', 'ZINC', 'STAR', 'SKULL', 'DOLLY', 'WOOD', 'RETRO', 'STRAWBERRY',
         'MINI', 'POLKADOT', 'SPOT', 'CREAM', 'ROSE', 'CERAMIC', 'GLASSE', 'VINTAGE', 'RETROSPOT', 'HEART',
         'SPOTS', 'SKULLS', 'SCANDINAVIAN', 'LONDON', 'FRENCH', 'WOODEN', 'WOODLAND', 'BAKELIKE', 'FELTCRAFT', 'PORCELAIN',
         'SPACEBOY', 'GLASS', 'TRADICIONAL', 'BIRD', 'BIRDS', 'FLOWER', 'ANTIQUE', 'TUBE','DAISY','TRAY','POLKA', 'KEEP','CALM','CUP','TEA']

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
                    if word in Design: 
                        r = r.replace(word, '').replace('  ', ' ') 

                filtered_row.append(r)
            write(filtered_row)


read()