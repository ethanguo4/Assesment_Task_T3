#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt


#----Global Variables----#
quit = False
gamedf = pd.read_csv('/ethanslaptopd/documents/vgchartz-2024.csv', on_bad_lines='skip')

gamedf2 = pd.read_csv('/ethanslaptopd/documents/vgchartz-2024.csv',
                   header=None,
                   names=['Title', 'Genre', 'Critic', 'Date', 'Total Sales'])

def useCases():
    global quit

    print("This UI will present data on game sales, release dates and genres. Please make a pick of which dataset you would like.")

    while True:
        print("\nChoose a dataset.")
        print("1. Original Data")
        print("2. Genre Sales")
        print("3. Game Sales over the Years")
        print('4. Popular genres ')
        print("5. Exit the UI? :(")
        
        choice = int(input("Please enter your choice, (1-5): "))

        if choice == '1':
            originaldata()
        elif choice == '2':
            one()
        elif choice == '3':
            two()
        elif choice == '4':
            three()
        elif choice == '5':
            print("Exiting... :(")
            break
        else:
            print("Try entering a number between 1-5.")


#----Define Functions Below----#
def originaldata():
        gamedf = pd.read_csv('vgchartz-2024.csv', on_bad_lines='warn', encoding='ISO-8859-1')
        with pd.option_context('display.max_rows', None,
                        'display.max_colums', None,
                        'display.width', None,
                        'display.precision', 3,
                        'display.colheader_justify', 'left'):
            print( gamedf ) 

def one():
    a = gamedf2['Total Sales'].sum()
    print(f"Total amount of sales made by games is {x} people")

def two():
    column = input('Choose a colum: ')
    if column in gamedf2.columns:
        result = gamedf2[column]
        print(result)
    else:
       print(f"Column {column} isn't in the dataframe :/")

def three():
    gamedf2.plot( 
    kind='bar',
    x='Genre',
    y='Total Sales',
    colour='blue',
    alpha=0.3,
    title='Total Sales in Genres')
    plt.show()





print(cldb)

def cleandata():
    global dataset
    dataset = dataset.drop_duplicates()
    dataset = dataset.drop['img']
    dataset = dataset.drop['na_sales']
    dataset = dataset.drop['jp_sales']
    dataset = dataset.drop['pal_sales']
    dataset = dataset.drop['last_update']

n = dataset
n = n.sort_values('release_date')
n.to_csv