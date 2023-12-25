import numpy as np
import pandas as pd
import math




def calculate_average_walking_distance(shelter_density):
    if shelter_density <= 0:
        raise ValueError("Shelter density must be greater than 0")
    average_walking_distance = 1 / (2 * math.sqrt(shelter_density))
    return average_walking_distance




