#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on Mon Sep 25 13:51:07 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'WythoffsHumanExp'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/Jack/Desktop/PNC/CoAx/WythoffsHumanExp/WythoffsHumanExp_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "setup_instruct" ---
# Run 'Begin Experiment' code from setup_code
# Make game board tiles for rendering later

squares = []

for row in range(14):
    for col in range(14):
        
        if (row + col) % 2 == 0:
            color = 'lightgray'
        else:
            color = 'darkgray'
        
        x_loc = ((14 - row) - 7.5) / 16
        y_loc = (col - 6.5) / 16
        
        squares.append(
            visual.Rect(
                win = win,
                width = 1/16,
                height = 1/16,
                pos = (x_loc, y_loc),
                fillColor = color))

# --- Initialize components for Routine "countdown" ---
countdown_text = visual.TextStim(win=win, name='countdown_text',
    text='',
    font='Open Sans',
    pos=(0, 0.465), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
blue_piece = visual.ShapeStim(
    win=win, name='blue_piece',
    size=(1/18, 1/18), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=1.0, depth=-2.0, interpolate=True)
red_piece = visual.ShapeStim(
    win=win, name='red_piece',
    size=(1/18, 1/18), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=1.0, depth=-3.0, interpolate=True)

# --- Initialize components for Routine "select_move" ---
piece = visual.ShapeStim(
    win=win, name='piece',
    size=(1/18, 1/18), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=None, depth=-1.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Your turn',
    font='Open Sans',
    pos=(0, 0.465), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "make_move" ---
moving_piece = visual.ShapeStim(
    win=win, name='moving_piece',
    size=(1/18, 1/18), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "npc_wait" ---
npc = visual.ShapeStim(
    win=win, name='npc',
    size=(1/18, 1/18), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "npc_move" ---
moving_npc = visual.ShapeStim(
    win=win, name='moving_npc',
    size=(1/18, 1/18), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "end_pause" ---
end_blue = visual.ShapeStim(
    win=win, name='end_blue',
    size=(1/18, 1/18), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=1.0, depth=-1.0, interpolate=True)
end_red = visual.ShapeStim(
    win=win, name='end_red',
    size=(1/18, 1/18), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=1.0, depth=-2.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "setup_instruct" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
setup_instructComponents = []
for thisComponent in setup_instructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "setup_instruct" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setup_instructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "setup_instruct" ---
for thisComponent in setup_instructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup_instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
games = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='games')
thisExp.addLoop(games)  # add the loop to the experiment
thisGame = games.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisGame.rgb)
if thisGame != None:
    for paramName in thisGame:
        exec('{} = thisGame[paramName]'.format(paramName))

for thisGame in games:
    currentLoop = games
    # abbreviate parameter names if possible (e.g. rgb = thisGame.rgb)
    if thisGame != None:
        for paramName in thisGame:
            exec('{} = thisGame[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "countdown" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from countdown_code
    # board starting spot initialization
    
    import random
    import math
    
    player_won = None
    npc_start = random.choice([True, False])
    
    row = random.randint(0,13)
    col = random.randint(0,13)
    
    while row == col == 0:
        row = random.randint(0,13)
        col = random.randint(0,13)
    
    row_new = row
    col_new = col
    blue_piece.setOpacity(1 - npc_start)
    blue_piece.setPos(((col-6.5)/16, (14-row-7.5)/16))
    red_piece.setOpacity(npc_start)
    red_piece.setPos(((col-6.5)/16, (14-row-7.5)/16))
    # keep track of which components have finished
    countdownComponents = [countdown_text, blue_piece, red_piece]
    for thisComponent in countdownComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "countdown" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from countdown_code
        for square in squares:
            square.draw()
        
        # *countdown_text* updates
        
        # if countdown_text is starting this frame...
        if countdown_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            countdown_text.frameNStart = frameN  # exact frame index
            countdown_text.tStart = t  # local t and not account for scr refresh
            countdown_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(countdown_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'countdown_text.started')
            # update status
            countdown_text.status = STARTED
            countdown_text.setAutoDraw(True)
        
        # if countdown_text is active this frame...
        if countdown_text.status == STARTED:
            # update params
            countdown_text.setText((3 - math.floor(t)), log=False)
        
        # if countdown_text is stopping this frame...
        if countdown_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > countdown_text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                countdown_text.tStop = t  # not accounting for scr refresh
                countdown_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'countdown_text.stopped')
                # update status
                countdown_text.status = FINISHED
                countdown_text.setAutoDraw(False)
        
        # *blue_piece* updates
        
        # if blue_piece is starting this frame...
        if blue_piece.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blue_piece.frameNStart = frameN  # exact frame index
            blue_piece.tStart = t  # local t and not account for scr refresh
            blue_piece.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blue_piece, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blue_piece.started')
            # update status
            blue_piece.status = STARTED
            blue_piece.setAutoDraw(True)
        
        # if blue_piece is active this frame...
        if blue_piece.status == STARTED:
            # update params
            pass
        
        # if blue_piece is stopping this frame...
        if blue_piece.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blue_piece.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                blue_piece.tStop = t  # not accounting for scr refresh
                blue_piece.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blue_piece.stopped')
                # update status
                blue_piece.status = FINISHED
                blue_piece.setAutoDraw(False)
        
        # *red_piece* updates
        
        # if red_piece is starting this frame...
        if red_piece.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red_piece.frameNStart = frameN  # exact frame index
            red_piece.tStart = t  # local t and not account for scr refresh
            red_piece.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_piece, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'red_piece.started')
            # update status
            red_piece.status = STARTED
            red_piece.setAutoDraw(True)
        
        # if red_piece is active this frame...
        if red_piece.status == STARTED:
            # update params
            pass
        
        # if red_piece is stopping this frame...
        if red_piece.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > red_piece.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                red_piece.tStop = t  # not accounting for scr refresh
                red_piece.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'red_piece.stopped')
                # update status
                red_piece.status = FINISHED
                red_piece.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in countdownComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "countdown" ---
    for thisComponent in countdownComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # set up handler to look after randomisation of conditions etc
    turns = data.TrialHandler(nReps=13.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='turns')
    thisExp.addLoop(turns)  # add the loop to the experiment
    thisTurn = turns.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTurn.rgb)
    if thisTurn != None:
        for paramName in thisTurn:
            exec('{} = thisTurn[paramName]'.format(paramName))
    
    for thisTurn in turns:
        currentLoop = turns
        # abbreviate parameter names if possible (e.g. rgb = thisTurn.rgb)
        if thisTurn != None:
            for paramName in thisTurn:
                exec('{} = thisTurn[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "select_move" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        if npc_start:
            continueRoutine = False
        
        row = row_new
        col = col_new
        piece.setPos(((col-6.5)/16, (14-row-7.5)/16))
        # setup some python lists for storing info about the mouse
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        select_moveComponents = [piece, mouse, text]
        for thisComponent in select_moveComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "select_move" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code
            if mouse.getPressed()[0] == 1:
                mouse_x, mouse_y = mouse.getPos()
                row_new = round(0 - ((mouse_y * 16) + 7.5 - 14))
                col_new = round((mouse_x * 16) + 6.5)
                if row_new <= row and col_new <= col:
                    if row_new >= 0 and col_new >= 0:
                        if row_new==row or col_new==col or row-row_new == col-col_new:
                            continueRoutine = False
            
            for square in squares:
                square.draw()
            
            # *piece* updates
            
            # if piece is starting this frame...
            if piece.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                piece.frameNStart = frameN  # exact frame index
                piece.tStart = t  # local t and not account for scr refresh
                piece.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(piece, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'piece.started')
                # update status
                piece.status = STARTED
                piece.setAutoDraw(True)
            
            # if piece is active this frame...
            if piece.status == STARTED:
                # update params
                pass
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in select_moveComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "select_move" ---
        for thisComponent in select_moveComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for turns (TrialHandler)
        # the Routine "select_move" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "make_move" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from move_code
        if npc_start:
            npc_start = False
            continueRoutine = False
        # keep track of which components have finished
        make_moveComponents = [moving_piece]
        for thisComponent in make_moveComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "make_move" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from move_code
            for square in squares:
                square.draw()
            
            # *moving_piece* updates
            
            # if moving_piece is starting this frame...
            if moving_piece.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                moving_piece.frameNStart = frameN  # exact frame index
                moving_piece.tStart = t  # local t and not account for scr refresh
                moving_piece.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(moving_piece, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'moving_piece.started')
                # update status
                moving_piece.status = STARTED
                moving_piece.setAutoDraw(True)
            
            # if moving_piece is active this frame...
            if moving_piece.status == STARTED:
                # update params
                moving_piece.setPos(((((1-t)*col+t*col_new)-6.5)/16, (14-((1-t)*row+t*row_new)-7.5)/16), log=False)
            
            # if moving_piece is stopping this frame...
            if moving_piece.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > moving_piece.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    moving_piece.tStop = t  # not accounting for scr refresh
                    moving_piece.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'moving_piece.stopped')
                    # update status
                    moving_piece.status = FINISHED
                    moving_piece.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in make_moveComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "make_move" ---
        for thisComponent in make_moveComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from move_code
        if row_new == col_new == 0:
            player_won = True
            turns.finished = True
            continueRoutine = False
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "npc_wait" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from wait_code
        if turns.finished:
            continueRoutine = False
        
        row = row_new
        col = col_new
        
        # select random opponent move
        moves = []
        
        for r in range (row): # vertical moves
            moves.append((r, col))
            
        for c in range (col): # horiz moves
            moves.append((row, c))
            
        for d in range(1, min(row, col) + 1): # diag moves
            moves.append((row - d, col - d))
        
        import random
        
        if len(moves) > 0:
            (row_new, col_new) = random.choice(moves)
        npc.setPos(((col-6.5)/16, (14-row-7.5)/16))
        # keep track of which components have finished
        npc_waitComponents = [npc]
        for thisComponent in npc_waitComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "npc_wait" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.25:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from wait_code
            for square in squares:
                square.draw()
            
            # *npc* updates
            
            # if npc is starting this frame...
            if npc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                npc.frameNStart = frameN  # exact frame index
                npc.tStart = t  # local t and not account for scr refresh
                npc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(npc, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'npc.started')
                # update status
                npc.status = STARTED
                npc.setAutoDraw(True)
            
            # if npc is active this frame...
            if npc.status == STARTED:
                # update params
                pass
            
            # if npc is stopping this frame...
            if npc.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > npc.tStartRefresh + 1.25-frameTolerance:
                    # keep track of stop time/frame for later
                    npc.tStop = t  # not accounting for scr refresh
                    npc.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'npc.stopped')
                    # update status
                    npc.status = FINISHED
                    npc.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in npc_waitComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "npc_wait" ---
        for thisComponent in npc_waitComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.250000)
        
        # --- Prepare to start Routine "npc_move" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from npc_code
        if turns.finished:
            continueRoutine = False
        # keep track of which components have finished
        npc_moveComponents = [moving_npc]
        for thisComponent in npc_moveComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "npc_move" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from npc_code
            for square in squares:
                square.draw()
            
            # *moving_npc* updates
            
            # if moving_npc is starting this frame...
            if moving_npc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                moving_npc.frameNStart = frameN  # exact frame index
                moving_npc.tStart = t  # local t and not account for scr refresh
                moving_npc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(moving_npc, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'moving_npc.started')
                # update status
                moving_npc.status = STARTED
                moving_npc.setAutoDraw(True)
            
            # if moving_npc is active this frame...
            if moving_npc.status == STARTED:
                # update params
                moving_npc.setPos(((((1-t)*col+t*col_new)-6.5)/16, (14-((1-t)*row+t*row_new)-7.5)/16), log=False)
            
            # if moving_npc is stopping this frame...
            if moving_npc.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > moving_npc.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    moving_npc.tStop = t  # not accounting for scr refresh
                    moving_npc.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'moving_npc.stopped')
                    # update status
                    moving_npc.status = FINISHED
                    moving_npc.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in npc_moveComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "npc_move" ---
        for thisComponent in npc_moveComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from npc_code
        if row_new == col_new == 0:
            if player_won == None:
                player_won = False
            turns.finished = True
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 13.0 repeats of 'turns'
    
    
    # --- Prepare to start Routine "end_pause" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from end_code
    row = row_new
    col = col_new
    end_blue.setOpacity(player_won)
    end_blue.setPos(((col-6.5)/16, (14-row-7.5)/16))
    end_red.setOpacity(1 - player_won)
    end_red.setPos(((col-6.5)/16, (14-row-7.5)/16))
    # keep track of which components have finished
    end_pauseComponents = [end_blue, end_red]
    for thisComponent in end_pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end_pause" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from end_code
        for square in squares:
            square.draw()
        
        # *end_blue* updates
        
        # if end_blue is starting this frame...
        if end_blue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_blue.frameNStart = frameN  # exact frame index
            end_blue.tStart = t  # local t and not account for scr refresh
            end_blue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_blue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_blue.started')
            # update status
            end_blue.status = STARTED
            end_blue.setAutoDraw(True)
        
        # if end_blue is active this frame...
        if end_blue.status == STARTED:
            # update params
            pass
        
        # if end_blue is stopping this frame...
        if end_blue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_blue.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                end_blue.tStop = t  # not accounting for scr refresh
                end_blue.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'end_blue.stopped')
                # update status
                end_blue.status = FINISHED
                end_blue.setAutoDraw(False)
        
        # *end_red* updates
        
        # if end_red is starting this frame...
        if end_red.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_red.frameNStart = frameN  # exact frame index
            end_red.tStart = t  # local t and not account for scr refresh
            end_red.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_red, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_red.started')
            # update status
            end_red.status = STARTED
            end_red.setAutoDraw(True)
        
        # if end_red is active this frame...
        if end_red.status == STARTED:
            # update params
            pass
        
        # if end_red is stopping this frame...
        if end_red.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_red.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                end_red.tStop = t  # not accounting for scr refresh
                end_red.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'end_red.stopped')
                # update status
                end_red.status = FINISHED
                end_red.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end_pause" ---
    for thisComponent in end_pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'games'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
