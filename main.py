import wikipedia_service
import html_service
import animal_divider_service
from config import *


wikipedia_table = wikipedia_service.get_wikipedia_table(config['wikipedia_page'], 1)
if wikipedia_table is None:
    exit('Sorry! The table does not exists in the page you requested!')

dictionary = animal_divider_service.generate_reverse_dictionary_by_table(wikipedia_table, config['key_column_name'], config['values_column_name'])

all_values = []
for key, value in dictionary.items():
    for item in value:
        all_values.append(item.split()[0]) # We need only the first word as a name
all_values = list(set(all_values)) # Make the list to be distinct

html_service.insert_data_to_base_template(dictionary, config['download_path'])
wikipedia_service.download_multiple_wikipedia_main_images(all_values, config['download_path'], config['threads_count'])

