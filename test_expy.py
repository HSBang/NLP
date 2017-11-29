# -*- coding: utf-8 -*-
import expyriment as xpy


####################################
## Part 1: Set up any global set-ups
####################################
xpy.control.set_develop_mode(True)
xpy.misc.list_fonts()


####################################
## Part 2: Create design(blocks, trials), stimuli(and put them into trials), I/O devices (like button boxes etc.)
####################################
#exp = xpy.design.Experiment(name="First Experiment")
exp = xpy.control.initialize()

## Set up the first block
block_one = xpy.design.Block(name="A name for the first block")

trial_one = xpy.design.Trial()
stim = xpy.stimuli.TextLine(text="I'm a stimulus in Block 1, Trial 1", text_font="Courier")
stim.preload()
trial_one.add_stimulus(stim)

trial_two = xpy.design.Trial()
stim = xpy.stimuli.TextLine(text="두 번째 블락, 첫 번째 시행")
stim.preload()
trial_two.add_stimulus(stim)

block_one.add_trial(trial_one)
block_one.add_trial(trial_two)
exp.add_block(block_one)

## Set up the second block
block_two = xpy.design.Block(name="A name for the second block")

trial_one = xpy.design.Trial()
stim = xpy.stimuli.TextLine(text="I'm a stimulus in Block 2, Trial 1")
stim.preload()
trial_one.add_stimulus(stim)

trial_two = xpy.design.Trial()
stim = xpy.stimuli.TextLine(text="I am a stimulus in Block 2, Trial 2")
stim.preload()
trial_two.add_stimulus(stim)

block_two.add_trial(trial_one)
block_two.add_trial(trial_two)
exp.add_block(block_two)


#####################################
## Part 3: Experiment conduction
## Loop over blocks and trials, present stimuli and get user input
#####################################
xpy.control.start()

for block in exp.blocks:
	for trial in block.trials:
		trial.stimuli[0].present()
		# Wait until one of the specified respones are given
		# This function returns the key pressed and RT
		key, rt = exp.keyboard.wait([xpy.misc.constants.K_LEFT, xpy.misc.constants.K_RIGHT])
		# Add the elements in the list on the data file id of trial is automatically set when the trial is added to a block
		exp.data.add([block.name, trial.id, key, rt])

xpy.control.end()
