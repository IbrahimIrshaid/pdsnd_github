import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
   
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        print("Pick a City to Explore!")
        temp = str(input("Chicago, New York or Washington")).lower()#to compare to lower case no matter in what format the user inputs
        if temp == 'chicago':
            city = temp
            break
        elif temp == 'newyork' or temp == 'new york':#to cover the case where the user may forget the space in new york
            temp = 'new york'
            city = temp
            break
        elif temp == 'washington':
            city = temp
            break
        else:
            print("invalid input try again please")#treating any other input as invalid input
                   
                  
                   
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    print("Enter name of the month to filter data or enter all")
    while True:
        temp = str(input("Enter a month (January, February, March, April, May, June, or All): ")).lower()
        if temp in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            month = temp
            break
        else:
            print("Invalid input. Please try again.")

    # TO DO: get user input for month (all, january, february, ... , june)
    
    print("Enter a day to filter data or enter all")
    while True:
        temp = str(input("Sunday, Monday,...., Saturday, all")).lower()
        if temp in ("sunday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday","all"):
            day = temp
            break
        else:
            print("invalid input please try again")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'] )
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'] .dt.day_name()
                                 
    if month != 'all':
        month = months.index(month) + 1
                                
    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
   
    print("The Most Common Month is: " + months[df['month'].value_counts().idxmax()-1])                        

    # TO DO: display the most common day of week
   
    print("The Most Common Day of the Week is: "+ df['day'].value_counts().idxmax())

    # TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    print("The Most Common Hour is: " + str(df['hour'].value_counts().idxmax()))                             

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    
    print("Most Commonly Used Start Stations is: " + df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
   
    print("Most Commonly Used End Stations is: " + df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
   
    df['trip'] = df['Start Station'] + " to " + df['End Station']
    print("Most Common Combination of Start Station and End Station Trip is: " +             df['trip'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])                               
    df['travel time'] = df['End Time'] - df['Start Time']
    
    # TO DO: display total travel time
    
    print("Total Travel Time is: " + str(df['travel time'].sum()))

    # TO DO: display mean travel time
    
    print("The Mean Travel Time is: " + str(df['travel time'].mean()))


    #in th previous outputs I would format the output better if I was not short on time for example making it not showing the days when days = 0 same for hours 
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
   
    print(df['User Type'].value_counts())   

    # TO DO: Display counts of gender
   
    print(df['Gender'].value_counts())    

    # TO DO: Display earliest, most recent, and most common year of birth
    print("The Earliest Year of Birth is: " + str(df['Birth Year'].min())) 
    print("The Most Recent Year of Birth is: " + str(df['Birth Year'].max()))
    print("The Most Common Year of Birth is: " + str((df['Birth Year'].value_counts().idxmax())))# ToDo: remove the .0 since a birth year can only be an int

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
        count1 = 0
        count2 = 5
        while count1 < len(df):
            choice = input("Would You like to See 5 Trips Data? (Answer should be either yes or no)").lower()
            if choice == "yes":
                print(df.iloc[count1:count2])
                print('-'*40)
                count1 += 5
                count2 += 5
            elif choice == "no":
                break
            else:
                print("invalid input please try again")
def main():
   
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city == "washington":
            print("No Available Users' Gender/Birth Year Data for Washington!")
            print('-'*40)
        else:
            user_stats(df)
        
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
