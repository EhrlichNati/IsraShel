import folium
import pandas as pd
import os

class City:

    def __init__(self, city_demographic_data, shelters_data_tables: list[pd.DataFrame]):

        self.data = shelters_data_tables
        self.population = city_demographic_data["population"]
        self.area = city_demographic_data["area"]
        self.num_shelters = self.num_of_shelters(shelters_data_tables)
        self.data_categories = self.create_category_variable_list(shelters_data_tables)





    def create_category_variable_list(self, shelters_data_tables):
        unique_columns = set()
        for frame in shelters_data_tables:
            unique_columns.update(frame.columns)
        return list(unique_columns).sort()


    def num_of_shelters(self,shelters_data_tables ):
        total_locations = 0
        for frame in shelters_data_tables:
                try:
                    total_locations += len(frame)
                except Exception as e:
                    print(f"Error reading:")
        return total_locations









