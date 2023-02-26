"""
Created on Feb 25, 2023

@author: Wajiha
"""

import pandas as pd
import matplotlib.pyplot as plt
    

def population_bar_plot(xlabel, ylabel, subject, data):
    """
    Produces a bar graph for the population of different countries for 
    the given years.
    xlabel: To represent the title for x-axis
    ylabel: It is used to represent the title for y-axis
    subject: This parameter is used to define graph subject. It will be
    displayed on the top of the graph
    data: Data for population of countries over years. Columns will hold the
    population of countries and years. Year is being displayed on x-axis and
    on y-axis, we have displayed population.

    """
    
    ax = data.plot(kind='bar', figsize=(10, 6), width=0.8)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(subject)
    ax.legend(['USA', 'China', 'India', 'Indonesia', 'Brazil'])
    plt.show()
    

def year_population_pie_chart(data, title):
    """
    Produces a piechart of data to represent population ratio in major
    countries with other countries.
    data: an object of Pandas DataFrame having only one row of data 
    holding the countries and their population
    and total population in the given year.
    title: a string to name the graph

    """
    
    populations = data
    
    # Get and store percentages for each of country population in order to
    # display as a ratio
    percentages = (populations / populations.sum()) * 100
    
    plt.pie(percentages, labels=percentages.index, autopct='%1.1f%%', 
            startangle=90)
    plt.title(title)
    plt.axis('equal')
    
    plt.show()
    

def pak_weather lineplot(data, months):
    """
    Produces a minimal multiple-line graph to represent average temperature of 
    some cities of Pakistan during some initial months of year.
    data: an object of Pandas DataFrame having columns for city names and 
    months. Each column for month contains the average temperature in the
    specific city.
    months: a list of months for which we want to display data.

    """
    for month in months:
        plt.plot(data['City_name'], data[month], label=month)
    plt.legend()
    plt.xlabel('Month')
    plt.ylabel("Temperature")
    plt.show()
    
    

population_data_path = ('/Volumes/Untitled 2/ds_assignments/assignment_1/' 
+'population_by_country3.csv')
population_data= pd.read_csv(population_data_path)

weather_data_path =  ('/Volumes/Untitled 2/ds_assignments/assignment_1/' 
+'pak_temp.csv')
weather_data = pd.read_csv(weather_data_path)

# Create an object of Panda's DataFrame using first 30 rows of the data
df = pd.DataFrame(population_data.head(30))

# Change the data type of year column from float to int
df.year = df.year.astype(int)

# Set the year column as index of the complete DataFrame object
df.set_index('year', inplace=True)

# Create a bar graph for population against different years
df_for_bar_graph = df.loc[:, ["China","India", "USA", "Brazil", "Indonesia"]]
population_bar_plot('Year', 'Population', 'Country Populations', df_for_bar_graph)


# PieChart
df['Others'] = df['TotalPopulation'] - (df['China'] + df['India'] + 
                                        df['USA'] + df['Brazil'] + df['Indonesia'])
selected_year = df.iloc[-1].name
year_population_pie_chart(df.iloc[-1, [0, 1, 2, 3, 4, 6]], 
                          'Population Distribuation for year ' + str(selected_year), )


# Processing weather data
weather_data = weather_data.drop(columns=["Range"])

months = ["January","February","March","April","May","June","July","August",
          "September","October","November","December"]

pak_weather lineplot(weather_data.head(), months[0:5])






















