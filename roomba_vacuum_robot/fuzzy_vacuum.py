import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

cleanliness = ctrl.Antecedent(np.arange(0, 11, 1), 'cleanliness')
#is_next_tile_obstacle = ctrl.Antecedent(np.arange(0, 2, 1), 'is_next_tile_obstacle')
#water_level = ctrl.Antecedent(np.arange(0, 3, 1), 'water_level')
battery_level = ctrl.Antecedent(np.arange(0, 100, 1), 'battery_level')
#direction = ctrl.Consequent(np.arange(0, 5, 1), 'direction')
#water_dispense = ctrl.Consequent(np.arange(0, 3, 1), 'water_dispense')
motor_speed = ctrl.Consequent(np.arange(0, 11, 1), 'motor_speed')
#time_per_tile = ctrl.Consequent(np.arange(0, 4, 1), 'time_per_tile')

cleanliness['very_dirty'] = fuzz.trimf(cleanliness.universe, [0, 0, 3])
cleanliness['dirty'] = fuzz.trimf(cleanliness.universe, [0, 3, 5])
cleanliness['little_dirty'] = fuzz.trimf(cleanliness.universe, [5, 7, 10])
cleanliness['clean'] = fuzz.trimf(cleanliness.universe, [7, 10, 10])

battery_level['low'] = fuzz.trimf(battery_level.universe, [0, 0, 5])
battery_level['medium'] = fuzz.trimf(battery_level.universe, [0, 5, 10])
battery_level['high'] = fuzz.trimf(battery_level.universe, [5, 10, 10])



# ew. 1500 obrotów/min max
motor_speed['low'] = fuzz.trimf(motor_speed.universe, [0, 0, 5])
motor_speed['medium'] = fuzz.trimf(motor_speed.universe, [0, 5, 10])
motor_speed['high'] = fuzz.trimf(motor_speed.universe, [5, 10, 10])

# time_per_tile['short'] = fuzz.trimf(time_per_tile.universe, [0, 0, 1])
# time_per_tile['average'] = fuzz.trimf(time_per_tile.universe, [0, 1, 2])
# time_per_tile['long'] = fuzz.trimf(time_per_tile.universe, [1, 2, 2])

# cleanliness['very_dirty'].view()

battery_level.view()

motor_speed.view()

# time_per_tile.view()

