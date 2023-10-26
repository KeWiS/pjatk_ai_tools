import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


"""
* Antecednets (Inputs)
   - `cleanliness`
      * Universe (ie, crisp value range): How dirty is a tile on the floor, 
      on a scale of 0 to 10?
      * Fuzzy set (ie, fuzzy value range): very dirty, dirty, little dirty, clean
   - `battery level`
      * Universe: How much battery has the robot left, on a scale of 0 to 100?
      * Fuzzy set: low, medium, high
   - `water level`
      * Universe: What is the water level, on a scale of 0 to 5?
      * Fuzzy set: low, medium, high
* Consequents (Outputs)
   - `motor speed`
      * Universe: How fast do motors rotate per minute, on a scale of 0 to 10
      * Fuzzy set: slow, average, fast
   - `water dispense?`
      * Universe: How much water will be disposed, on a scale of 0 to 10
      * Fuzzy set: low, medium, high
   - `time per tile`
      * Universe: How much time does a robot spend on one tile, on a scale of 0 to 3
      * Fuzzy set: short, average, long
* Rules
   - IF the *cleanliness* is very dirty *and* the *battery level* and *water level*
     is high,
     THEN the motor_speed will be high and time_per_tile will be long and water disposal will be high.
   - IF the *cleanliness* is dirty and water level is high, THEN the motor speed and time per tile and water dispense will be medium will be average.
   - IF the *cleanliness* is a little dirty *or* the *battery level* is medium
     THEN the motor speed will be low and time per tile will be medium.
   - IF the *cleanliness* is clean *or* the *battery level* is low
     THEN the motor speed will be very low and time per tile will be short.
* Usage
   - If I tell this controller that I rated:
      * the cleanliness as 1.5, and
      * the battery level as 95,
   - it would recommend I leave:
      * a x motor speed.
"""

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

