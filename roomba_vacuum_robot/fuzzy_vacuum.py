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
      * Universe: What is the water level, on a scale of 0 to 6?
      * Fuzzy set: low, medium, high
* Consequents (Outputs)
   - `motor speed`
      * Universe: How fast do motors rotate per minute, on a scale of 0 to 10
      * Fuzzy set: slow, average, fast
   - `time per tile`
      * Universe: How much time does a robot spend on one tile, on a scale of 0 to 4
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
# Antecedents
cleanliness = ctrl.Antecedent(np.arange(0, 11, 1), 'cleanliness')
water_level = ctrl.Antecedent(np.arange(0, 7, 1), 'water_level')
battery_level = ctrl.Antecedent(np.arange(0, 100, 1), 'battery_level')
# Consequents
motor_speed = ctrl.Consequent(np.arange(0, 11, 1), 'motor_speed')
time_per_tile = ctrl.Consequent(np.arange(0, 5, 1), 'time_per_tile')

# Antecedents
cleanliness['very_dirty'] = fuzz.trimf(cleanliness.universe, [0, 0, 3])
cleanliness['dirty'] = fuzz.trimf(cleanliness.universe, [0, 3, 7])
cleanliness['little_dirty'] = fuzz.trimf(cleanliness.universe, [3, 7, 10])
cleanliness['clean'] = fuzz.trimf(cleanliness.universe, [7, 10, 10])

water_level['low'] = fuzz.trimf(water_level.universe, [0, 0, 3])
water_level['medium'] = fuzz.trimf(water_level.universe, [0, 3, 6])
water_level['high'] = fuzz.trimf(water_level.universe, [3, 6, 6])

battery_level['low'] = fuzz.trimf(battery_level.universe, [0, 0, 50])
battery_level['medium'] = fuzz.trimf(battery_level.universe, [0, 50, 100])
battery_level['high'] = fuzz.trimf(battery_level.universe, [50, 100, 100])

# Consequents
motor_speed['low'] = fuzz.trimf(motor_speed.universe, [0, 0, 5])
motor_speed['medium'] = fuzz.trimf(motor_speed.universe, [0, 5, 10])
motor_speed['high'] = fuzz.trimf(motor_speed.universe, [5, 10, 10])

time_per_tile['short'] = fuzz.trimf(time_per_tile.universe, [0, 0, 2])
time_per_tile['average'] = fuzz.trimf(time_per_tile.universe, [0, 2, 4])
time_per_tile['long'] = fuzz.trimf(time_per_tile.universe, [2, 4, 4])


# Graph showing
cleanliness.view()
water_level.view()
battery_level.view()

motor_speed.view()
time_per_tile.view()

"""
Fuzzy rules
-----------

Now, to make these triangles useful, we define the *fuzzy relationship*
between input and output variables. For the purposes of our example, consider
three simple rules:

* Rules
   - IF the *cleanliness* is very dirty *and* the *battery level* and *water level*
     is high,
     THEN the motor_speed will be high and time_per_tile will be long and water disposal will be high.
   - IF the *cleanliness* is dirty and water level is high, THEN the motor speed and time per tile and water dispense will be medium will be average.
   - IF the *cleanliness* is a little dirty *or* the *battery level* is medium
     THEN the motor speed will be low and time per tile will be medium.
   - IF the *cleanliness* is clean *or* the *battery level* is low
     THEN the motor speed will be very low and time per tile will be short.

Most people would agree on these rules, but the rules are fuzzy. Mapping the
imprecise rules into a defined, actionable tip is a challenge. This is the
kind of task at which fuzzy logic excels.
"""
motor_rule1 = ctrl.Rule(cleanliness['very_dirty'] & battery_level['high'], motor_speed['high'])
motor_rule2 = ctrl.Rule(cleanliness['dirty'], motor_speed['medium'])
motor_rule3 = ctrl.Rule(cleanliness['little_dirty'] | battery_level['medium'], motor_speed['low'])
motor_rule4 = ctrl.Rule(cleanliness['clean'] | battery_level['low'], motor_speed['low'])

motor_speed_ctrl = ctrl.ControlSystem([motor_rule1, motor_rule2, motor_rule3, motor_rule4])

motor_speed_simulation = ctrl.ControlSystemSimulation(motor_speed_ctrl)

time_per_tile_rule1 = ctrl.Rule(cleanliness['very_dirty'] & water_level['low'], time_per_tile['long'])
time_per_tile_rule2 = ctrl.Rule(cleanliness['very_dirty'] & water_level['medium'], time_per_tile['long'])
time_per_tile_rule3 = ctrl.Rule(cleanliness['very_dirty'] & water_level['high'], time_per_tile['average'])
time_per_tile_rule4 = ctrl.Rule(cleanliness['dirty'] & water_level['low'], time_per_tile['long'])
time_per_tile_rule5 = ctrl.Rule(cleanliness['dirty'] & water_level['medium'], time_per_tile['average'])
time_per_tile_rule6 = ctrl.Rule(cleanliness['dirty'] & water_level['high'], time_per_tile['average'])
time_per_tile_rule7 = ctrl.Rule(cleanliness['little_dirty'] & water_level['low'], time_per_tile['average'])
time_per_tile_rule8 = ctrl.Rule(cleanliness['little_dirty'] & water_level['medium'], time_per_tile['average'])
time_per_tile_rule9 = ctrl.Rule(cleanliness['little_dirty'] & water_level['high'], time_per_tile['short'])
time_per_tile_rule10 = ctrl.Rule(cleanliness['clean'] & water_level['low'], time_per_tile['average'])
time_per_tile_rule11 = ctrl.Rule(cleanliness['clean'] & water_level['medium'], time_per_tile['short'])
time_per_tile_rule12 = ctrl.Rule(cleanliness['clean'] & water_level['high'], time_per_tile['short'])

time_per_tile_ctrl = ctrl.ControlSystem([time_per_tile_rule1, time_per_tile_rule2, time_per_tile_rule3,
                                         time_per_tile_rule4, time_per_tile_rule5, time_per_tile_rule6,
                                         time_per_tile_rule7, time_per_tile_rule8, time_per_tile_rule9,
                                         time_per_tile_rule10, time_per_tile_rule11, time_per_tile_rule12])

time_per_tile_simulation = ctrl.ControlSystemSimulation(time_per_tile_ctrl)

cleanliness_input = 3
water_level_input = 3
battery_level_input = 75

motor_speed_simulation.input['cleanliness'] = cleanliness_input
motor_speed_simulation.input['battery_level'] = battery_level_input

time_per_tile_simulation.input['cleanliness'] = cleanliness_input
time_per_tile_simulation.input['water_level'] = water_level_input

motor_speed_simulation.compute()
time_per_tile_simulation.compute()

print("Motor speed: " + str(motor_speed_simulation.output['motor_speed']))
print("Time per tile: " + str(time_per_tile_simulation.output['time_per_tile']))
motor_speed.view(sim=motor_speed_simulation)
time_per_tile.view(sim=time_per_tile_simulation)

plt.show()
