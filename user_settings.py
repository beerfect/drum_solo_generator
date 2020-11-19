# SETTINGS
user_seed = "Roman Z"
bars_in_etude = 8 # number of measures in a piece 4/8/16/32
beats_in_bar = [2,3] # possible time signatures 1/2/3/4/5/6/7/8/9
proportion_of_pauses = 10 # 0-100
proportion_of_accents = 10 # 0-100
proportion_of_flams = 0 # 0-100
maximum_flams_in_a_row = 1 # 1-4
proportion_of_doubles = 0 # 0-100
maximum_number_of_notes_played_with_one_hand_in_a_row = 1 # 1-4
starting_hand = ['R'] # ['R', 'L'] ['R'], ['L']

# al least one of them == True
enabled_notes = {
    'eight': [True, 2],
    'triplets': [False, 3],
    'sixteen': [True, 4],
    'quitniplets': [False, 5],
    'sixteen_triplets': [False, 6],
    'septoles': [False, 7],
    
    # will be enabled automatically
    'two_sixteenths_with_triplet': [False, 5],
}

# automatic enabling 'two_sixteenths_with_triplet'
if enabled_notes['sixteen'][0] and enabled_notes['sixteen_triplets'][0]:
    enabled_notes['two_sixteenths_with_triplet'][0] = True


draw_reverse_applicature = {
    'enabled': False,
    'R': 'L',
    'L': 'R'
}

print('COMPLETED: user_settings.py')

