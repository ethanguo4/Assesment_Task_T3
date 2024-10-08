#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt     

#dataframe stuff
file_path = 'data/vgchartz-2024.csv'

#----Global Variables----#
quit = False
gamedf = pd.read_csv("data/vgchartz-2024.csv")

gamedf2 = gamedf[['title', 'genre', 'publisher', 'developer', 'critic_score', 'release_date', 'total_sales']]
#global quit
quit = False

#----Global Variables----#
gamedf = pd.read_csv("data/vgchartz-2024.csv")


def useCases():
    global quit

    print("This UI will present data on game sales, release dates and genres. Please make a pick of which dataset you would like.")

    print("Choose a dataset.")
    print("1. Original Data")
    print("2. Total Sales")
    print("3. Game Sales over the Years")
    print('4. Games rankings')
    print('5. Genre popularity')
    print("6. Exit the UI? :(")
    
    choice = input("Please enter your choice, (1-6): ")

    if choice == '1':
        originaldata()
    elif choice == '2':
        one()
    elif choice == '3':
        two()
    elif choice == '4':
        three()
    elif choice == '5':
        four()
    elif choice == '6':
        print("Exiting... :(")
        exit()
    else:
        print("Try entering a number between 1-6.")


#----Define Functions Below----#
def originaldata():
        gamedf = pd.read_csv("data/vgchartz-2024.csv", on_bad_lines='warn')
        with pd.option_context('display.max_rows', None,
                        'display.max_colums', None,
                        'display.width', None,
                        'display.precision', 3,
                        'display.colheader_justify', 'left'):
            print( gamedf ) 

def one():
    a = gamedf2['total_sum'].sum()
    print(f"Total amount of sales made by games is {a} people")

def columns():
    column = input('Choose a colum: ')
    if column in gamedf2.columns:
        result = gamedf2[column]
        print(result)
    else:
       print(f"Column {column} isn't in the dataframe :/")

def two():
    filtered_df = gamedf2[gamedf2["title"].str.contains("X...X")]
    filtered_df = gamedf2[gamedf2["critic_score"].str.contains("N.N")]

    filtered_df.plot(
    kind='bar',
    x='genre',
    y='total_sales',
    color='blue',
    alpha=0.3,
    title='Game Sales over the Years')
    plt.show()

def three():
    filtered_df = gamedf2[gamedf2["title"].str.contains("X...X")]
    filtered_df = gamedf2[gamedf2["critic_score"].str.contains("N.N")]

    filtered_df.plot(
    kind='bar',
    x='title',
    y='critic_score',
    color='blue',
    alpha=0.3,
    title='Games Rankings') 
    plt.show()

def four():
    filtered_df = gamedf2[gamedf2["genre"].str.contains("X...X")]
    filtered_df = gamedf2[gamedf2["total_sales"].str.contains("N.NN")]

    filtered_df.plot(
    kind='bar',
    x='genre',
    y='total_sales',
    color='blue',
    alpha=0.3,
    title='Genre popularity')
    plt.show()
    
    
print(gamedf2.dtypes)

while not quit:
    useCases()
