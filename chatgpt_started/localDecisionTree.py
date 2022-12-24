#CHAT GPT generated
import numpy as np

# Set of units and structures that can be built
units = {
    'worker': {'cost': 50, 'build_time': 5},
    'marine': {'cost': 50, 'build_time': 10},
    'special_worker': {'cost': 100, 'build_time': 15}
}
structures = {
    'supply_depot': {'cost': 100, 'build_time': 10, 'required_structures': ['barracks']},
    'barracks': {'cost': 150, 'build_time': 15}
}

# Set of actions that can be taken at each timestep
actions = []
for unit_name, unit_info in units.items():
    actions.append(f'build_{unit_name}')
for structure_name, structure_info in structures.items():
    actions.append(f'build_{structure_name}')

# Initialize variables
money = 50
units_in_progress = {}
units_count = {unit_name: 0 for unit_name in units}
structures_in_progress = {}
structures_count = {structure_name: 0 for structure_name in structures}

# Set of conditions that must be met to take certain actions
conditions = {}
for unit_name, unit_info in units.items():
    conditions[f'build_{unit_name}'] = lambda unit_name=unit_name: money >= unit_info['cost'] and unit_name not in units_in_progress
for structure_name, structure_info in structures.items():
    def condition(structure_name=structure_name):
        required_structures_present = all(structures_count[required_structure] > 0 for required_structure in structure_info['required_structures'])
        return money >= structure_info['cost'] and structure_name not in structures_in_progress and required_structures_present
    conditions[f'build_{structure_name}'] = condition

# Main loop
for t in range(100):
    # Update units and structures in progress
    for unit_name, build_time in units_in_progress.items():
        if build_time == 0:
            del units_in_progress[unit_name]
            units_count[unit_name] += 1
        else:
            units_in_progress[unit_name] -= 1
    for structure_name, build_time in structures_in_progress.items():
        if build_time == 0:
            del structures_in_progress[structure_name]
            structures_count[structure_name] += 1
        else:
            structures_in_progress[structure_name] -= 1

    # Increase money based on the number of workers
    money += units_count['worker']

    # Choose the best action according to the decision tree
    best_action = None
    best_reward = -float('inf')
    for action in actions:
        # Check if the conditions for the action are met
        if not conditions[action]():
            continue

        # Calculate the reward for the action
        reward = 0
        if action.startswith('build_'):
            unit_or_structure_name = action[len('build_'):]
            if unit_or_structure_name in units:
                reward += units[unit_or_structure_name]['build_time']
            elif unit_or_structure_name in structures:
                reward += structures[unit_or_structure_name]['build_time']

        # Update the best action if the reward is higher
        if reward > best_reward:
            best_action = action
            best_reward = reward

    # Take the best action and update the variables
    if best_action is not None:
        if best_action.startswith('build_'):
            unit_or_structure_name = best_action[len('build_'):]
            if unit_or_structure_name in units:
                money -= units[unit_or_structure_name]['cost']
                units_in_progress[unit_or_structure_name] = units[unit_or_structure_name]['build_time']
            elif unit_or_structure_name in structures:
                money -= structures[unit_or_structure_name]['cost']
                structures_in_progress[unit_or_structure_name] = structures[unit_or_structure_name]['build_time']

print(units_count)
print(structures_count)
