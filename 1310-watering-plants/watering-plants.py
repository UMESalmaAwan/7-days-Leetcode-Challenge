class Solution(object):
    def wateringPlants(self, steps, watercapacity):
        total_steps = 0 # Initialize the total steps needed
        watering_can = watercapacity # Initialize the watering can
        n = len(steps)
        for steps_to_plant in range(n): # Iterate through each plant
            if watering_can < steps[steps_to_plant]: # Check if the watering can has enough water for the current plant
                watering_can = watercapacity # Refill the watering can
                total_steps +=  2 * steps_to_plant # Add 2 steps to the total for refilling the watering can
            watering_can -= steps[steps_to_plant] # Subtract the water used for watering the plant
            total_steps += 1 # Add 1 step to the total for moving to the next plant
        return total_steps # Return the total steps needed