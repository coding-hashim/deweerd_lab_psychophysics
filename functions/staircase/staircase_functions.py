'''
@author Ibrahim Che Hashim
@email coding.hashim@gmail.com

Script containing functions for staircases for the DeWeerd Lab Psychophysics Software

Last edited: 19/04/2020 by Ibrahim Che Hashim
Saved on github under https://github.com/coding-hashim/deweerdlab_psychophysics_software
'''


# This function creates all the changes in orientation required by the user. The orientations will be used to modify the 
# reference orientation set by the user.
def create_orientation_list(maximum_value, division_value, length_list,):
    orientation_list = [float(maximum_value)/(float(x)*float(division_value)) if x != 0 else float(maximum_value) for x in range(0, length_list)]
    return orientation_list
    
    
# This function creates and returns two empty lists.
def reset_staircase_counters():  # sets both list counters back to empty
        staircase_counter_1 = []
        staircase_counter_2 = []
        return staircase_counter_1, staircase_counter_2


# This function updates the staircase counters and decides whether the staircase should be moving up or down based on the 
# number of correct and wrong answer a participant has given.
def staircase_count_update(staircase_counter_down, staircase_counter_up, n_down, n_up, response):
    if response == 1:  # if correct response
        staircase_counter_down.append(1)
    elif response == -1:  # if wrong response
        staircase_counter_up.append(1)
        
    if sum(staircase_counter_down) == n_down:  # if correct answers is equal to number down return down direction
        movement_direction = 'down'
        staircase_counter_down, staircase_counter_up = reset_staircase_counters()  # if wrong answers is equal to number up return down direction
    elif sum(staircase_counter_up) == n_up:
        movement_direction = 'up'
        staircase_counter_down, staircase_counter_up = reset_staircase_counters()
    else:
        movement_direction = 'no_change'  # if neither of two conditions above have been achieved
        
    return(staircase_counter_down, staircase_counter_up, movement_direction)
