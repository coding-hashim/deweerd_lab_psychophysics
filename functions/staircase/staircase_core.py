from psychopy import visual, event
import staircase_functions

# set staircase values
number_reversals = 1
number_trials = 5


# create orientation list and setting reference orientation_list
reference_orientation = -45
ori_list_length = 28
ori_list_max = 22.5
ori_list_div = 1.2
orientation_list = staircase_functions.create_orientation_list(ori_list_max, ori_list_div, ori_list_length)


# create window and stimulus
win = visual.Window([1600,900],allowGUI=True, monitor='testMonitor', units='deg', fullscr = True) # This defines the parameters for the WINDOW where stimuli are shown

fix_neutral = visual.GratingStim(win, color = [1,1,1], colorSpace = 'rgb', tex = None, mask = 'circle', units = 'cm', size = 0.2, pos = (0, 0)) # Paramters of FIXATION DOT continuously presented
fix_correct = visual.GratingStim(win, color = [0,1,0], colorSpace = 'rgb', tex = None, mask = 'circle', units = 'cm', size = 0.2, pos = (0, 0)) # Paramters of FIXATION DOT continuously presented
fix_wrong = visual.GratingStim(win, color = [1,0,0], colorSpace = 'rgb', tex = None, mask = 'circle', units = 'cm', size = 0.2, pos = (0, 0)) # Paramters of FIXATION DOT continuously presented

# set both staircase counters to []
staircase_up, staircase_down = staircase_functions.reset_staircase_counters()  


while number_reversals != 0 and number_trials != 0:
    
    grating_ori = 22.5
    grating = visual.GratingStim(win,contrast = 1, phase = 1, tex = 'sin', units = 'cm', mask = 'circle', sf = 2.4, size = 4, ori = grating_ori, pos=(4.5, 4.5))
    
    fix_neutral.draw()
    grating.draw()
    win.flip()
    event.waitKeys()

    
    
    number_trials -= 1
