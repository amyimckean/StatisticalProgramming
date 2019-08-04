# October 7th, 2018
# CPSC-51100 Statistical Programming
# Fall 1, 2018
# Programming Assignment 5: Data Preparations 
import pandas as pd

# Prints the program header
def print_header():
    print ("CPSC-51100, Fall 2018")
    print ("Name: Amy Wilson")
    print ("PROGRAMMING ASSIGNMENT #5")

# Gets the difference between the mean and standard deviation     
def mean_std_diff(country_df, add):
    country_df = country_df.drop('Continent', axis=1)
    if add:
        return country_df.stack().mean() + country_df.stack().std()
    else:
        return country_df.stack().mean() - country_df.stack().std() 

# Creates and cleans the country dataframe
def create_country_dataframe(countries):
    energy_df = pd.read_csv('energy.csv')
    energy_df.set_index("Unnamed: 0", inplace=True)
    energy_df = energy_df.apply(pd.to_numeric, args=('coerce',))
    energy_df = energy_df.apply(lambda row: row.fillna(row.mean()), axis=1)
    energy_df = energy_df.drop(['EU27total', 'OECDtotal', 'World'])
    return energy_df.join(countries)

# Creates and populates the continent dataframe         
def create_continent_dataframe(country_df):
    continent_df = pd.DataFrame(index = country_df['Continent'].unique())
    continent_df['num_countries'] = country_df.groupby('Continent')['Continent'].count()
    continent_df['mean'] = country_df.groupby('Continent').sum().T.mean() / country_df.groupby('Continent')['Continent'].count()
    continent_df['small'] = continent_df['mean'].apply(lambda row: 1 if row < mean_std_diff(country_df, False) else 0)
    continent_df['avg'] = continent_df['mean'].apply(lambda row: 1 if mean_std_diff(country_df, False) 
    < row < mean_std_diff(country_df, True) else 0)
    continent_df['large'] = continent_df['mean'].apply(lambda row: 1 if row > mean_std_diff(country_df, True) else 0)
    return continent_df

# Dataframe containing country to continent mappings
countries = pd.DataFrame([{'Australia':'Australia',
    u'Austria':'Europe',
    u'Belgium':'Europe',
    u'Canada':'North America',
    u'Chile':'South America',
    u'CzechRepublic':'Europe',
    u'Denmark':'Europe',
    u'Estonia':'Europe',
    u'Finland':'Europe',
    u'France':'Europe',
    u'Germany':'Europe',
    u'Greece':'Europe',
    u'Hungary':'Europe',
    u'Iceland':'Europe',
    u'Ireland':'Europe',
    u'Israel':'Asia',
    u'Italy':'Europe',
    u'Japan':'Asia',
    u'Korea':'Asia',
    u'Luxembourg':'Europe',
    u'Mexico':'North America',
    u'Netherlands':'Europe',
    u'NewZealand':'Oceania',
    u'Norway':'Europe',
    u'Poland':'Europe',
    u'Portugal':'Europe',
    u'SlovakRepublic':'Europe',
    u'Slovenia':'Europe',
    u'Spain':'Europe',
    u'Sweden':'Europe',
    u'Switzerland':'Europe',
    u'Turkey':'Asia',
    u'UnitedKingdom':'Europe',
    u'UnitedStates':'North America',
    u'Brazil':'South America',
    u'China':'Asia',
    u'India':'Asia',
    u'Indonesia':'Asia',
    u'RussianFederation':'Europe',
    u'SouthAfrica':'Africa'}]).T
countries.columns = ['Continent']

# Print header
print_header() 

# Create country dataframe
country_df = create_country_dataframe(countries)

# Create continent dataframes   
continent_df = create_continent_dataframe(country_df)

# Print and sort continent dataframe
print "\n", continent_df.sort_values(by=['num_countries', 'mean'], ascending=False)

           