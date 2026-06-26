import json
from needed_urls import urls

filters = ['gdp', 'population', 'countries']
region_filter = ['Europe', 'North America', 'South America', 'Asia', 'Africa', 'Oceania']

with open('scraped_data.json', 'r') as file:
    all_tables = json.load(file)

while True:
    chosen_filter = input('Enter a filter(gdp/population/countries): ').lower()
    if chosen_filter not in filters:
        print('Please enter a valid filter')
        continue
    break

current_filter = ''
for link in urls:
    if chosen_filter in link:
        current_filter = link

country_list = []

if chosen_filter == 'gdp' or chosen_filter == "countries":
    for row in all_tables[current_filter]:
        country_list.append(row['Country'])

if chosen_filter == 'gdp':
    while True:
        print('Enter a specific country to see GDP or leave blank to show all countries, or type "bye" to exit')
        print("Or you can choose to see GDP per continent, leave blank to show all continents")
        print(f'Continents: {", ".join(region_filter)}')
        chosen_continent = input('Choose continent: ')
        chosen_country = input('Choose specific country to show gdp: ')
        data = all_tables[current_filter]

        if chosen_country == 'bye' or chosen_continent == 'bye':
            break

        if chosen_continent == '':

            if chosen_country == '':
                with open('filtered_data.json', 'w', encoding='utf-8') as file:
                        json.dump(data, file, indent=4)
            else:
                if chosen_country not in country_list:
                    print('Please choose another country!')
                    continue
                for row in data:
                    if chosen_country in row.values():
                        with open('filtered_data.json', 'w') as file:
                            json.dump(row, file, indent=4)

        else:
            if chosen_continent not in region_filter:
                print('Please choose another continent!')
                continue
            continent_gdp = []
            total_gdp = 0
            gdp_full_value = 0
            for row in data:
                if chosen_country not in country_list:
                    print('Please choose another country!')
                    continue
                for key, value in row.items():
                    if key == 'GDP (Full Value)':
                        current_gdp = value
                        b = current_gdp.replace(',','_')
                        gdp_full_value += int(b)
                        total_gdp += int(b[:5])

elif chosen_filter == 'population':
    # TODO POPULATION TASK
    print('Enter a specific country to see its population, or leave blank to show all countries')
    print('You can also sort by Regions/Continents to see the population, leave blank to show all continents')
    chosen_region = input('Choose region: ')
    chosen_country = input('Choose country: ')
    pass

elif chosen_filter == 'countries':
    data = all_tables[current_filter]
    print('Enter a specific Region to see countries and their population information, leave space to show all countries')
    print('Also, you can sort by Regions/Continents, leave blank if you want to see all regions.')
    chosen_region = input('Choose Region to see countries[Europe, South/North America, Asia, Africa, Oceania]: ')
    chosen_country = input('Choose specific country to show population: ')
    if chosen_region == '':
        if chosen_country == '':
            for row in data:
                for key, value in row.items():
                    with open('filtered_data.json', 'w') as file:
                        json.dump(f'{key}: {value}\n', file, indent=4)
        else:
            for row in data:
                if chosen_country in row.values():
                    for key, value in row.items():
                        with open('filtered_data.json', 'w') as file:
                            json.dump(f'{key}: {value}\n', file, indent=4)
    else:
        final_row = []
        for row in data:
            if chosen_region in region_filter and chosen_region in row.values():
                final_row.append(row)
        with open('filtered_data.json', 'w') as file:
            json.dump(final_row, file, indent=4)
            file.write('\n')