import csv
from csv import reader

colors = ['BLACK', 'BLUE', 'BROWN', 'GOLD', 'GREEN', 'GREY', 'ORANGE', 'PINK', 'PURPLE', 'RED', 'SILVER', 'WHITE', 'YELLOW', 'IVORY', 'BLACK/BLUE']

stop_words = ['SET', 'PACK', 'SMALL', 'LARGE', 'JUMBO', 'OF', '&', 'IN', 'SET/10', ' DOLLY', 'GIRL', 'CIRCUS', 'PARADE', 'BAKE', 'CAKE', 'A', 'IN',
             'TIN' 'STRONGMAN', 'SKULLS','SPACEBOYS', 'GIRAFFE', 'REVOLVER', 'SET/2','SET/3','SET/4','SET/5','SET/7','SET/8','SET/9', 'OF4','500g','+']

categories = ['DINOSAURS','BALLOONS','MINT', 'ROSEMARY', 'BASIL', 'CHIVES', 'PARSLEY', 'THYME', 'BOXES', 'BOX',"50'S", 'POLKADOT', 'RETROSPOT',
             'ANIMALS', 'AND', 'NATURE','HORSE','PONY','BUFFALO', 'BILL', 'TOMATO','CARROT']

design = ['GINGHAM', 'BUTTERFLY', 'ZINC', 'STAR', 'SKULL', 'DOLLY', 'WOOD', 'RETRO', 'STRAWBERRY',
         'MINI', 'POLKADOT', 'SPOT', 'CREAM', 'ROSE', 'CERAMIC', 'GLASSE', 'VINTAGE', 'RETROSPOT', 'HEART',
         'SPOTS', 'SKULLS', 'SCANDINAVIAN', 'LONDON', 'FRENCH', 'WOODEN', 'WOODLAND', 'BAKELIKE', 'FELTCRAFT', 'PORCELAIN',
         'SPACEBOY', 'GLASS', 'TRADICIONAL', 'BIRD', 'BIRDS', 'FLOWER', 'ANTIQUE', 'TUBE','DAISY','TRAY','POLKA', 'KEEP','CALM','CUP','TEA']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50']


coluna_remover = 2  #começa em 0


def write(row):
    with open('datanew.csv', 'a+', newline='', encoding='UTF-8') as file: #ira criar um novo arquivo csv com os nomes filtrados
        writer = csv.writer(file)
        writer.writerow(row)


def read():
    with open('data.csv', 'r', encoding='UTF-8') as read_obj: # abrir o arquivo csv atual para começar a limpeza
        csv_reader = reader(read_obj)
        for row in csv_reader:
            filtered_row = []
            for index, cell in enumerate(row):
                if index == coluna_remover:
                    for word in cell.split(' '): # verifica se a palavra  esta presente em uma das listas, se estiver ela é excluida
                        if word in categories: 
                            cell = cell.replace(word, '').replace('  ', ' ')
                        if word in colors: 
                            cell = cell.replace(word, '').replace('  ', ' ') 
                        if word in stop_words: 
                            cell = cell.replace(word, '').replace('  ', ' ')
                        if word in design: 
                            cell = cell.replace(word, '').replace('  ', ' ') 
                        if word in numbers: 
                            cell = cell.replace(word, '').replace('  ', ' ')

                filtered_row.append(cell)
            write(filtered_row)

read()