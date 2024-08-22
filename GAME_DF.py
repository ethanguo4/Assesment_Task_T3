#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt


#----Global Variables----#
quit = False
game_df = pd.read_csv('/Downloads/vgchartz-2024.csv', on_bad_lines='skip')

def main():
    
    while True:
        print("\nChoose a dataset.")
        print("1. Genre Sales")
        print("2. Game Sales over the Years")
        print("3. Popular genres ")
        print("4. Exit")
        
        choice = input("Please enter your choice, (1/2/3/4): ")

        if choice == '1':
            plot_Genre_Sales()
        elif choice == '2':
            plot_Game_Sales_over_the_Years()
        elif choice == '3':
            plot_Popular_genres()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the main function
if __name__ == "__main__":
    main()


#----Define Functions Below----#
dataset.plot(
               kind='scatter',
               x='genre',
               y='total_sales',
               color='blue',
               alpha=0.3,
               title='Popularity of Genres'
              )
plt.show()

dataset.plot(
               kind='scatter',
               x='genre',
               y='total_sales',
               color='blue',
               alpha=0.3,
               title='Popularity of Genres'
              )
plt.show()

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