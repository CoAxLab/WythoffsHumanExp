#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on Tue Jan  9 12:21:55 2024
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

# Run 'Before Experiment' code from setup_code
import numpy as np
import pandas as pd

# create tidy DataFrame to hold game record
df = pd.DataFrame()
df['session'] = []
df['section'] = []
df['type'] = []
df['game'] = []
df['ref_game'] = []
df['move_num'] = []
df['player'] = []
df['start_row'] = []
df['start_col'] = []
df['end_row'] = []
df['end_col'] = []
df['RT'] = []
df['DT'] = []
df['winner'] = []
df['chosen_winner'] = []
df = df.astype('object')
#print(df)


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

for row in range(15):
    for col in range(15):
        
        if (row + col) % 2 == 0:
            color = 'lightgray'
        else:
            color = 'darkgray'
        
        x_loc = ((15 - row) - 8) / 17
        y_loc = (col - 7) / 17
        
        squares.append(
            visual.Rect(
                win = win,
                width = 1/17,
                height = 1/17,
                pos = (x_loc, y_loc),
                fillColor = color))
title_text = visual.TextStim(win=win, name='title_text',
    text="Wythoff's Game Experiment",
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=1.3, ori=0.0, 
    color='gold', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
overview_text = visual.TextStim(win=win, name='overview_text',
    text='Welcome! Please read all instructions carefully.\n\nThis experiment will have 4 sections.\nYou will be playing a virtual board game.\nClick the button below for the tutorial.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
start_button = visual.Rect(
    win=win, name='start_button',
    width=(0.2, 0.1)[0], height=(0.2, 0.1)[1],
    ori=0.0, pos=(0, -0.3), anchor='center',
    lineWidth=8.0,     colorSpace='rgb',  lineColor='silver', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
button_label = visual.TextStim(win=win, name='button_label',
    text='begin!',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='grey', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
start_mouse = event.Mouse(win=win)
x, y = [None, None]
start_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "tutorial" ---
board_outline = visual.Rect(
    win=win, name='board_outline',
    width=(15/17, -15/17)[0], height=(15/17, -15/17)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=20.0,     colorSpace='rgb',  lineColor='black', fillColor=None,
    opacity=None, depth=-1.0, interpolate=True)
begin_button = visual.Rect(
    win=win, name='begin_button',
    width=(0.2, 0.1)[0], height=(0.2, 0.1)[1],
    ori=0.0, pos=(0.6, -0.35), anchor='center',
    lineWidth=8.0,     colorSpace='rgb',  lineColor='silver', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
begin_text = visual.TextStim(win=win, name='begin_text',
    text='ready!',
    font='Open Sans',
    pos=(0.6, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='grey', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
tutorial_mouse = event.Mouse(win=win)
x, y = [None, None]
tutorial_mouse.mouseClock = core.Clock()
tutorial_title = visual.TextStim(win=win, name='tutorial_title',
    text='Tutorial',
    font='Open Sans',
    pos=(0, 0.47), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
box_1 = visual.Rect(
    win=win, name='box_1',
    width=(0.3, 2/17)[0], height=(0.3, 2/17)[1],
    ori=0.0, pos=(-15/17/2, 15/17/2), anchor='top-right',
    lineWidth=20.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-6.0, interpolate=True)
text_1 = visual.TextStim(win=win, name='text_1',
    text='1) This is the\ngame board.',
    font='Open Sans',
    pos=(-0.595, 13/17/2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
arrow = visual.ShapeStim(
    win=win, name='arrow', vertices='arrow',
    size=(0.15, 0.15),
    ori=-45.0, pos=(-13.25/17/2, 13.25/17/2), anchor='top-center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=-8.0, interpolate=True)
box_2 = visual.Rect(
    win=win, name='box_2',
    width=(0.35, 2/17)[0], height=(0.35, 2/17)[1],
    ori=0.0, pos=(-17.5/17/2, 7.5/17/2), anchor='center',
    lineWidth=20.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-9.0, interpolate=True)
text_2 = visual.TextStim(win=win, name='text_2',
    text='2) The top-left\nspot is the goal.',
    font='Open Sans',
    pos=(-17.5/17/2, 7.5/17/2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
tutorial_piece = visual.ShapeStim(
    win=win, name='tutorial_piece',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=((7-7)/17, (15-4-8)/17), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=None, depth=-11.0, interpolate=True)
left_arrow = visual.ShapeStim(
    win=win, name='left_arrow', vertices='arrow',
    size=(1/20, 1/20),
    ori=-90.0, pos=((5.75-7)/17, (15-4-8)/17), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=-12.0, interpolate=True)
up_arrow = visual.ShapeStim(
    win=win, name='up_arrow', vertices='arrow',
    size=(1/20, 1/20),
    ori=0.0, pos=((7-7)/17, (15-2.75-8)/17), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=-13.0, interpolate=True)
up_left_arrow = visual.ShapeStim(
    win=win, name='up_left_arrow', vertices='arrow',
    size=(1/20, 1/20),
    ori=-45.0, pos=((6.05-7)/17, (15-3.05-8)/17), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=-14.0, interpolate=True)
box_3 = visual.Rect(
    win=win, name='box_3',
    width=(6/17, 7/17)[0], height=(6/17, 7/17)[1],
    ori=0.0, pos=(8/17/2, 1/17/2), anchor='center',
    lineWidth=20.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-15.0, interpolate=True)
text_3 = visual.TextStim(win=win, name='text_3',
    text='3) This is the\ngame piece. It\ncan move any\nnumber of spots\nup, left, or up-\nleft diagonally.\nIt turns red for\nopponent turns.',
    font='Open Sans',
    pos=(8/17/2, 1/17/2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);
box_4 = visual.Rect(
    win=win, name='box_4',
    width=(4/17, 3.5/17)[0], height=(4/17, 3.5/17)[1],
    ori=0.0, pos=(20/17/2, -4/17/2), anchor='center',
    lineWidth=20.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-17.0, interpolate=True)
text_4 = visual.TextStim(win=win, name='text_4',
    text='4) starting\nspot and\nplayer are\nrandom.',
    font='Open Sans',
    pos=(20/17/2, -4/17/2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-18.0);

# --- Initialize components for Routine "practice_info" ---
title_0 = visual.TextStim(win=win, name='title_0',
    text='Starting three practice games',
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=1.4, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
button_0 = visual.Rect(
    win=win, name='button_0',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=8.0,     colorSpace='rgb',  lineColor='silver', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
button_0_text = visual.TextStim(win=win, name='button_0_text',
    text='proceed',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='gray', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse_0 = event.Mouse(win=win)
x, y = [None, None]
mouse_0.mouseClock = core.Clock()
section_0_text = visual.TextStim(win=win, name='section_0_text',
    text='Click the button below to play three practice games before starting experiment section 1.',
    font='Open Sans',
    pos=(0, 0.15), height=0.05, wrapWidth=1.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

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
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=1.0, depth=-2.0, interpolate=True)
red_piece = visual.ShapeStim(
    win=win, name='red_piece',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=1.0, depth=-3.0, interpolate=True)

# --- Initialize components for Routine "select_move" ---
piece = visual.ShapeStim(
    win=win, name='piece',
    size=(1/19, 1/19), vertices='circle',
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
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=1.0, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "npc_wait" ---
# Run 'Begin Experiment' code from wait_code
import math

optimal_moves_wythoffs = [(0,0),(1,2),(2,1),(3,5),(5,3),(4,7), (7,4),(6,10),(10,6),(8,13),(13,8)]

optimal_moves_nim = []
for i in range(15):
    optimal_moves_nim.append((i,i))

optimal_moves_euclid = []
for r in range(15):
    for c in range(15):
        if  r == c == 0:
            optimal_moves_euclid.append((r,c))
        elif min(r,c) / max(r,c) > (1 + math.sqrt(5)) / 2:
            optimal_moves_euclid.append((r,c))

def euclid_move(pos1, pos2):
    (r1, c1) = pos1
    (r2, c2) = pos2
    
    if r2 >= r1 or c2 >= c1: return False
    
    elif r1 == 0 or c1 == 0:
        
        if r1 == 0 and c2 < c1: return True
        else: return False
        if c1 == 0 and r2 < r1: return True
        else: return False
    
    else:
        if r1 == c1:
            if   r1 == 0 and c2 == c1: return True
            elif c2 == 0 and r2 == r1: return True
            else: return False
        
        if r1 > c1:
            if (r1 - r2) % c1 == 0: return True
            else: return False
        
        if c1 > r1:
            if (c1 - c2) % r1 == 0: return True
            else: return False


npc = visual.ShapeStim(
    win=win, name='npc',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "npc_move" ---
moving_npc = visual.ShapeStim(
    win=win, name='moving_npc',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=1.0, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "end_pause" ---
end_blue = visual.ShapeStim(
    win=win, name='end_blue',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=1.0, depth=-1.0, interpolate=True)
end_red = visual.ShapeStim(
    win=win, name='end_red',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=1.0, depth=-2.0, interpolate=True)

# --- Initialize components for Routine "feedback" ---
feedback_win = visual.TextStim(win=win, name='feedback_win',
    text='YOU WON!',
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0.0, 
    color='gold', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
feedback_lose = visual.TextStim(win=win, name='feedback_lose',
    text='YOU LOST!',
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-2.0);
status_text = visual.TextStim(win=win, name='status_text',
    text='',
    font='Open Sans',
    pos=(0, 0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
button = visual.Rect(
    win=win, name='button',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=8.0,     colorSpace='rgb',  lineColor='silver', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
button_text = visual.TextStim(win=win, name='button_text',
    text='proceed',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='gray', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
next_mouse = event.Mouse(win=win)
x, y = [None, None]
next_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "section_1" ---
title_1 = visual.TextStim(win=win, name='title_1',
    text='Starting Experiment Section 1',
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=1.4, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
button_1 = visual.Rect(
    win=win, name='button_1',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0.0, pos=(0, -0.15), anchor='center',
    lineWidth=8.0,     colorSpace='rgb',  lineColor='silver', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
button_1_text = visual.TextStim(win=win, name='button_1_text',
    text='proceed',
    font='Open Sans',
    pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='gray', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse_1 = event.Mouse(win=win)
x, y = [None, None]
mouse_1.mouseClock = core.Clock()
section_1_text = visual.TextStim(win=win, name='section_1_text',
    text='',
    font='Open Sans',
    pos=(0, 0.075), height=0.05, wrapWidth=0.75, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

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
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=1.0, depth=-2.0, interpolate=True)
red_piece = visual.ShapeStim(
    win=win, name='red_piece',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=1.0, depth=-3.0, interpolate=True)

# --- Initialize components for Routine "select_move" ---
piece = visual.ShapeStim(
    win=win, name='piece',
    size=(1/19, 1/19), vertices='circle',
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
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=1.0, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "npc_wait" ---
# Run 'Begin Experiment' code from wait_code
import math

optimal_moves_wythoffs = [(0,0),(1,2),(2,1),(3,5),(5,3),(4,7), (7,4),(6,10),(10,6),(8,13),(13,8)]

optimal_moves_nim = []
for i in range(15):
    optimal_moves_nim.append((i,i))

optimal_moves_euclid = []
for r in range(15):
    for c in range(15):
        if  r == c == 0:
            optimal_moves_euclid.append((r,c))
        elif min(r,c) / max(r,c) > (1 + math.sqrt(5)) / 2:
            optimal_moves_euclid.append((r,c))

def euclid_move(pos1, pos2):
    (r1, c1) = pos1
    (r2, c2) = pos2
    
    if r2 >= r1 or c2 >= c1: return False
    
    elif r1 == 0 or c1 == 0:
        
        if r1 == 0 and c2 < c1: return True
        else: return False
        if c1 == 0 and r2 < r1: return True
        else: return False
    
    else:
        if r1 == c1:
            if   r1 == 0 and c2 == c1: return True
            elif c2 == 0 and r2 == r1: return True
            else: return False
        
        if r1 > c1:
            if (r1 - r2) % c1 == 0: return True
            else: return False
        
        if c1 > r1:
            if (c1 - c2) % r1 == 0: return True
            else: return False


npc = visual.ShapeStim(
    win=win, name='npc',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "npc_move" ---
moving_npc = visual.ShapeStim(
    win=win, name='moving_npc',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=1.0, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "end_pause" ---
end_blue = visual.ShapeStim(
    win=win, name='end_blue',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=1.0, depth=-1.0, interpolate=True)
end_red = visual.ShapeStim(
    win=win, name='end_red',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=1.0, depth=-2.0, interpolate=True)

# --- Initialize components for Routine "feedback" ---
feedback_win = visual.TextStim(win=win, name='feedback_win',
    text='YOU WON!',
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0.0, 
    color='gold', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
feedback_lose = visual.TextStim(win=win, name='feedback_lose',
    text='YOU LOST!',
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-2.0);
status_text = visual.TextStim(win=win, name='status_text',
    text='',
    font='Open Sans',
    pos=(0, 0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
button = visual.Rect(
    win=win, name='button',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=8.0,     colorSpace='rgb',  lineColor='silver', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
button_text = visual.TextStim(win=win, name='button_text',
    text='proceed',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='gray', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
next_mouse = event.Mouse(win=win)
x, y = [None, None]
next_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "instruct_recall" ---
recall_title = visual.TextStim(win=win, name='recall_title',
    text='Experiment Section 2 Instructions',
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
recall_button = visual.Rect(
    win=win, name='recall_button',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0.0, pos=(0, -0.3), anchor='center',
    lineWidth=8.0,     colorSpace='rgb',  lineColor='silver', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
recall_ready = visual.TextStim(win=win, name='recall_ready',
    text='ready!',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='gray', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
recall_mouse = event.Mouse(win=win)
x, y = [None, None]
recall_mouse.mouseClock = core.Clock()
recall_text = visual.TextStim(win=win, name='recall_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.1, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "instruct_imagine" ---
imagine_title = visual.TextStim(win=win, name='imagine_title',
    text='Experiment Section 2 Instructions',
    font='Open Sans',
    pos=(0, 0.35), height=0.1, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
imagine_button = visual.Rect(
    win=win, name='imagine_button',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0.0, pos=(0, -0.35), anchor='center',
    lineWidth=8.0,     colorSpace='rgb',  lineColor='silver', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
imagine_ready = visual.TextStim(win=win, name='imagine_ready',
    text='ready!',
    font='Open Sans',
    pos=(0, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='gray', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
imagine_mouse = event.Mouse(win=win)
x, y = [None, None]
imagine_mouse.mouseClock = core.Clock()
imagine_text = visual.TextStim(win=win, name='imagine_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.175, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "section_2" ---
title_2 = visual.TextStim(win=win, name='title_2',
    text='Starting Experiment Section 2',
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=1.4, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
button_2 = visual.Rect(
    win=win, name='button_2',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=8.0,     colorSpace='rgb',  lineColor='silver', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
button_2_text = visual.TextStim(win=win, name='button_2_text',
    text='proceed',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='gray', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
section_2_text = visual.TextStim(win=win, name='section_2_text',
    text='',
    font='Open Sans',
    pos=(0, 0.15), height=0.05, wrapWidth=1.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "intervention_countdown" ---
intervention_countdown_text = visual.TextStim(win=win, name='intervention_countdown_text',
    text='',
    font='Open Sans',
    pos=(0, 0.465), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
intervention_blue_piece = visual.ShapeStim(
    win=win, name='intervention_blue_piece',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=1.0, depth=-2.0, interpolate=True)
intervention_red_piece = visual.ShapeStim(
    win=win, name='intervention_red_piece',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=1.0, depth=-3.0, interpolate=True)

# --- Initialize components for Routine "imagination_prompt" ---
prompt_piece = visual.ShapeStim(
    win=win, name='prompt_piece',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "intervention_player_wait" ---
intervention_piece = visual.ShapeStim(
    win=win, name='intervention_piece',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "make_move" ---
moving_piece = visual.ShapeStim(
    win=win, name='moving_piece',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=1.0, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "intervention_npc_wait" ---
intervention_npc = visual.ShapeStim(
    win=win, name='intervention_npc',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "npc_move" ---
moving_npc = visual.ShapeStim(
    win=win, name='moving_npc',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=1.0, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "end_pause" ---
end_blue = visual.ShapeStim(
    win=win, name='end_blue',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=1.0, depth=-1.0, interpolate=True)
end_red = visual.ShapeStim(
    win=win, name='end_red',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=1.0, depth=-2.0, interpolate=True)

# --- Initialize components for Routine "who_won" ---
who_won_title = visual.TextStim(win=win, name='who_won_title',
    text='Who won?',
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
opponent_button = visual.Rect(
    win=win, name='opponent_button',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0.0, pos=(-0.3, 0), anchor='center',
    lineWidth=8.0,     colorSpace='rgb',  lineColor='silver', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
opponent_text = visual.TextStim(win=win, name='opponent_text',
    text='opponent',
    font='Open Sans',
    pos=(-0.3, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='gray', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
me_button = visual.Rect(
    win=win, name='me_button',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0.0, pos=(0.3, 0), anchor='center',
    lineWidth=8.0,     colorSpace='rgb',  lineColor='silver', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
me_text = visual.TextStim(win=win, name='me_text',
    text='me',
    font='Open Sans',
    pos=(0.3, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='gray', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
choice_mouse = event.Mouse(win=win)
x, y = [None, None]
choice_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "section_3" ---
title_3 = visual.TextStim(win=win, name='title_3',
    text='Starting Experiment Section 3',
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=1.4, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
button_3 = visual.Rect(
    win=win, name='button_3',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=8.0,     colorSpace='rgb',  lineColor='silver', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
button_3_text = visual.TextStim(win=win, name='button_3_text',
    text='proceed',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='gray', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
section_3_text = visual.TextStim(win=win, name='section_3_text',
    text='',
    font='Open Sans',
    pos=(0, 0.15), height=0.05, wrapWidth=1.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

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
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=1.0, depth=-2.0, interpolate=True)
red_piece = visual.ShapeStim(
    win=win, name='red_piece',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=1.0, depth=-3.0, interpolate=True)

# --- Initialize components for Routine "select_move" ---
piece = visual.ShapeStim(
    win=win, name='piece',
    size=(1/19, 1/19), vertices='circle',
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
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=1.0, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "npc_wait" ---
# Run 'Begin Experiment' code from wait_code
import math

optimal_moves_wythoffs = [(0,0),(1,2),(2,1),(3,5),(5,3),(4,7), (7,4),(6,10),(10,6),(8,13),(13,8)]

optimal_moves_nim = []
for i in range(15):
    optimal_moves_nim.append((i,i))

optimal_moves_euclid = []
for r in range(15):
    for c in range(15):
        if  r == c == 0:
            optimal_moves_euclid.append((r,c))
        elif min(r,c) / max(r,c) > (1 + math.sqrt(5)) / 2:
            optimal_moves_euclid.append((r,c))

def euclid_move(pos1, pos2):
    (r1, c1) = pos1
    (r2, c2) = pos2
    
    if r2 >= r1 or c2 >= c1: return False
    
    elif r1 == 0 or c1 == 0:
        
        if r1 == 0 and c2 < c1: return True
        else: return False
        if c1 == 0 and r2 < r1: return True
        else: return False
    
    else:
        if r1 == c1:
            if   r1 == 0 and c2 == c1: return True
            elif c2 == 0 and r2 == r1: return True
            else: return False
        
        if r1 > c1:
            if (r1 - r2) % c1 == 0: return True
            else: return False
        
        if c1 > r1:
            if (c1 - c2) % r1 == 0: return True
            else: return False


npc = visual.ShapeStim(
    win=win, name='npc',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "npc_move" ---
moving_npc = visual.ShapeStim(
    win=win, name='moving_npc',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=1.0, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "end_pause" ---
end_blue = visual.ShapeStim(
    win=win, name='end_blue',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=1.0, depth=-1.0, interpolate=True)
end_red = visual.ShapeStim(
    win=win, name='end_red',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=1.0, depth=-2.0, interpolate=True)

# --- Initialize components for Routine "feedback" ---
feedback_win = visual.TextStim(win=win, name='feedback_win',
    text='YOU WON!',
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0.0, 
    color='gold', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
feedback_lose = visual.TextStim(win=win, name='feedback_lose',
    text='YOU LOST!',
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-2.0);
status_text = visual.TextStim(win=win, name='status_text',
    text='',
    font='Open Sans',
    pos=(0, 0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
button = visual.Rect(
    win=win, name='button',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=8.0,     colorSpace='rgb',  lineColor='silver', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
button_text = visual.TextStim(win=win, name='button_text',
    text='proceed',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='gray', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
next_mouse = event.Mouse(win=win)
x, y = [None, None]
next_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "section_4" ---
title_4 = visual.TextStim(win=win, name='title_4',
    text='Starting Experiment Section 4',
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=1.4, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
button_4 = visual.Rect(
    win=win, name='button_4',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=8.0,     colorSpace='rgb',  lineColor='silver', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
button_4_text = visual.TextStim(win=win, name='button_4_text',
    text='proceed',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='gray', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_4.mouseClock = core.Clock()
section_4_text = visual.TextStim(win=win, name='section_4_text',
    text='',
    font='Open Sans',
    pos=(0, 0.15), height=0.05, wrapWidth=1.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

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
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=1.0, depth=-2.0, interpolate=True)
red_piece = visual.ShapeStim(
    win=win, name='red_piece',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=1.0, depth=-3.0, interpolate=True)

# --- Initialize components for Routine "select_move" ---
piece = visual.ShapeStim(
    win=win, name='piece',
    size=(1/19, 1/19), vertices='circle',
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
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=1.0, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "npc_wait" ---
# Run 'Begin Experiment' code from wait_code
import math

optimal_moves_wythoffs = [(0,0),(1,2),(2,1),(3,5),(5,3),(4,7), (7,4),(6,10),(10,6),(8,13),(13,8)]

optimal_moves_nim = []
for i in range(15):
    optimal_moves_nim.append((i,i))

optimal_moves_euclid = []
for r in range(15):
    for c in range(15):
        if  r == c == 0:
            optimal_moves_euclid.append((r,c))
        elif min(r,c) / max(r,c) > (1 + math.sqrt(5)) / 2:
            optimal_moves_euclid.append((r,c))

def euclid_move(pos1, pos2):
    (r1, c1) = pos1
    (r2, c2) = pos2
    
    if r2 >= r1 or c2 >= c1: return False
    
    elif r1 == 0 or c1 == 0:
        
        if r1 == 0 and c2 < c1: return True
        else: return False
        if c1 == 0 and r2 < r1: return True
        else: return False
    
    else:
        if r1 == c1:
            if   r1 == 0 and c2 == c1: return True
            elif c2 == 0 and r2 == r1: return True
            else: return False
        
        if r1 > c1:
            if (r1 - r2) % c1 == 0: return True
            else: return False
        
        if c1 > r1:
            if (c1 - c2) % r1 == 0: return True
            else: return False


npc = visual.ShapeStim(
    win=win, name='npc',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "npc_move" ---
moving_npc = visual.ShapeStim(
    win=win, name='moving_npc',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=1.0, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "end_pause" ---
end_blue = visual.ShapeStim(
    win=win, name='end_blue',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dodgerblue', fillColor='dodgerblue',
    opacity=1.0, depth=-1.0, interpolate=True)
end_red = visual.ShapeStim(
    win=win, name='end_red',
    size=(1/19, 1/19), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='chestnut', fillColor='chestnut',
    opacity=1.0, depth=-2.0, interpolate=True)

# --- Initialize components for Routine "feedback" ---
feedback_win = visual.TextStim(win=win, name='feedback_win',
    text='YOU WON!',
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0.0, 
    color='gold', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
feedback_lose = visual.TextStim(win=win, name='feedback_lose',
    text='YOU LOST!',
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-2.0);
status_text = visual.TextStim(win=win, name='status_text',
    text='',
    font='Open Sans',
    pos=(0, 0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
button = visual.Rect(
    win=win, name='button',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=8.0,     colorSpace='rgb',  lineColor='silver', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
button_text = visual.TextStim(win=win, name='button_text',
    text='proceed',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='gray', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
next_mouse = event.Mouse(win=win)
x, y = [None, None]
next_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "end_screen" ---
end_title = visual.TextStim(win=win, name='end_title',
    text='Experiment sections complete',
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=1.4, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
end_button = visual.Rect(
    win=win, name='end_button',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0.0, pos=(0, -0.35), anchor='center',
    lineWidth=8.0,     colorSpace='rgb',  lineColor='silver', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
end_button_text = visual.TextStim(win=win, name='end_button_text',
    text='done',
    font='Open Sans',
    pos=(0, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='gray', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
end_text = visual.TextStim(win=win, name='end_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
end_mouse = event.Mouse(win=win)
x, y = [None, None]
end_mouse.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "setup_instruct" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from setup_code
import random

npc_starts = [False, True, False]
num_games = len(npc_starts)

game = 0 # initialize game counter
num_wins = 0 # initialize win counter
visibility = 1 # pieces are visible for Section 0/1
section = 0 # variable for experiment section
move_duration = 1 # how long moves take
end_pause_duration = 0.75 # game-end pause amt
# setup some python lists for storing info about the start_mouse
start_mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
setup_instructComponents = [title_text, overview_text, start_button, button_label, start_mouse]
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
    
    # *title_text* updates
    
    # if title_text is starting this frame...
    if title_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        title_text.frameNStart = frameN  # exact frame index
        title_text.tStart = t  # local t and not account for scr refresh
        title_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(title_text, 'tStartRefresh')  # time at next scr refresh
        # update status
        title_text.status = STARTED
        title_text.setAutoDraw(True)
    
    # if title_text is active this frame...
    if title_text.status == STARTED:
        # update params
        pass
    
    # *overview_text* updates
    
    # if overview_text is starting this frame...
    if overview_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        overview_text.frameNStart = frameN  # exact frame index
        overview_text.tStart = t  # local t and not account for scr refresh
        overview_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(overview_text, 'tStartRefresh')  # time at next scr refresh
        # update status
        overview_text.status = STARTED
        overview_text.setAutoDraw(True)
    
    # if overview_text is active this frame...
    if overview_text.status == STARTED:
        # update params
        pass
    
    # *start_button* updates
    
    # if start_button is starting this frame...
    if start_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_button.frameNStart = frameN  # exact frame index
        start_button.tStart = t  # local t and not account for scr refresh
        start_button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_button, 'tStartRefresh')  # time at next scr refresh
        # update status
        start_button.status = STARTED
        start_button.setAutoDraw(True)
    
    # if start_button is active this frame...
    if start_button.status == STARTED:
        # update params
        pass
    
    # *button_label* updates
    
    # if button_label is starting this frame...
    if button_label.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_label.frameNStart = frameN  # exact frame index
        button_label.tStart = t  # local t and not account for scr refresh
        button_label.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_label, 'tStartRefresh')  # time at next scr refresh
        # update status
        button_label.status = STARTED
        button_label.setAutoDraw(True)
    
    # if button_label is active this frame...
    if button_label.status == STARTED:
        # update params
        pass
    # *start_mouse* updates
    
    # if start_mouse is starting this frame...
    if start_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_mouse.frameNStart = frameN  # exact frame index
        start_mouse.tStart = t  # local t and not account for scr refresh
        start_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_mouse, 'tStartRefresh')  # time at next scr refresh
        # update status
        start_mouse.status = STARTED
        start_mouse.mouseClock.reset()
        prevButtonState = start_mouse.getPressed()  # if button is down already this ISN'T a new click
    if start_mouse.status == STARTED:  # only update if started and not finished!
        buttons = start_mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                clickableList = environmenttools.getFromNames(start_button, namespace=locals())
                for obj in clickableList:
                    # is this object clicked on?
                    if obj.contains(start_mouse):
                        gotValidClick = True
                        start_mouse.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # end routine on response
    
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
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "setup_instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "tutorial" ---
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the tutorial_mouse
tutorial_mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
tutorialComponents = [board_outline, begin_button, begin_text, tutorial_mouse, tutorial_title, box_1, text_1, arrow, box_2, text_2, tutorial_piece, left_arrow, up_arrow, up_left_arrow, box_3, text_3, box_4, text_4]
for thisComponent in tutorialComponents:
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

# --- Run Routine "tutorial" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # Run 'Each Frame' code from tutorial_code
    for square in squares:
        square.draw()
    
    # *board_outline* updates
    
    # if board_outline is starting this frame...
    if board_outline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        board_outline.frameNStart = frameN  # exact frame index
        board_outline.tStart = t  # local t and not account for scr refresh
        board_outline.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(board_outline, 'tStartRefresh')  # time at next scr refresh
        # update status
        board_outline.status = STARTED
        board_outline.setAutoDraw(True)
    
    # if board_outline is active this frame...
    if board_outline.status == STARTED:
        # update params
        pass
    
    # *begin_button* updates
    
    # if begin_button is starting this frame...
    if begin_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin_button.frameNStart = frameN  # exact frame index
        begin_button.tStart = t  # local t and not account for scr refresh
        begin_button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_button, 'tStartRefresh')  # time at next scr refresh
        # update status
        begin_button.status = STARTED
        begin_button.setAutoDraw(True)
    
    # if begin_button is active this frame...
    if begin_button.status == STARTED:
        # update params
        pass
    
    # *begin_text* updates
    
    # if begin_text is starting this frame...
    if begin_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin_text.frameNStart = frameN  # exact frame index
        begin_text.tStart = t  # local t and not account for scr refresh
        begin_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_text, 'tStartRefresh')  # time at next scr refresh
        # update status
        begin_text.status = STARTED
        begin_text.setAutoDraw(True)
    
    # if begin_text is active this frame...
    if begin_text.status == STARTED:
        # update params
        pass
    # *tutorial_mouse* updates
    
    # if tutorial_mouse is starting this frame...
    if tutorial_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tutorial_mouse.frameNStart = frameN  # exact frame index
        tutorial_mouse.tStart = t  # local t and not account for scr refresh
        tutorial_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tutorial_mouse, 'tStartRefresh')  # time at next scr refresh
        # update status
        tutorial_mouse.status = STARTED
        tutorial_mouse.mouseClock.reset()
        prevButtonState = tutorial_mouse.getPressed()  # if button is down already this ISN'T a new click
    if tutorial_mouse.status == STARTED:  # only update if started and not finished!
        buttons = tutorial_mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                clickableList = environmenttools.getFromNames(begin_button, namespace=locals())
                for obj in clickableList:
                    # is this object clicked on?
                    if obj.contains(tutorial_mouse):
                        gotValidClick = True
                        tutorial_mouse.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # end routine on response
    
    # *tutorial_title* updates
    
    # if tutorial_title is starting this frame...
    if tutorial_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tutorial_title.frameNStart = frameN  # exact frame index
        tutorial_title.tStart = t  # local t and not account for scr refresh
        tutorial_title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tutorial_title, 'tStartRefresh')  # time at next scr refresh
        # update status
        tutorial_title.status = STARTED
        tutorial_title.setAutoDraw(True)
    
    # if tutorial_title is active this frame...
    if tutorial_title.status == STARTED:
        # update params
        pass
    
    # *box_1* updates
    
    # if box_1 is starting this frame...
    if box_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        box_1.frameNStart = frameN  # exact frame index
        box_1.tStart = t  # local t and not account for scr refresh
        box_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(box_1, 'tStartRefresh')  # time at next scr refresh
        # update status
        box_1.status = STARTED
        box_1.setAutoDraw(True)
    
    # if box_1 is active this frame...
    if box_1.status == STARTED:
        # update params
        pass
    
    # *text_1* updates
    
    # if text_1 is starting this frame...
    if text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_1.frameNStart = frameN  # exact frame index
        text_1.tStart = t  # local t and not account for scr refresh
        text_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
        # update status
        text_1.status = STARTED
        text_1.setAutoDraw(True)
    
    # if text_1 is active this frame...
    if text_1.status == STARTED:
        # update params
        pass
    
    # *arrow* updates
    
    # if arrow is starting this frame...
    if arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        arrow.frameNStart = frameN  # exact frame index
        arrow.tStart = t  # local t and not account for scr refresh
        arrow.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arrow, 'tStartRefresh')  # time at next scr refresh
        # update status
        arrow.status = STARTED
        arrow.setAutoDraw(True)
    
    # if arrow is active this frame...
    if arrow.status == STARTED:
        # update params
        pass
    
    # *box_2* updates
    
    # if box_2 is starting this frame...
    if box_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        box_2.frameNStart = frameN  # exact frame index
        box_2.tStart = t  # local t and not account for scr refresh
        box_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(box_2, 'tStartRefresh')  # time at next scr refresh
        # update status
        box_2.status = STARTED
        box_2.setAutoDraw(True)
    
    # if box_2 is active this frame...
    if box_2.status == STARTED:
        # update params
        pass
    
    # *text_2* updates
    
    # if text_2 is starting this frame...
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # update status
        text_2.status = STARTED
        text_2.setAutoDraw(True)
    
    # if text_2 is active this frame...
    if text_2.status == STARTED:
        # update params
        pass
    
    # *tutorial_piece* updates
    
    # if tutorial_piece is starting this frame...
    if tutorial_piece.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tutorial_piece.frameNStart = frameN  # exact frame index
        tutorial_piece.tStart = t  # local t and not account for scr refresh
        tutorial_piece.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tutorial_piece, 'tStartRefresh')  # time at next scr refresh
        # update status
        tutorial_piece.status = STARTED
        tutorial_piece.setAutoDraw(True)
    
    # if tutorial_piece is active this frame...
    if tutorial_piece.status == STARTED:
        # update params
        pass
    
    # *left_arrow* updates
    
    # if left_arrow is starting this frame...
    if left_arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        left_arrow.frameNStart = frameN  # exact frame index
        left_arrow.tStart = t  # local t and not account for scr refresh
        left_arrow.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(left_arrow, 'tStartRefresh')  # time at next scr refresh
        # update status
        left_arrow.status = STARTED
        left_arrow.setAutoDraw(True)
    
    # if left_arrow is active this frame...
    if left_arrow.status == STARTED:
        # update params
        pass
    
    # *up_arrow* updates
    
    # if up_arrow is starting this frame...
    if up_arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        up_arrow.frameNStart = frameN  # exact frame index
        up_arrow.tStart = t  # local t and not account for scr refresh
        up_arrow.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(up_arrow, 'tStartRefresh')  # time at next scr refresh
        # update status
        up_arrow.status = STARTED
        up_arrow.setAutoDraw(True)
    
    # if up_arrow is active this frame...
    if up_arrow.status == STARTED:
        # update params
        pass
    
    # *up_left_arrow* updates
    
    # if up_left_arrow is starting this frame...
    if up_left_arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        up_left_arrow.frameNStart = frameN  # exact frame index
        up_left_arrow.tStart = t  # local t and not account for scr refresh
        up_left_arrow.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(up_left_arrow, 'tStartRefresh')  # time at next scr refresh
        # update status
        up_left_arrow.status = STARTED
        up_left_arrow.setAutoDraw(True)
    
    # if up_left_arrow is active this frame...
    if up_left_arrow.status == STARTED:
        # update params
        pass
    
    # *box_3* updates
    
    # if box_3 is starting this frame...
    if box_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        box_3.frameNStart = frameN  # exact frame index
        box_3.tStart = t  # local t and not account for scr refresh
        box_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(box_3, 'tStartRefresh')  # time at next scr refresh
        # update status
        box_3.status = STARTED
        box_3.setAutoDraw(True)
    
    # if box_3 is active this frame...
    if box_3.status == STARTED:
        # update params
        pass
    
    # *text_3* updates
    
    # if text_3 is starting this frame...
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        # update status
        text_3.status = STARTED
        text_3.setAutoDraw(True)
    
    # if text_3 is active this frame...
    if text_3.status == STARTED:
        # update params
        pass
    
    # *box_4* updates
    
    # if box_4 is starting this frame...
    if box_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        box_4.frameNStart = frameN  # exact frame index
        box_4.tStart = t  # local t and not account for scr refresh
        box_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(box_4, 'tStartRefresh')  # time at next scr refresh
        # update status
        box_4.status = STARTED
        box_4.setAutoDraw(True)
    
    # if box_4 is active this frame...
    if box_4.status == STARTED:
        # update params
        pass
    
    # *text_4* updates
    
    # if text_4 is starting this frame...
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        # update status
        text_4.status = STARTED
        text_4.setAutoDraw(True)
    
    # if text_4 is active this frame...
    if text_4.status == STARTED:
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
    for thisComponent in tutorialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "tutorial" ---
for thisComponent in tutorialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "tutorial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "practice_info" ---
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_0
mouse_0.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
practice_infoComponents = [title_0, button_0, button_0_text, mouse_0, section_0_text]
for thisComponent in practice_infoComponents:
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

# --- Run Routine "practice_info" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *title_0* updates
    
    # if title_0 is starting this frame...
    if title_0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        title_0.frameNStart = frameN  # exact frame index
        title_0.tStart = t  # local t and not account for scr refresh
        title_0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(title_0, 'tStartRefresh')  # time at next scr refresh
        # update status
        title_0.status = STARTED
        title_0.setAutoDraw(True)
    
    # if title_0 is active this frame...
    if title_0.status == STARTED:
        # update params
        pass
    
    # *button_0* updates
    
    # if button_0 is starting this frame...
    if button_0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_0.frameNStart = frameN  # exact frame index
        button_0.tStart = t  # local t and not account for scr refresh
        button_0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_0, 'tStartRefresh')  # time at next scr refresh
        # update status
        button_0.status = STARTED
        button_0.setAutoDraw(True)
    
    # if button_0 is active this frame...
    if button_0.status == STARTED:
        # update params
        pass
    
    # *button_0_text* updates
    
    # if button_0_text is starting this frame...
    if button_0_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_0_text.frameNStart = frameN  # exact frame index
        button_0_text.tStart = t  # local t and not account for scr refresh
        button_0_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_0_text, 'tStartRefresh')  # time at next scr refresh
        # update status
        button_0_text.status = STARTED
        button_0_text.setAutoDraw(True)
    
    # if button_0_text is active this frame...
    if button_0_text.status == STARTED:
        # update params
        pass
    # *mouse_0* updates
    
    # if mouse_0 is starting this frame...
    if mouse_0.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_0.frameNStart = frameN  # exact frame index
        mouse_0.tStart = t  # local t and not account for scr refresh
        mouse_0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_0, 'tStartRefresh')  # time at next scr refresh
        # update status
        mouse_0.status = STARTED
        mouse_0.mouseClock.reset()
        prevButtonState = mouse_0.getPressed()  # if button is down already this ISN'T a new click
    if mouse_0.status == STARTED:  # only update if started and not finished!
        buttons = mouse_0.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                clickableList = environmenttools.getFromNames(button_0, namespace=locals())
                for obj in clickableList:
                    # is this object clicked on?
                    if obj.contains(mouse_0):
                        gotValidClick = True
                        mouse_0.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # end routine on response
    
    # *section_0_text* updates
    
    # if section_0_text is starting this frame...
    if section_0_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        section_0_text.frameNStart = frameN  # exact frame index
        section_0_text.tStart = t  # local t and not account for scr refresh
        section_0_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(section_0_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'section_0_text.started')
        # update status
        section_0_text.status = STARTED
        section_0_text.setAutoDraw(True)
    
    # if section_0_text is active this frame...
    if section_0_text.status == STARTED:
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
    for thisComponent in practice_infoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "practice_info" ---
for thisComponent in practice_infoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "practice_info" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_games = data.TrialHandler(nReps=num_games, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practice_games')
thisExp.addLoop(practice_games)  # add the loop to the experiment
thisPractice_game = practice_games.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_game.rgb)
if thisPractice_game != None:
    for paramName in thisPractice_game:
        exec('{} = thisPractice_game[paramName]'.format(paramName))

for thisPractice_game in practice_games:
    currentLoop = practice_games
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_game.rgb)
    if thisPractice_game != None:
        for paramName in thisPractice_game:
            exec('{} = thisPractice_game[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "countdown" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from countdown_code
    event.Mouse(visible=False)
    
    import random
    import math
    
    if section == 1 or section == 3 or section == 4:
        practice_turns.finished = False
    
    player_won = None
    npc_start = npc_starts[game]
    game = game + 1
    
    move_num = 0 # initialize move counter
    
    row = random.randint(0,14)
    col = random.randint(0,14)
    
    while row == col == 0:
        row = random.randint(0,14)
        col = random.randint(0,14)
    
    row_new = row
    col_new = col
    blue_piece.setOpacity(1 - npc_start)
    blue_piece.setPos(((col-7)/17, (15-row-8)/17))
    red_piece.setOpacity(npc_start)
    red_piece.setPos(((col-7)/17, (15-row-8)/17))
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
    practice_turns = data.TrialHandler(nReps=15.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='practice_turns')
    thisExp.addLoop(practice_turns)  # add the loop to the experiment
    thisPractice_turn = practice_turns.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_turn.rgb)
    if thisPractice_turn != None:
        for paramName in thisPractice_turn:
            exec('{} = thisPractice_turn[paramName]'.format(paramName))
    
    for thisPractice_turn in practice_turns:
        currentLoop = practice_turns
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_turn.rgb)
        if thisPractice_turn != None:
            for paramName in thisPractice_turn:
                exec('{} = thisPractice_turn[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "select_move" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        mouse.setPos(newPos=(0,0))
        event.Mouse(visible=True)
        
        if npc_start:
            continueRoutine = False
        
        timer = core.Clock()
        timer.reset()
        RT = 0
        
        row = row_new
        col = col_new
        
        mouse_still = True
        mouse_start = mouse.getPos()
        piece.setPos(((col-7)/17, (15-row-8)/17))
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
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
            # record mouse move onset time (RT)
            if mouse_still and any(mouse.getPos() != mouse_start):
                RT = timer.getTime()
                mouse_moved = True
            
            # on click, check for valid move selection
            if mouse.getPressed()[0] == 1:
                mouse_x, mouse_y = mouse.getPos()
                row_new = round(0 - ((mouse_y * 17) + 8 - 15))
                col_new = round((mouse_x * 17) + 7)
                if row_new <= row and col_new <= col:
                    if row_new >= 0 and col_new >= 0:
                        if row_new==row or col_new==col or (section != 4 and row-row_new == col-col_new):
                            if row_new != row or col_new != col:
                                if section != 4 or int(expInfo['session']) % 2 == 1 or euclid_move(move):
                                    continueRoutine = False
            
            # draw game board
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
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
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
        # Run 'End Routine' code from code
        if npc_start == False:
            move_num = move_num + 1
            df = df.append(pd.Series(dtype = 'object'), ignore_index = True)
            df.loc[len(df) - 1, 'session'] = expInfo['session']
            df.loc[len(df) - 1, 'section'] = section
            if section == 4 and int(expInfo['session']) % 2 == 0:
                df.loc[len(df) - 1, 'type'] = 'euc'
            if section == 4 and int(expInfo['session']) % 2 == 1:
                df.loc[len(df) - 1, 'type'] = 'nim'
            df.loc[len(df) - 1, 'game'] = game
            df.loc[len(df) - 1, 'move_num'] = move_num
            df.loc[len(df) - 1, 'player'] = 'human'
            df.loc[len(df) - 1, 'start_row'] = row
            df.loc[len(df) - 1, 'start_col'] = col
            df.loc[len(df) - 1, 'end_row'] = row_new
            df.loc[len(df) - 1, 'end_col'] = col_new
            df.loc[len(df) - 1, 'RT'] = RT
            df.loc[len(df) - 1, 'DT'] = timer.getTime()
            #print(df.to_string())
        # store data for practice_turns (TrialHandler)
        practice_turns.addData('mouse.x', mouse.x)
        practice_turns.addData('mouse.y', mouse.y)
        practice_turns.addData('mouse.leftButton', mouse.leftButton)
        practice_turns.addData('mouse.midButton', mouse.midButton)
        practice_turns.addData('mouse.rightButton', mouse.rightButton)
        practice_turns.addData('mouse.time', mouse.time)
        # the Routine "select_move" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "make_move" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from move_code
        event.Mouse(visible=False)
        
        #timer = core.Clock()
        #timer.reset()
        
        if npc_start or visibility == 0:
            npc_start = False
            continueRoutine = False
        moving_piece.setOpacity(visibility)
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
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from move_code
            for square in squares:
                square.draw()
            
            #if timer.getTime() > move_duration:
            #    continueRoutine = False
            
            # *moving_piece* updates
            
            # if moving_piece is starting this frame...
            if moving_piece.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                moving_piece.frameNStart = frameN  # exact frame index
                moving_piece.tStart = t  # local t and not account for scr refresh
                moving_piece.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(moving_piece, 'tStartRefresh')  # time at next scr refresh
                # update status
                moving_piece.status = STARTED
                moving_piece.setAutoDraw(True)
            
            # if moving_piece is active this frame...
            if moving_piece.status == STARTED:
                # update params
                moving_piece.setPos(((((1-min(move_duration,t)/move_duration)*col+min(move_duration,t)/move_duration*col_new)-7)/17, (15-((1-min(move_duration,t)/move_duration)*row+min(move_duration,t)/move_duration*row_new)-8)/17), log=False)
            
            # if moving_piece is stopping this frame...
            if moving_piece.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > moving_piece.tStartRefresh + move_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    moving_piece.tStop = t  # not accounting for scr refresh
                    moving_piece.frameNStop = frameN  # exact frame index
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
            if player_won == None:
                player_won = True
            num_wins = num_wins + 1
            practice_turns.finished = True
            if section == 1:
                turns.finished = True
            if section == 3:
                more_turns.finished = True
            if section == 4:
                turns_4.finished = True
            continueRoutine = False
        # the Routine "make_move" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "npc_wait" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from wait_code
        event.Mouse(visible=False)
        
        if practice_turns.finished:
            continueRoutine = False
        
        row = row_new
        col = col_new
        
        # select random opponent move
        moves = []
        Q_table = []
        
        if section != 4:
            optimal_moves = optimal_moves_wythoffs
        else:
            if int(expInfo['session']) % 2 == 0:
                optimal_moves = optimal_moves_euclid
            else:
                optimal_moves = optimal_moves_nim
        
        for r in range (row): # vertical moves
            move = (r, col)
            if section != 4 or int(expInfo['session']) % 2 == 1 or euclid_move(move):
                moves.append(move)
                if move in optimal_moves:
                    Q_table.append(1)
                else:
                    Q_table.append(0)
            
        for c in range (col): # horiz moves
            move = (row, c)
            if section != 4 or int(expInfo['session']) % 2 == 1 or euclid_move(move):
                moves.append(move)
                if move in optimal_moves:
                    Q_table.append(1)
                else:
                    Q_table.append(0)
            
        for d in range(1, min(row, col) + 1): # diag moves
            move = (row - d, col - d)
            if section != 4:
                moves.append(move)
                if move in optimal_moves:
                    Q_table.append(1)
                else:
                    Q_table.append(0)
        
        # action selection
        if len(moves) > 0:
            # calculate Boltzmann (softmax) action probs
            T = 0.55 # temperature parameter
            probs = np.exp(np.true_divide(Q_table,T))
            probs = np.true_divide(probs, sum(probs))
            action = np.random.choice(len(moves),p=probs)
            (row_new, col_new) = moves[action]
            # better to use np.random.Generator.choice
        npc.setPos(((col-7)/17, (15-row-8)/17))
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
        # Run 'End Routine' code from wait_code
        if practice_turns.finished == False:
            move_num = move_num + 1
            df = df.append(pd.Series(dtype = 'object'), ignore_index = True)
            df.loc[len(df) - 1, 'session'] = expInfo['session']
            df.loc[len(df) - 1, 'section'] = section
            df.loc[len(df) - 1, 'game'] = game
            df.loc[len(df) - 1, 'move_num'] = move_num
            df.loc[len(df) - 1, 'player'] = 'AI'
            df.loc[len(df) - 1, 'start_row'] = row
            df.loc[len(df) - 1, 'start_col'] = col
            df.loc[len(df) - 1, 'end_row'] = row_new
            df.loc[len(df) - 1, 'end_col'] = col_new
            df.loc[len(df) - 1, 'DT'] = 1.25
            #print(df.to_string())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.250000)
        
        # --- Prepare to start Routine "npc_move" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from npc_code
        event.Mouse(visible=False)
        
        #timer = core.Clock()
        #timer.reset()
        
        if practice_turns.finished or visibility == 0:
            continueRoutine = False
        moving_npc.setOpacity(visibility)
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
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from npc_code
            for square in squares:
                square.draw()
            
            #if timer.getTime() > move_duration:
            #    continueRoutine = False
            
            # *moving_npc* updates
            
            # if moving_npc is starting this frame...
            if moving_npc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                moving_npc.frameNStart = frameN  # exact frame index
                moving_npc.tStart = t  # local t and not account for scr refresh
                moving_npc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(moving_npc, 'tStartRefresh')  # time at next scr refresh
                # update status
                moving_npc.status = STARTED
                moving_npc.setAutoDraw(True)
            
            # if moving_npc is active this frame...
            if moving_npc.status == STARTED:
                # update params
                moving_npc.setPos(((((1-min(move_duration,t)/move_duration)*col+min(move_duration,t)/move_duration*col_new)-7)/17, (15-((1-min(move_duration,t)/move_duration)*row+min(move_duration,t)/move_duration*row_new)-8)/17), log=False)
            
            # if moving_npc is stopping this frame...
            if moving_npc.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > moving_npc.tStartRefresh + move_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    moving_npc.tStop = t  # not accounting for scr refresh
                    moving_npc.frameNStop = frameN  # exact frame index
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
            practice_turns.finished = True
            if section == 1:
                turns.finished = True
            if section == 3:
                more_turns.finished = True
            if section == 4:
                turns_4.finished = True
        # the Routine "npc_move" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 15.0 repeats of 'practice_turns'
    
    
    # --- Prepare to start Routine "end_pause" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from end_code
    event.Mouse(visible=False)
    
    row = row_new
    col = col_new
    
    if visibility == 0:
        continueRoutine = False
    
    #print(df.to_string())
    end_blue.setOpacity(player_won)
    end_blue.setPos(((col-7)/17, (15-row-8)/17))
    end_red.setOpacity(1 - player_won)
    end_red.setPos(((col-7)/17, (15-row-8)/17))
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
    while continueRoutine:
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
            if tThisFlipGlobal > end_blue.tStartRefresh + end_pause_duration-frameTolerance:
                # keep track of stop time/frame for later
                end_blue.tStop = t  # not accounting for scr refresh
                end_blue.frameNStop = frameN  # exact frame index
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
            if tThisFlipGlobal > end_red.tStartRefresh + end_pause_duration-frameTolerance:
                # keep track of stop time/frame for later
                end_red.tStop = t  # not accounting for scr refresh
                end_red.frameNStop = frameN  # exact frame index
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
    # the Routine "end_pause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code
    event.Mouse(visible=True)
    
    if player_won:
        df.loc[(df.game==game) & (df.section==section), 'winner'] = 'human'
    else:
        df.loc[(df.game==game) & (df.section==section), 'winner'] = 'AI'
    feedback_win.setOpacity(player_won)
    feedback_lose.setOpacity(1 - player_won)
    status_text.setText('games played: ' + str(game) + ' of ' + str(num_games) + '\nwin percentage: ' + str(round (num_wins / game * 100)) + '%')
    # setup some python lists for storing info about the next_mouse
    next_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    feedbackComponents = [feedback_win, feedback_lose, status_text, button, button_text, next_mouse]
    for thisComponent in feedbackComponents:
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
    
    # --- Run Routine "feedback" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_win* updates
        
        # if feedback_win is starting this frame...
        if feedback_win.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_win.frameNStart = frameN  # exact frame index
            feedback_win.tStart = t  # local t and not account for scr refresh
            feedback_win.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_win, 'tStartRefresh')  # time at next scr refresh
            # update status
            feedback_win.status = STARTED
            feedback_win.setAutoDraw(True)
        
        # if feedback_win is active this frame...
        if feedback_win.status == STARTED:
            # update params
            pass
        
        # *feedback_lose* updates
        
        # if feedback_lose is starting this frame...
        if feedback_lose.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_lose.frameNStart = frameN  # exact frame index
            feedback_lose.tStart = t  # local t and not account for scr refresh
            feedback_lose.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_lose, 'tStartRefresh')  # time at next scr refresh
            # update status
            feedback_lose.status = STARTED
            feedback_lose.setAutoDraw(True)
        
        # if feedback_lose is active this frame...
        if feedback_lose.status == STARTED:
            # update params
            pass
        
        # *status_text* updates
        
        # if status_text is starting this frame...
        if status_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            status_text.frameNStart = frameN  # exact frame index
            status_text.tStart = t  # local t and not account for scr refresh
            status_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(status_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'status_text.started')
            # update status
            status_text.status = STARTED
            status_text.setAutoDraw(True)
        
        # if status_text is active this frame...
        if status_text.status == STARTED:
            # update params
            pass
        
        # *button* updates
        
        # if button is starting this frame...
        if button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button.frameNStart = frameN  # exact frame index
            button.tStart = t  # local t and not account for scr refresh
            button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
            # update status
            button.status = STARTED
            button.setAutoDraw(True)
        
        # if button is active this frame...
        if button.status == STARTED:
            # update params
            pass
        
        # *button_text* updates
        
        # if button_text is starting this frame...
        if button_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_text.frameNStart = frameN  # exact frame index
            button_text.tStart = t  # local t and not account for scr refresh
            button_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            button_text.status = STARTED
            button_text.setAutoDraw(True)
        
        # if button_text is active this frame...
        if button_text.status == STARTED:
            # update params
            pass
        # *next_mouse* updates
        
        # if next_mouse is starting this frame...
        if next_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next_mouse.frameNStart = frameN  # exact frame index
            next_mouse.tStart = t  # local t and not account for scr refresh
            next_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_mouse, 'tStartRefresh')  # time at next scr refresh
            # update status
            next_mouse.status = STARTED
            next_mouse.mouseClock.reset()
            prevButtonState = next_mouse.getPressed()  # if button is down already this ISN'T a new click
        if next_mouse.status == STARTED:  # only update if started and not finished!
            buttons = next_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(button, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(next_mouse):
                            gotValidClick = True
                            next_mouse.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
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
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for practice_games (TrialHandler)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed num_games repeats of 'practice_games'


# set up handler to look after randomisation of conditions etc
double_click_1 = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='double_click_1')
thisExp.addLoop(double_click_1)  # add the loop to the experiment
thisDouble_click_1 = double_click_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDouble_click_1.rgb)
if thisDouble_click_1 != None:
    for paramName in thisDouble_click_1:
        exec('{} = thisDouble_click_1[paramName]'.format(paramName))

for thisDouble_click_1 in double_click_1:
    currentLoop = double_click_1
    # abbreviate parameter names if possible (e.g. rgb = thisDouble_click_1.rgb)
    if thisDouble_click_1 != None:
        for paramName in thisDouble_click_1:
            exec('{} = thisDouble_click_1[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "section_1" ---
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_1
    mouse_1.clicked_name = []
    gotValidClick = False  # until a click is received
    section_1_text.setText('Click the button below when you are ready to start playing.')
    # Run 'Begin Routine' code from section_1_code
    num_games = 2 # must be even
    assert(num_games % 2 == 0)
    
    # generate shuffled list of who starts each game
    npc_starts = []
    for game in range(int(num_games/2)):
        npc_starts.append(True)
        npc_starts.append(False)
    random.shuffle(npc_starts)
    
    game = 0 # initialize game counter
    num_wins = 0 # initialize win counter
    visibility = 1 # pieces are visible for Section 1
    section = 1 # variable for experiment section
    
    practice_turns.finished = False
    # keep track of which components have finished
    section_1Components = [title_1, button_1, button_1_text, mouse_1, section_1_text]
    for thisComponent in section_1Components:
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
    
    # --- Run Routine "section_1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *title_1* updates
        
        # if title_1 is starting this frame...
        if title_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            title_1.frameNStart = frameN  # exact frame index
            title_1.tStart = t  # local t and not account for scr refresh
            title_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(title_1, 'tStartRefresh')  # time at next scr refresh
            # update status
            title_1.status = STARTED
            title_1.setAutoDraw(True)
        
        # if title_1 is active this frame...
        if title_1.status == STARTED:
            # update params
            pass
        
        # *button_1* updates
        
        # if button_1 is starting this frame...
        if button_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_1.frameNStart = frameN  # exact frame index
            button_1.tStart = t  # local t and not account for scr refresh
            button_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_1, 'tStartRefresh')  # time at next scr refresh
            # update status
            button_1.status = STARTED
            button_1.setAutoDraw(True)
        
        # if button_1 is active this frame...
        if button_1.status == STARTED:
            # update params
            pass
        
        # *button_1_text* updates
        
        # if button_1_text is starting this frame...
        if button_1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_1_text.frameNStart = frameN  # exact frame index
            button_1_text.tStart = t  # local t and not account for scr refresh
            button_1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_1_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            button_1_text.status = STARTED
            button_1_text.setAutoDraw(True)
        
        # if button_1_text is active this frame...
        if button_1_text.status == STARTED:
            # update params
            pass
        # *mouse_1* updates
        
        # if mouse_1 is starting this frame...
        if mouse_1.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_1.frameNStart = frameN  # exact frame index
            mouse_1.tStart = t  # local t and not account for scr refresh
            mouse_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_1, 'tStartRefresh')  # time at next scr refresh
            # update status
            mouse_1.status = STARTED
            mouse_1.mouseClock.reset()
            prevButtonState = mouse_1.getPressed()  # if button is down already this ISN'T a new click
        if mouse_1.status == STARTED:  # only update if started and not finished!
            buttons = mouse_1.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(button_1, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_1):
                            gotValidClick = True
                            mouse_1.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
        # *section_1_text* updates
        
        # if section_1_text is starting this frame...
        if section_1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            section_1_text.frameNStart = frameN  # exact frame index
            section_1_text.tStart = t  # local t and not account for scr refresh
            section_1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(section_1_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'section_1_text.started')
            # update status
            section_1_text.status = STARTED
            section_1_text.setAutoDraw(True)
        
        # if section_1_text is active this frame...
        if section_1_text.status == STARTED:
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
        for thisComponent in section_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "section_1" ---
    for thisComponent in section_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for double_click_1 (TrialHandler)
    # the Routine "section_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 2.0 repeats of 'double_click_1'


# set up handler to look after randomisation of conditions etc
games = data.TrialHandler(nReps=num_games, method='random', 
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
    event.Mouse(visible=False)
    
    import random
    import math
    
    if section == 1 or section == 3 or section == 4:
        practice_turns.finished = False
    
    player_won = None
    npc_start = npc_starts[game]
    game = game + 1
    
    move_num = 0 # initialize move counter
    
    row = random.randint(0,14)
    col = random.randint(0,14)
    
    while row == col == 0:
        row = random.randint(0,14)
        col = random.randint(0,14)
    
    row_new = row
    col_new = col
    blue_piece.setOpacity(1 - npc_start)
    blue_piece.setPos(((col-7)/17, (15-row-8)/17))
    red_piece.setOpacity(npc_start)
    red_piece.setPos(((col-7)/17, (15-row-8)/17))
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
    turns = data.TrialHandler(nReps=15.0, method='random', 
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
        mouse.setPos(newPos=(0,0))
        event.Mouse(visible=True)
        
        if npc_start:
            continueRoutine = False
        
        timer = core.Clock()
        timer.reset()
        RT = 0
        
        row = row_new
        col = col_new
        
        mouse_still = True
        mouse_start = mouse.getPos()
        piece.setPos(((col-7)/17, (15-row-8)/17))
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
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
            # record mouse move onset time (RT)
            if mouse_still and any(mouse.getPos() != mouse_start):
                RT = timer.getTime()
                mouse_moved = True
            
            # on click, check for valid move selection
            if mouse.getPressed()[0] == 1:
                mouse_x, mouse_y = mouse.getPos()
                row_new = round(0 - ((mouse_y * 17) + 8 - 15))
                col_new = round((mouse_x * 17) + 7)
                if row_new <= row and col_new <= col:
                    if row_new >= 0 and col_new >= 0:
                        if row_new==row or col_new==col or (section != 4 and row-row_new == col-col_new):
                            if row_new != row or col_new != col:
                                if section != 4 or int(expInfo['session']) % 2 == 1 or euclid_move(move):
                                    continueRoutine = False
            
            # draw game board
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
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
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
        # Run 'End Routine' code from code
        if npc_start == False:
            move_num = move_num + 1
            df = df.append(pd.Series(dtype = 'object'), ignore_index = True)
            df.loc[len(df) - 1, 'session'] = expInfo['session']
            df.loc[len(df) - 1, 'section'] = section
            if section == 4 and int(expInfo['session']) % 2 == 0:
                df.loc[len(df) - 1, 'type'] = 'euc'
            if section == 4 and int(expInfo['session']) % 2 == 1:
                df.loc[len(df) - 1, 'type'] = 'nim'
            df.loc[len(df) - 1, 'game'] = game
            df.loc[len(df) - 1, 'move_num'] = move_num
            df.loc[len(df) - 1, 'player'] = 'human'
            df.loc[len(df) - 1, 'start_row'] = row
            df.loc[len(df) - 1, 'start_col'] = col
            df.loc[len(df) - 1, 'end_row'] = row_new
            df.loc[len(df) - 1, 'end_col'] = col_new
            df.loc[len(df) - 1, 'RT'] = RT
            df.loc[len(df) - 1, 'DT'] = timer.getTime()
            #print(df.to_string())
        # store data for turns (TrialHandler)
        turns.addData('mouse.x', mouse.x)
        turns.addData('mouse.y', mouse.y)
        turns.addData('mouse.leftButton', mouse.leftButton)
        turns.addData('mouse.midButton', mouse.midButton)
        turns.addData('mouse.rightButton', mouse.rightButton)
        turns.addData('mouse.time', mouse.time)
        # the Routine "select_move" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "make_move" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from move_code
        event.Mouse(visible=False)
        
        #timer = core.Clock()
        #timer.reset()
        
        if npc_start or visibility == 0:
            npc_start = False
            continueRoutine = False
        moving_piece.setOpacity(visibility)
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
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from move_code
            for square in squares:
                square.draw()
            
            #if timer.getTime() > move_duration:
            #    continueRoutine = False
            
            # *moving_piece* updates
            
            # if moving_piece is starting this frame...
            if moving_piece.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                moving_piece.frameNStart = frameN  # exact frame index
                moving_piece.tStart = t  # local t and not account for scr refresh
                moving_piece.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(moving_piece, 'tStartRefresh')  # time at next scr refresh
                # update status
                moving_piece.status = STARTED
                moving_piece.setAutoDraw(True)
            
            # if moving_piece is active this frame...
            if moving_piece.status == STARTED:
                # update params
                moving_piece.setPos(((((1-min(move_duration,t)/move_duration)*col+min(move_duration,t)/move_duration*col_new)-7)/17, (15-((1-min(move_duration,t)/move_duration)*row+min(move_duration,t)/move_duration*row_new)-8)/17), log=False)
            
            # if moving_piece is stopping this frame...
            if moving_piece.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > moving_piece.tStartRefresh + move_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    moving_piece.tStop = t  # not accounting for scr refresh
                    moving_piece.frameNStop = frameN  # exact frame index
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
            if player_won == None:
                player_won = True
            num_wins = num_wins + 1
            practice_turns.finished = True
            if section == 1:
                turns.finished = True
            if section == 3:
                more_turns.finished = True
            if section == 4:
                turns_4.finished = True
            continueRoutine = False
        # the Routine "make_move" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "npc_wait" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from wait_code
        event.Mouse(visible=False)
        
        if practice_turns.finished:
            continueRoutine = False
        
        row = row_new
        col = col_new
        
        # select random opponent move
        moves = []
        Q_table = []
        
        if section != 4:
            optimal_moves = optimal_moves_wythoffs
        else:
            if int(expInfo['session']) % 2 == 0:
                optimal_moves = optimal_moves_euclid
            else:
                optimal_moves = optimal_moves_nim
        
        for r in range (row): # vertical moves
            move = (r, col)
            if section != 4 or int(expInfo['session']) % 2 == 1 or euclid_move(move):
                moves.append(move)
                if move in optimal_moves:
                    Q_table.append(1)
                else:
                    Q_table.append(0)
            
        for c in range (col): # horiz moves
            move = (row, c)
            if section != 4 or int(expInfo['session']) % 2 == 1 or euclid_move(move):
                moves.append(move)
                if move in optimal_moves:
                    Q_table.append(1)
                else:
                    Q_table.append(0)
            
        for d in range(1, min(row, col) + 1): # diag moves
            move = (row - d, col - d)
            if section != 4:
                moves.append(move)
                if move in optimal_moves:
                    Q_table.append(1)
                else:
                    Q_table.append(0)
        
        # action selection
        if len(moves) > 0:
            # calculate Boltzmann (softmax) action probs
            T = 0.55 # temperature parameter
            probs = np.exp(np.true_divide(Q_table,T))
            probs = np.true_divide(probs, sum(probs))
            action = np.random.choice(len(moves),p=probs)
            (row_new, col_new) = moves[action]
            # better to use np.random.Generator.choice
        npc.setPos(((col-7)/17, (15-row-8)/17))
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
        # Run 'End Routine' code from wait_code
        if practice_turns.finished == False:
            move_num = move_num + 1
            df = df.append(pd.Series(dtype = 'object'), ignore_index = True)
            df.loc[len(df) - 1, 'session'] = expInfo['session']
            df.loc[len(df) - 1, 'section'] = section
            df.loc[len(df) - 1, 'game'] = game
            df.loc[len(df) - 1, 'move_num'] = move_num
            df.loc[len(df) - 1, 'player'] = 'AI'
            df.loc[len(df) - 1, 'start_row'] = row
            df.loc[len(df) - 1, 'start_col'] = col
            df.loc[len(df) - 1, 'end_row'] = row_new
            df.loc[len(df) - 1, 'end_col'] = col_new
            df.loc[len(df) - 1, 'DT'] = 1.25
            #print(df.to_string())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.250000)
        
        # --- Prepare to start Routine "npc_move" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from npc_code
        event.Mouse(visible=False)
        
        #timer = core.Clock()
        #timer.reset()
        
        if practice_turns.finished or visibility == 0:
            continueRoutine = False
        moving_npc.setOpacity(visibility)
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
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from npc_code
            for square in squares:
                square.draw()
            
            #if timer.getTime() > move_duration:
            #    continueRoutine = False
            
            # *moving_npc* updates
            
            # if moving_npc is starting this frame...
            if moving_npc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                moving_npc.frameNStart = frameN  # exact frame index
                moving_npc.tStart = t  # local t and not account for scr refresh
                moving_npc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(moving_npc, 'tStartRefresh')  # time at next scr refresh
                # update status
                moving_npc.status = STARTED
                moving_npc.setAutoDraw(True)
            
            # if moving_npc is active this frame...
            if moving_npc.status == STARTED:
                # update params
                moving_npc.setPos(((((1-min(move_duration,t)/move_duration)*col+min(move_duration,t)/move_duration*col_new)-7)/17, (15-((1-min(move_duration,t)/move_duration)*row+min(move_duration,t)/move_duration*row_new)-8)/17), log=False)
            
            # if moving_npc is stopping this frame...
            if moving_npc.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > moving_npc.tStartRefresh + move_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    moving_npc.tStop = t  # not accounting for scr refresh
                    moving_npc.frameNStop = frameN  # exact frame index
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
            practice_turns.finished = True
            if section == 1:
                turns.finished = True
            if section == 3:
                more_turns.finished = True
            if section == 4:
                turns_4.finished = True
        # the Routine "npc_move" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 15.0 repeats of 'turns'
    
    
    # --- Prepare to start Routine "end_pause" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from end_code
    event.Mouse(visible=False)
    
    row = row_new
    col = col_new
    
    if visibility == 0:
        continueRoutine = False
    
    #print(df.to_string())
    end_blue.setOpacity(player_won)
    end_blue.setPos(((col-7)/17, (15-row-8)/17))
    end_red.setOpacity(1 - player_won)
    end_red.setPos(((col-7)/17, (15-row-8)/17))
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
    while continueRoutine:
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
            if tThisFlipGlobal > end_blue.tStartRefresh + end_pause_duration-frameTolerance:
                # keep track of stop time/frame for later
                end_blue.tStop = t  # not accounting for scr refresh
                end_blue.frameNStop = frameN  # exact frame index
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
            if tThisFlipGlobal > end_red.tStartRefresh + end_pause_duration-frameTolerance:
                # keep track of stop time/frame for later
                end_red.tStop = t  # not accounting for scr refresh
                end_red.frameNStop = frameN  # exact frame index
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
    # the Routine "end_pause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code
    event.Mouse(visible=True)
    
    if player_won:
        df.loc[(df.game==game) & (df.section==section), 'winner'] = 'human'
    else:
        df.loc[(df.game==game) & (df.section==section), 'winner'] = 'AI'
    feedback_win.setOpacity(player_won)
    feedback_lose.setOpacity(1 - player_won)
    status_text.setText('games played: ' + str(game) + ' of ' + str(num_games) + '\nwin percentage: ' + str(round (num_wins / game * 100)) + '%')
    # setup some python lists for storing info about the next_mouse
    next_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    feedbackComponents = [feedback_win, feedback_lose, status_text, button, button_text, next_mouse]
    for thisComponent in feedbackComponents:
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
    
    # --- Run Routine "feedback" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_win* updates
        
        # if feedback_win is starting this frame...
        if feedback_win.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_win.frameNStart = frameN  # exact frame index
            feedback_win.tStart = t  # local t and not account for scr refresh
            feedback_win.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_win, 'tStartRefresh')  # time at next scr refresh
            # update status
            feedback_win.status = STARTED
            feedback_win.setAutoDraw(True)
        
        # if feedback_win is active this frame...
        if feedback_win.status == STARTED:
            # update params
            pass
        
        # *feedback_lose* updates
        
        # if feedback_lose is starting this frame...
        if feedback_lose.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_lose.frameNStart = frameN  # exact frame index
            feedback_lose.tStart = t  # local t and not account for scr refresh
            feedback_lose.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_lose, 'tStartRefresh')  # time at next scr refresh
            # update status
            feedback_lose.status = STARTED
            feedback_lose.setAutoDraw(True)
        
        # if feedback_lose is active this frame...
        if feedback_lose.status == STARTED:
            # update params
            pass
        
        # *status_text* updates
        
        # if status_text is starting this frame...
        if status_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            status_text.frameNStart = frameN  # exact frame index
            status_text.tStart = t  # local t and not account for scr refresh
            status_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(status_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'status_text.started')
            # update status
            status_text.status = STARTED
            status_text.setAutoDraw(True)
        
        # if status_text is active this frame...
        if status_text.status == STARTED:
            # update params
            pass
        
        # *button* updates
        
        # if button is starting this frame...
        if button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button.frameNStart = frameN  # exact frame index
            button.tStart = t  # local t and not account for scr refresh
            button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
            # update status
            button.status = STARTED
            button.setAutoDraw(True)
        
        # if button is active this frame...
        if button.status == STARTED:
            # update params
            pass
        
        # *button_text* updates
        
        # if button_text is starting this frame...
        if button_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_text.frameNStart = frameN  # exact frame index
            button_text.tStart = t  # local t and not account for scr refresh
            button_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            button_text.status = STARTED
            button_text.setAutoDraw(True)
        
        # if button_text is active this frame...
        if button_text.status == STARTED:
            # update params
            pass
        # *next_mouse* updates
        
        # if next_mouse is starting this frame...
        if next_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next_mouse.frameNStart = frameN  # exact frame index
            next_mouse.tStart = t  # local t and not account for scr refresh
            next_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_mouse, 'tStartRefresh')  # time at next scr refresh
            # update status
            next_mouse.status = STARTED
            next_mouse.mouseClock.reset()
            prevButtonState = next_mouse.getPressed()  # if button is down already this ISN'T a new click
        if next_mouse.status == STARTED:  # only update if started and not finished!
            buttons = next_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(button, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(next_mouse):
                            gotValidClick = True
                            next_mouse.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
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
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for games (TrialHandler)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed num_games repeats of 'games'


# --- Prepare to start Routine "instruct_recall" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from recall_code
# skip recall instructions if imagining
if int(expInfo['session']) % 2 == 0:
    continueRoutine = False
# setup some python lists for storing info about the recall_mouse
recall_mouse.clicked_name = []
gotValidClick = False  # until a click is received
recall_text.setText('In this section you will view game replays.\n\nAt the end of each replay, you will be asked who won the game (you vs. the opponent).\n\nPlease pay attention and respond as best you can!')
# keep track of which components have finished
instruct_recallComponents = [recall_title, recall_button, recall_ready, recall_mouse, recall_text]
for thisComponent in instruct_recallComponents:
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

# --- Run Routine "instruct_recall" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *recall_title* updates
    
    # if recall_title is starting this frame...
    if recall_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        recall_title.frameNStart = frameN  # exact frame index
        recall_title.tStart = t  # local t and not account for scr refresh
        recall_title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(recall_title, 'tStartRefresh')  # time at next scr refresh
        # update status
        recall_title.status = STARTED
        recall_title.setAutoDraw(True)
    
    # if recall_title is active this frame...
    if recall_title.status == STARTED:
        # update params
        pass
    
    # *recall_button* updates
    
    # if recall_button is starting this frame...
    if recall_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        recall_button.frameNStart = frameN  # exact frame index
        recall_button.tStart = t  # local t and not account for scr refresh
        recall_button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(recall_button, 'tStartRefresh')  # time at next scr refresh
        # update status
        recall_button.status = STARTED
        recall_button.setAutoDraw(True)
    
    # if recall_button is active this frame...
    if recall_button.status == STARTED:
        # update params
        pass
    
    # *recall_ready* updates
    
    # if recall_ready is starting this frame...
    if recall_ready.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        recall_ready.frameNStart = frameN  # exact frame index
        recall_ready.tStart = t  # local t and not account for scr refresh
        recall_ready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(recall_ready, 'tStartRefresh')  # time at next scr refresh
        # update status
        recall_ready.status = STARTED
        recall_ready.setAutoDraw(True)
    
    # if recall_ready is active this frame...
    if recall_ready.status == STARTED:
        # update params
        pass
    # *recall_mouse* updates
    
    # if recall_mouse is starting this frame...
    if recall_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        recall_mouse.frameNStart = frameN  # exact frame index
        recall_mouse.tStart = t  # local t and not account for scr refresh
        recall_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(recall_mouse, 'tStartRefresh')  # time at next scr refresh
        # update status
        recall_mouse.status = STARTED
        recall_mouse.mouseClock.reset()
        prevButtonState = recall_mouse.getPressed()  # if button is down already this ISN'T a new click
    if recall_mouse.status == STARTED:  # only update if started and not finished!
        buttons = recall_mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                clickableList = environmenttools.getFromNames(recall_button, namespace=locals())
                for obj in clickableList:
                    # is this object clicked on?
                    if obj.contains(recall_mouse):
                        gotValidClick = True
                        recall_mouse.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # end routine on response
    
    # *recall_text* updates
    
    # if recall_text is starting this frame...
    if recall_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        recall_text.frameNStart = frameN  # exact frame index
        recall_text.tStart = t  # local t and not account for scr refresh
        recall_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(recall_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'recall_text.started')
        # update status
        recall_text.status = STARTED
        recall_text.setAutoDraw(True)
    
    # if recall_text is active this frame...
    if recall_text.status == STARTED:
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
    for thisComponent in instruct_recallComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruct_recall" ---
for thisComponent in instruct_recallComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "instruct_recall" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruct_imagine" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from imagine_code
# skip recall instructions if recalling
if int(expInfo['session']) % 2 == 1:
    continueRoutine = False
# setup some python lists for storing info about the imagine_mouse
imagine_mouse.clicked_name = []
gotValidClick = False  # until a click is received
imagine_text.setText('In this section you will imagine game plays.\n\nYou will be shown a starting position (spot and player) from which to imagine a game from beginning to end. At the end of each imagined game, you will be asked who won (you vs. the opponent). The game board will transition to the question screen automatically.\n\nPlease imagine and respond as best you can!')
# keep track of which components have finished
instruct_imagineComponents = [imagine_title, imagine_button, imagine_ready, imagine_mouse, imagine_text]
for thisComponent in instruct_imagineComponents:
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

# --- Run Routine "instruct_imagine" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *imagine_title* updates
    
    # if imagine_title is starting this frame...
    if imagine_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        imagine_title.frameNStart = frameN  # exact frame index
        imagine_title.tStart = t  # local t and not account for scr refresh
        imagine_title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagine_title, 'tStartRefresh')  # time at next scr refresh
        # update status
        imagine_title.status = STARTED
        imagine_title.setAutoDraw(True)
    
    # if imagine_title is active this frame...
    if imagine_title.status == STARTED:
        # update params
        pass
    
    # *imagine_button* updates
    
    # if imagine_button is starting this frame...
    if imagine_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        imagine_button.frameNStart = frameN  # exact frame index
        imagine_button.tStart = t  # local t and not account for scr refresh
        imagine_button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagine_button, 'tStartRefresh')  # time at next scr refresh
        # update status
        imagine_button.status = STARTED
        imagine_button.setAutoDraw(True)
    
    # if imagine_button is active this frame...
    if imagine_button.status == STARTED:
        # update params
        pass
    
    # *imagine_ready* updates
    
    # if imagine_ready is starting this frame...
    if imagine_ready.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        imagine_ready.frameNStart = frameN  # exact frame index
        imagine_ready.tStart = t  # local t and not account for scr refresh
        imagine_ready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagine_ready, 'tStartRefresh')  # time at next scr refresh
        # update status
        imagine_ready.status = STARTED
        imagine_ready.setAutoDraw(True)
    
    # if imagine_ready is active this frame...
    if imagine_ready.status == STARTED:
        # update params
        pass
    # *imagine_mouse* updates
    
    # if imagine_mouse is starting this frame...
    if imagine_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        imagine_mouse.frameNStart = frameN  # exact frame index
        imagine_mouse.tStart = t  # local t and not account for scr refresh
        imagine_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagine_mouse, 'tStartRefresh')  # time at next scr refresh
        # update status
        imagine_mouse.status = STARTED
        imagine_mouse.mouseClock.reset()
        prevButtonState = imagine_mouse.getPressed()  # if button is down already this ISN'T a new click
    if imagine_mouse.status == STARTED:  # only update if started and not finished!
        buttons = imagine_mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                clickableList = environmenttools.getFromNames(imagine_button, namespace=locals())
                for obj in clickableList:
                    # is this object clicked on?
                    if obj.contains(imagine_mouse):
                        gotValidClick = True
                        imagine_mouse.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # end routine on response
    
    # *imagine_text* updates
    
    # if imagine_text is starting this frame...
    if imagine_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        imagine_text.frameNStart = frameN  # exact frame index
        imagine_text.tStart = t  # local t and not account for scr refresh
        imagine_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagine_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'imagine_text.started')
        # update status
        imagine_text.status = STARTED
        imagine_text.setAutoDraw(True)
    
    # if imagine_text is active this frame...
    if imagine_text.status == STARTED:
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
    for thisComponent in instruct_imagineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruct_imagine" ---
for thisComponent in instruct_imagineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "instruct_imagine" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
double_click_2 = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='double_click_2')
thisExp.addLoop(double_click_2)  # add the loop to the experiment
thisDouble_click_2 = double_click_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDouble_click_2.rgb)
if thisDouble_click_2 != None:
    for paramName in thisDouble_click_2:
        exec('{} = thisDouble_click_2[paramName]'.format(paramName))

for thisDouble_click_2 in double_click_2:
    currentLoop = double_click_2
    # abbreviate parameter names if possible (e.g. rgb = thisDouble_click_2.rgb)
    if thisDouble_click_2 != None:
        for paramName in thisDouble_click_2:
            exec('{} = thisDouble_click_2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "section_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from section_2_code
    # shuffle order of reference games
    game_idxs = []
    for game in range(num_games):
        game_idxs.append(game + 1)
    random.shuffle(game_idxs)
    
    game_idx = 0 # initialize game index counter
    section = 2 # variable for experiment section
    move_duration = 0.75 # how long moves take
    end_pause_duration = 0.75*0.75 # game-end pause amt
    # setup some python lists for storing info about the mouse_2
    mouse_2.clicked_name = []
    gotValidClick = False  # until a click is received
    section_2_text.setText('Click the button below when you are ready to start visualizing games and recording winners.')
    # keep track of which components have finished
    section_2Components = [title_2, button_2, button_2_text, mouse_2, section_2_text]
    for thisComponent in section_2Components:
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
    
    # --- Run Routine "section_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *title_2* updates
        
        # if title_2 is starting this frame...
        if title_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            title_2.frameNStart = frameN  # exact frame index
            title_2.tStart = t  # local t and not account for scr refresh
            title_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(title_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            title_2.status = STARTED
            title_2.setAutoDraw(True)
        
        # if title_2 is active this frame...
        if title_2.status == STARTED:
            # update params
            pass
        
        # *button_2* updates
        
        # if button_2 is starting this frame...
        if button_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_2.frameNStart = frameN  # exact frame index
            button_2.tStart = t  # local t and not account for scr refresh
            button_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            button_2.status = STARTED
            button_2.setAutoDraw(True)
        
        # if button_2 is active this frame...
        if button_2.status == STARTED:
            # update params
            pass
        
        # *button_2_text* updates
        
        # if button_2_text is starting this frame...
        if button_2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_2_text.frameNStart = frameN  # exact frame index
            button_2_text.tStart = t  # local t and not account for scr refresh
            button_2_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_2_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            button_2_text.status = STARTED
            button_2_text.setAutoDraw(True)
        
        # if button_2_text is active this frame...
        if button_2_text.status == STARTED:
            # update params
            pass
        # *mouse_2* updates
        
        # if mouse_2 is starting this frame...
        if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.tStart = t  # local t and not account for scr refresh
            mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            mouse_2.status = STARTED
            mouse_2.mouseClock.reset()
            prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
        if mouse_2.status == STARTED:  # only update if started and not finished!
            buttons = mouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(button_2, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_2):
                            gotValidClick = True
                            mouse_2.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
        # *section_2_text* updates
        
        # if section_2_text is starting this frame...
        if section_2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            section_2_text.frameNStart = frameN  # exact frame index
            section_2_text.tStart = t  # local t and not account for scr refresh
            section_2_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(section_2_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'section_2_text.started')
            # update status
            section_2_text.status = STARTED
            section_2_text.setAutoDraw(True)
        
        # if section_2_text is active this frame...
        if section_2_text.status == STARTED:
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
        for thisComponent in section_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "section_2" ---
    for thisComponent in section_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for double_click_2 (TrialHandler)
    # the Routine "section_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 2.0 repeats of 'double_click_2'


# set up handler to look after randomisation of conditions etc
intervention_games = data.TrialHandler(nReps=num_games, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='intervention_games')
thisExp.addLoop(intervention_games)  # add the loop to the experiment
thisIntervention_game = intervention_games.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisIntervention_game.rgb)
if thisIntervention_game != None:
    for paramName in thisIntervention_game:
        exec('{} = thisIntervention_game[paramName]'.format(paramName))

for thisIntervention_game in intervention_games:
    currentLoop = intervention_games
    # abbreviate parameter names if possible (e.g. rgb = thisIntervention_game.rgb)
    if thisIntervention_game != None:
        for paramName in thisIntervention_game:
            exec('{} = thisIntervention_game[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "intervention_countdown" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from intervention_countdown_code
    event.Mouse(visible=False)
    
    # Make sure replay/imagination shows correctly
    visibility = int(expInfo['session']) % 2
    practice_turns.finished = False
    
    move_idx = 0
    
    # select reference game data frame
    df_1 = df[df.section == 1]
    ref_df = df_1[df_1.game == game_idxs[game_idx]]
    ref_df = ref_df.reset_index()
    print(ref_df.to_string())
    #print('move_idx: ' + str(move_idx))
    
    # set starting position
    row = ref_df.loc[move_idx, 'start_row']
    col = ref_df.loc[move_idx, 'start_col']
    row_new = row
    col_new = col
    #print('row: '+ str(row))
    #print('col: '+ str(col))
    
    winner = ref_df.loc[len(ref_df) - 1, 'winner']
    if winner == 'human':
        player_won = True
    else:
        player_won = False
    
    if visibility == 0:
        # we add 0.75 for the end_pause
        whole_game_duration = sum(ref_df['DT']) + 0.75
    
    if ref_df.loc[move_idx, 'player'] == 'AI':
        npc_start = True
        piece_color = 'chestnut'
    else:
        npc_start = False
        piece_color = 'dodgerblue'
    
    # advance game idx counter
    game_idx = game_idx + 1
    intervention_blue_piece.setOpacity(1 - npc_start)
    intervention_blue_piece.setPos(((col-7)/17, (15-row-8)/17))
    intervention_red_piece.setOpacity(npc_start)
    intervention_red_piece.setPos(((col-7)/17, (15-row-8)/17))
    # keep track of which components have finished
    intervention_countdownComponents = [intervention_countdown_text, intervention_blue_piece, intervention_red_piece]
    for thisComponent in intervention_countdownComponents:
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
    
    # --- Run Routine "intervention_countdown" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from intervention_countdown_code
        for square in squares:
            square.draw()
        
        # *intervention_countdown_text* updates
        
        # if intervention_countdown_text is starting this frame...
        if intervention_countdown_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intervention_countdown_text.frameNStart = frameN  # exact frame index
            intervention_countdown_text.tStart = t  # local t and not account for scr refresh
            intervention_countdown_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intervention_countdown_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            intervention_countdown_text.status = STARTED
            intervention_countdown_text.setAutoDraw(True)
        
        # if intervention_countdown_text is active this frame...
        if intervention_countdown_text.status == STARTED:
            # update params
            intervention_countdown_text.setText((3 - math.floor(t)), log=False)
        
        # if intervention_countdown_text is stopping this frame...
        if intervention_countdown_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > intervention_countdown_text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                intervention_countdown_text.tStop = t  # not accounting for scr refresh
                intervention_countdown_text.frameNStop = frameN  # exact frame index
                # update status
                intervention_countdown_text.status = FINISHED
                intervention_countdown_text.setAutoDraw(False)
        
        # *intervention_blue_piece* updates
        
        # if intervention_blue_piece is starting this frame...
        if intervention_blue_piece.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intervention_blue_piece.frameNStart = frameN  # exact frame index
            intervention_blue_piece.tStart = t  # local t and not account for scr refresh
            intervention_blue_piece.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intervention_blue_piece, 'tStartRefresh')  # time at next scr refresh
            # update status
            intervention_blue_piece.status = STARTED
            intervention_blue_piece.setAutoDraw(True)
        
        # if intervention_blue_piece is active this frame...
        if intervention_blue_piece.status == STARTED:
            # update params
            pass
        
        # if intervention_blue_piece is stopping this frame...
        if intervention_blue_piece.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > intervention_blue_piece.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                intervention_blue_piece.tStop = t  # not accounting for scr refresh
                intervention_blue_piece.frameNStop = frameN  # exact frame index
                # update status
                intervention_blue_piece.status = FINISHED
                intervention_blue_piece.setAutoDraw(False)
        
        # *intervention_red_piece* updates
        
        # if intervention_red_piece is starting this frame...
        if intervention_red_piece.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intervention_red_piece.frameNStart = frameN  # exact frame index
            intervention_red_piece.tStart = t  # local t and not account for scr refresh
            intervention_red_piece.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intervention_red_piece, 'tStartRefresh')  # time at next scr refresh
            # update status
            intervention_red_piece.status = STARTED
            intervention_red_piece.setAutoDraw(True)
        
        # if intervention_red_piece is active this frame...
        if intervention_red_piece.status == STARTED:
            # update params
            pass
        
        # if intervention_red_piece is stopping this frame...
        if intervention_red_piece.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > intervention_red_piece.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                intervention_red_piece.tStop = t  # not accounting for scr refresh
                intervention_red_piece.frameNStop = frameN  # exact frame index
                # update status
                intervention_red_piece.status = FINISHED
                intervention_red_piece.setAutoDraw(False)
        
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
        for thisComponent in intervention_countdownComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "intervention_countdown" ---
    for thisComponent in intervention_countdownComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # --- Prepare to start Routine "imagination_prompt" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from prompt_code
    event.Mouse(visible=False)
    
    if visibility == 1:
        continueRoutine = False
    prompt_piece.setFillColor(piece_color)
    prompt_piece.setPos(((col-7)/17, (15-row-8)/17))
    prompt_piece.setLineColor(piece_color)
    # keep track of which components have finished
    imagination_promptComponents = [prompt_piece]
    for thisComponent in imagination_promptComponents:
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
    
    # --- Run Routine "imagination_prompt" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from prompt_code
        for square in squares:
            square.draw()
        
        # *prompt_piece* updates
        
        # if prompt_piece is starting this frame...
        if prompt_piece.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prompt_piece.frameNStart = frameN  # exact frame index
            prompt_piece.tStart = t  # local t and not account for scr refresh
            prompt_piece.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prompt_piece, 'tStartRefresh')  # time at next scr refresh
            # update status
            prompt_piece.status = STARTED
            prompt_piece.setAutoDraw(True)
        
        # if prompt_piece is active this frame...
        if prompt_piece.status == STARTED:
            # update params
            pass
        
        # if prompt_piece is stopping this frame...
        if prompt_piece.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prompt_piece.tStartRefresh + whole_game_duration * 0.75-frameTolerance:
                # keep track of stop time/frame for later
                prompt_piece.tStop = t  # not accounting for scr refresh
                prompt_piece.frameNStop = frameN  # exact frame index
                # update status
                prompt_piece.status = FINISHED
                prompt_piece.setAutoDraw(False)
        
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
        for thisComponent in imagination_promptComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "imagination_prompt" ---
    for thisComponent in imagination_promptComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "imagination_prompt" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    intervention_moves = data.TrialHandler(nReps=15.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='intervention_moves')
    thisExp.addLoop(intervention_moves)  # add the loop to the experiment
    thisIntervention_move = intervention_moves.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisIntervention_move.rgb)
    if thisIntervention_move != None:
        for paramName in thisIntervention_move:
            exec('{} = thisIntervention_move[paramName]'.format(paramName))
    
    for thisIntervention_move in intervention_moves:
        currentLoop = intervention_moves
        # abbreviate parameter names if possible (e.g. rgb = thisIntervention_move.rgb)
        if thisIntervention_move != None:
            for paramName in thisIntervention_move:
                exec('{} = thisIntervention_move[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "intervention_player_wait" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from intervention_code
        event.Mouse(visible=False)
        
        if npc_start or visibility == 0:
            continueRoutine = False
        elif row_new == col_new == 0:
            intervention_moves.finished = True
            practice_turns.finished = True
            npc_start = True
            continueRoutine = False
        else:
            print('move_idx: ' + str(move_idx))
            
            pause_duration = ref_df.loc[move_idx, 'DT']
            
            row = ref_df.loc[move_idx, 'start_row']
            col = ref_df.loc[move_idx, 'start_col']
            row_new = ref_df.loc[move_idx, 'end_row']
            col_new = ref_df.loc[move_idx, 'end_col']
            
            move_idx = move_idx + 1
        intervention_piece.setPos(((col-7)/17, (15-row-8)/17))
        # keep track of which components have finished
        intervention_player_waitComponents = [intervention_piece]
        for thisComponent in intervention_player_waitComponents:
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
        
        # --- Run Routine "intervention_player_wait" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from intervention_code
            for square in squares:
                square.draw()
            
            # *intervention_piece* updates
            
            # if intervention_piece is starting this frame...
            if intervention_piece.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                intervention_piece.frameNStart = frameN  # exact frame index
                intervention_piece.tStart = t  # local t and not account for scr refresh
                intervention_piece.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(intervention_piece, 'tStartRefresh')  # time at next scr refresh
                # update status
                intervention_piece.status = STARTED
                intervention_piece.setAutoDraw(True)
            
            # if intervention_piece is active this frame...
            if intervention_piece.status == STARTED:
                # update params
                pass
            
            # if intervention_piece is stopping this frame...
            if intervention_piece.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > intervention_piece.tStartRefresh + pause_duration * 0.75-frameTolerance:
                    # keep track of stop time/frame for later
                    intervention_piece.tStop = t  # not accounting for scr refresh
                    intervention_piece.frameNStop = frameN  # exact frame index
                    # update status
                    intervention_piece.status = FINISHED
                    intervention_piece.setAutoDraw(False)
            
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
            for thisComponent in intervention_player_waitComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "intervention_player_wait" ---
        for thisComponent in intervention_player_waitComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "intervention_player_wait" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "make_move" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from move_code
        event.Mouse(visible=False)
        
        #timer = core.Clock()
        #timer.reset()
        
        if npc_start or visibility == 0:
            npc_start = False
            continueRoutine = False
        moving_piece.setOpacity(visibility)
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
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from move_code
            for square in squares:
                square.draw()
            
            #if timer.getTime() > move_duration:
            #    continueRoutine = False
            
            # *moving_piece* updates
            
            # if moving_piece is starting this frame...
            if moving_piece.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                moving_piece.frameNStart = frameN  # exact frame index
                moving_piece.tStart = t  # local t and not account for scr refresh
                moving_piece.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(moving_piece, 'tStartRefresh')  # time at next scr refresh
                # update status
                moving_piece.status = STARTED
                moving_piece.setAutoDraw(True)
            
            # if moving_piece is active this frame...
            if moving_piece.status == STARTED:
                # update params
                moving_piece.setPos(((((1-min(move_duration,t)/move_duration)*col+min(move_duration,t)/move_duration*col_new)-7)/17, (15-((1-min(move_duration,t)/move_duration)*row+min(move_duration,t)/move_duration*row_new)-8)/17), log=False)
            
            # if moving_piece is stopping this frame...
            if moving_piece.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > moving_piece.tStartRefresh + move_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    moving_piece.tStop = t  # not accounting for scr refresh
                    moving_piece.frameNStop = frameN  # exact frame index
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
            if player_won == None:
                player_won = True
            num_wins = num_wins + 1
            practice_turns.finished = True
            if section == 1:
                turns.finished = True
            if section == 3:
                more_turns.finished = True
            if section == 4:
                turns_4.finished = True
            continueRoutine = False
        # the Routine "make_move" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "intervention_npc_wait" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from intervention_wait_code
        event.Mouse(visible=False)
        
        if practice_turns.finished or visibility == 0:
            continueRoutine = False
        elif row_new == col_new == 0:
            intervention_moves.finished = True
            practice_turns.finished = True
            npc_start = True
            continueRoutine = False
        else:
            print('move_idx: ' + str(move_idx))
            
            pause_duration = ref_df.loc[move_idx, 'DT']
            
            row = ref_df.loc[move_idx, 'start_row']
            col = ref_df.loc[move_idx, 'start_col']
            row_new = ref_df.loc[move_idx, 'end_row']
            col_new = ref_df.loc[move_idx, 'end_col']
            
            move_idx = move_idx + 1
        intervention_npc.setPos(((col-7)/17, (15-row-8)/17))
        # keep track of which components have finished
        intervention_npc_waitComponents = [intervention_npc]
        for thisComponent in intervention_npc_waitComponents:
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
        
        # --- Run Routine "intervention_npc_wait" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from intervention_wait_code
            for square in squares:
                square.draw()
            
            # *intervention_npc* updates
            
            # if intervention_npc is starting this frame...
            if intervention_npc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                intervention_npc.frameNStart = frameN  # exact frame index
                intervention_npc.tStart = t  # local t and not account for scr refresh
                intervention_npc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(intervention_npc, 'tStartRefresh')  # time at next scr refresh
                # update status
                intervention_npc.status = STARTED
                intervention_npc.setAutoDraw(True)
            
            # if intervention_npc is active this frame...
            if intervention_npc.status == STARTED:
                # update params
                pass
            
            # if intervention_npc is stopping this frame...
            if intervention_npc.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > intervention_npc.tStartRefresh + pause_duration * 0.75-frameTolerance:
                    # keep track of stop time/frame for later
                    intervention_npc.tStop = t  # not accounting for scr refresh
                    intervention_npc.frameNStop = frameN  # exact frame index
                    # update status
                    intervention_npc.status = FINISHED
                    intervention_npc.setAutoDraw(False)
            
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
            for thisComponent in intervention_npc_waitComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "intervention_npc_wait" ---
        for thisComponent in intervention_npc_waitComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "intervention_npc_wait" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "npc_move" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from npc_code
        event.Mouse(visible=False)
        
        #timer = core.Clock()
        #timer.reset()
        
        if practice_turns.finished or visibility == 0:
            continueRoutine = False
        moving_npc.setOpacity(visibility)
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
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from npc_code
            for square in squares:
                square.draw()
            
            #if timer.getTime() > move_duration:
            #    continueRoutine = False
            
            # *moving_npc* updates
            
            # if moving_npc is starting this frame...
            if moving_npc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                moving_npc.frameNStart = frameN  # exact frame index
                moving_npc.tStart = t  # local t and not account for scr refresh
                moving_npc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(moving_npc, 'tStartRefresh')  # time at next scr refresh
                # update status
                moving_npc.status = STARTED
                moving_npc.setAutoDraw(True)
            
            # if moving_npc is active this frame...
            if moving_npc.status == STARTED:
                # update params
                moving_npc.setPos(((((1-min(move_duration,t)/move_duration)*col+min(move_duration,t)/move_duration*col_new)-7)/17, (15-((1-min(move_duration,t)/move_duration)*row+min(move_duration,t)/move_duration*row_new)-8)/17), log=False)
            
            # if moving_npc is stopping this frame...
            if moving_npc.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > moving_npc.tStartRefresh + move_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    moving_npc.tStop = t  # not accounting for scr refresh
                    moving_npc.frameNStop = frameN  # exact frame index
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
            practice_turns.finished = True
            if section == 1:
                turns.finished = True
            if section == 3:
                more_turns.finished = True
            if section == 4:
                turns_4.finished = True
        # the Routine "npc_move" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 15.0 repeats of 'intervention_moves'
    
    
    # --- Prepare to start Routine "end_pause" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from end_code
    event.Mouse(visible=False)
    
    row = row_new
    col = col_new
    
    if visibility == 0:
        continueRoutine = False
    
    #print(df.to_string())
    end_blue.setOpacity(player_won)
    end_blue.setPos(((col-7)/17, (15-row-8)/17))
    end_red.setOpacity(1 - player_won)
    end_red.setPos(((col-7)/17, (15-row-8)/17))
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
    while continueRoutine:
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
            if tThisFlipGlobal > end_blue.tStartRefresh + end_pause_duration-frameTolerance:
                # keep track of stop time/frame for later
                end_blue.tStop = t  # not accounting for scr refresh
                end_blue.frameNStop = frameN  # exact frame index
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
            if tThisFlipGlobal > end_red.tStartRefresh + end_pause_duration-frameTolerance:
                # keep track of stop time/frame for later
                end_red.tStop = t  # not accounting for scr refresh
                end_red.frameNStop = frameN  # exact frame index
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
    # the Routine "end_pause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "who_won" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from who_won_code
    choice_mouse.setPos(newPos=(0,0))
    event.Mouse(visible=True)
    
    timer = core.Clock()
    timer.reset()
    # setup some python lists for storing info about the choice_mouse
    choice_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    who_wonComponents = [who_won_title, opponent_button, opponent_text, me_button, me_text, choice_mouse]
    for thisComponent in who_wonComponents:
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
    
    # --- Run Routine "who_won" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *who_won_title* updates
        
        # if who_won_title is starting this frame...
        if who_won_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            who_won_title.frameNStart = frameN  # exact frame index
            who_won_title.tStart = t  # local t and not account for scr refresh
            who_won_title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(who_won_title, 'tStartRefresh')  # time at next scr refresh
            # update status
            who_won_title.status = STARTED
            who_won_title.setAutoDraw(True)
        
        # if who_won_title is active this frame...
        if who_won_title.status == STARTED:
            # update params
            pass
        
        # *opponent_button* updates
        
        # if opponent_button is starting this frame...
        if opponent_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            opponent_button.frameNStart = frameN  # exact frame index
            opponent_button.tStart = t  # local t and not account for scr refresh
            opponent_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(opponent_button, 'tStartRefresh')  # time at next scr refresh
            # update status
            opponent_button.status = STARTED
            opponent_button.setAutoDraw(True)
        
        # if opponent_button is active this frame...
        if opponent_button.status == STARTED:
            # update params
            pass
        
        # *opponent_text* updates
        
        # if opponent_text is starting this frame...
        if opponent_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            opponent_text.frameNStart = frameN  # exact frame index
            opponent_text.tStart = t  # local t and not account for scr refresh
            opponent_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(opponent_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            opponent_text.status = STARTED
            opponent_text.setAutoDraw(True)
        
        # if opponent_text is active this frame...
        if opponent_text.status == STARTED:
            # update params
            pass
        
        # *me_button* updates
        
        # if me_button is starting this frame...
        if me_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            me_button.frameNStart = frameN  # exact frame index
            me_button.tStart = t  # local t and not account for scr refresh
            me_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(me_button, 'tStartRefresh')  # time at next scr refresh
            # update status
            me_button.status = STARTED
            me_button.setAutoDraw(True)
        
        # if me_button is active this frame...
        if me_button.status == STARTED:
            # update params
            pass
        
        # *me_text* updates
        
        # if me_text is starting this frame...
        if me_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            me_text.frameNStart = frameN  # exact frame index
            me_text.tStart = t  # local t and not account for scr refresh
            me_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(me_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            me_text.status = STARTED
            me_text.setAutoDraw(True)
        
        # if me_text is active this frame...
        if me_text.status == STARTED:
            # update params
            pass
        # *choice_mouse* updates
        
        # if choice_mouse is starting this frame...
        if choice_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_mouse.frameNStart = frameN  # exact frame index
            choice_mouse.tStart = t  # local t and not account for scr refresh
            choice_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_mouse, 'tStartRefresh')  # time at next scr refresh
            # update status
            choice_mouse.status = STARTED
            choice_mouse.mouseClock.reset()
            prevButtonState = choice_mouse.getPressed()  # if button is down already this ISN'T a new click
        if choice_mouse.status == STARTED:  # only update if started and not finished!
            buttons = choice_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames([opponent_button, me_button], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(choice_mouse):
                            gotValidClick = True
                            choice_mouse.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
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
        for thisComponent in who_wonComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "who_won" ---
    for thisComponent in who_wonComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from who_won_code
    if npc_start == False:
        df = df.append(pd.Series(dtype = 'object'), ignore_index = True)
        df.loc[len(df) - 1, 'session'] = expInfo['session']
        df.loc[len(df) - 1, 'section'] = section
        if visibility == 0:
            df.loc[len(df) - 1, 'type'] = 'img'
        else:
            df.loc[len(df) - 1, 'type'] = 'mem'
        df.loc[len(df) - 1, 'game'] = game_idx
        df.loc[len(df) - 1, 'ref_game'] = game_idxs[game_idx - 1]
        df.loc[len(df) - 1, 'start_row'] = ref_df.loc[0, 'start_row']
        df.loc[len(df) - 1, 'start_col'] = ref_df.loc[0, 'start_col']
        if choice_mouse.clicked_name[0] == 'me_button':
            df.loc[len(df) - 1, 'chosen_winner'] = 'human'
        else:
            df.loc[len(df) - 1, 'chosen_winner'] = 'AI'
        df.loc[len(df) - 1, 'DT'] = timer.getTime()
    # store data for intervention_games (TrialHandler)
    # the Routine "who_won" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed num_games repeats of 'intervention_games'


# set up handler to look after randomisation of conditions etc
double_click_3 = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='double_click_3')
thisExp.addLoop(double_click_3)  # add the loop to the experiment
thisDouble_click_3 = double_click_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDouble_click_3.rgb)
if thisDouble_click_3 != None:
    for paramName in thisDouble_click_3:
        exec('{} = thisDouble_click_3[paramName]'.format(paramName))

for thisDouble_click_3 in double_click_3:
    currentLoop = double_click_3
    # abbreviate parameter names if possible (e.g. rgb = thisDouble_click_3.rgb)
    if thisDouble_click_3 != None:
        for paramName in thisDouble_click_3:
            exec('{} = thisDouble_click_3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "section_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_3
    # generate shuffled list of who starts each game
    npc_starts = []
    for game in range(int(num_games/2)):
        npc_starts.append(True)
        npc_starts.append(False)
    random.shuffle(npc_starts)
    
    game = 0 # initialize game counter
    num_wins = 0 # initialize win counter
    visibility = 1 # pieces are visible for Section 3
    section = 3 # variable for experiment section
    move_duration = 1 # how long moves take
    end_pause_duration = 0.75 # game-end pause amt
    # setup some python lists for storing info about the mouse_3
    mouse_3.clicked_name = []
    gotValidClick = False  # until a click is received
    section_3_text.setText('In this section you will play more games like in Section 1. Click the button below when you are ready to start.')
    # keep track of which components have finished
    section_3Components = [title_3, button_3, button_3_text, mouse_3, section_3_text]
    for thisComponent in section_3Components:
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
    
    # --- Run Routine "section_3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *title_3* updates
        
        # if title_3 is starting this frame...
        if title_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            title_3.frameNStart = frameN  # exact frame index
            title_3.tStart = t  # local t and not account for scr refresh
            title_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(title_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            title_3.status = STARTED
            title_3.setAutoDraw(True)
        
        # if title_3 is active this frame...
        if title_3.status == STARTED:
            # update params
            pass
        
        # *button_3* updates
        
        # if button_3 is starting this frame...
        if button_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_3.frameNStart = frameN  # exact frame index
            button_3.tStart = t  # local t and not account for scr refresh
            button_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            button_3.status = STARTED
            button_3.setAutoDraw(True)
        
        # if button_3 is active this frame...
        if button_3.status == STARTED:
            # update params
            pass
        
        # *button_3_text* updates
        
        # if button_3_text is starting this frame...
        if button_3_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_3_text.frameNStart = frameN  # exact frame index
            button_3_text.tStart = t  # local t and not account for scr refresh
            button_3_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_3_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            button_3_text.status = STARTED
            button_3_text.setAutoDraw(True)
        
        # if button_3_text is active this frame...
        if button_3_text.status == STARTED:
            # update params
            pass
        # *mouse_3* updates
        
        # if mouse_3 is starting this frame...
        if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_3.frameNStart = frameN  # exact frame index
            mouse_3.tStart = t  # local t and not account for scr refresh
            mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            mouse_3.status = STARTED
            mouse_3.mouseClock.reset()
            prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
        if mouse_3.status == STARTED:  # only update if started and not finished!
            buttons = mouse_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(button_3, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_3):
                            gotValidClick = True
                            mouse_3.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
        # *section_3_text* updates
        
        # if section_3_text is starting this frame...
        if section_3_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            section_3_text.frameNStart = frameN  # exact frame index
            section_3_text.tStart = t  # local t and not account for scr refresh
            section_3_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(section_3_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'section_3_text.started')
            # update status
            section_3_text.status = STARTED
            section_3_text.setAutoDraw(True)
        
        # if section_3_text is active this frame...
        if section_3_text.status == STARTED:
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
        for thisComponent in section_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "section_3" ---
    for thisComponent in section_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for double_click_3 (TrialHandler)
    # the Routine "section_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 2.0 repeats of 'double_click_3'


# set up handler to look after randomisation of conditions etc
more_games = data.TrialHandler(nReps=num_games, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='more_games')
thisExp.addLoop(more_games)  # add the loop to the experiment
thisMore_game = more_games.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMore_game.rgb)
if thisMore_game != None:
    for paramName in thisMore_game:
        exec('{} = thisMore_game[paramName]'.format(paramName))

for thisMore_game in more_games:
    currentLoop = more_games
    # abbreviate parameter names if possible (e.g. rgb = thisMore_game.rgb)
    if thisMore_game != None:
        for paramName in thisMore_game:
            exec('{} = thisMore_game[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "countdown" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from countdown_code
    event.Mouse(visible=False)
    
    import random
    import math
    
    if section == 1 or section == 3 or section == 4:
        practice_turns.finished = False
    
    player_won = None
    npc_start = npc_starts[game]
    game = game + 1
    
    move_num = 0 # initialize move counter
    
    row = random.randint(0,14)
    col = random.randint(0,14)
    
    while row == col == 0:
        row = random.randint(0,14)
        col = random.randint(0,14)
    
    row_new = row
    col_new = col
    blue_piece.setOpacity(1 - npc_start)
    blue_piece.setPos(((col-7)/17, (15-row-8)/17))
    red_piece.setOpacity(npc_start)
    red_piece.setPos(((col-7)/17, (15-row-8)/17))
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
    more_turns = data.TrialHandler(nReps=15.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='more_turns')
    thisExp.addLoop(more_turns)  # add the loop to the experiment
    thisMore_turn = more_turns.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMore_turn.rgb)
    if thisMore_turn != None:
        for paramName in thisMore_turn:
            exec('{} = thisMore_turn[paramName]'.format(paramName))
    
    for thisMore_turn in more_turns:
        currentLoop = more_turns
        # abbreviate parameter names if possible (e.g. rgb = thisMore_turn.rgb)
        if thisMore_turn != None:
            for paramName in thisMore_turn:
                exec('{} = thisMore_turn[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "select_move" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        mouse.setPos(newPos=(0,0))
        event.Mouse(visible=True)
        
        if npc_start:
            continueRoutine = False
        
        timer = core.Clock()
        timer.reset()
        RT = 0
        
        row = row_new
        col = col_new
        
        mouse_still = True
        mouse_start = mouse.getPos()
        piece.setPos(((col-7)/17, (15-row-8)/17))
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
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
            # record mouse move onset time (RT)
            if mouse_still and any(mouse.getPos() != mouse_start):
                RT = timer.getTime()
                mouse_moved = True
            
            # on click, check for valid move selection
            if mouse.getPressed()[0] == 1:
                mouse_x, mouse_y = mouse.getPos()
                row_new = round(0 - ((mouse_y * 17) + 8 - 15))
                col_new = round((mouse_x * 17) + 7)
                if row_new <= row and col_new <= col:
                    if row_new >= 0 and col_new >= 0:
                        if row_new==row or col_new==col or (section != 4 and row-row_new == col-col_new):
                            if row_new != row or col_new != col:
                                if section != 4 or int(expInfo['session']) % 2 == 1 or euclid_move(move):
                                    continueRoutine = False
            
            # draw game board
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
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
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
        # Run 'End Routine' code from code
        if npc_start == False:
            move_num = move_num + 1
            df = df.append(pd.Series(dtype = 'object'), ignore_index = True)
            df.loc[len(df) - 1, 'session'] = expInfo['session']
            df.loc[len(df) - 1, 'section'] = section
            if section == 4 and int(expInfo['session']) % 2 == 0:
                df.loc[len(df) - 1, 'type'] = 'euc'
            if section == 4 and int(expInfo['session']) % 2 == 1:
                df.loc[len(df) - 1, 'type'] = 'nim'
            df.loc[len(df) - 1, 'game'] = game
            df.loc[len(df) - 1, 'move_num'] = move_num
            df.loc[len(df) - 1, 'player'] = 'human'
            df.loc[len(df) - 1, 'start_row'] = row
            df.loc[len(df) - 1, 'start_col'] = col
            df.loc[len(df) - 1, 'end_row'] = row_new
            df.loc[len(df) - 1, 'end_col'] = col_new
            df.loc[len(df) - 1, 'RT'] = RT
            df.loc[len(df) - 1, 'DT'] = timer.getTime()
            #print(df.to_string())
        # store data for more_turns (TrialHandler)
        more_turns.addData('mouse.x', mouse.x)
        more_turns.addData('mouse.y', mouse.y)
        more_turns.addData('mouse.leftButton', mouse.leftButton)
        more_turns.addData('mouse.midButton', mouse.midButton)
        more_turns.addData('mouse.rightButton', mouse.rightButton)
        more_turns.addData('mouse.time', mouse.time)
        # the Routine "select_move" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "make_move" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from move_code
        event.Mouse(visible=False)
        
        #timer = core.Clock()
        #timer.reset()
        
        if npc_start or visibility == 0:
            npc_start = False
            continueRoutine = False
        moving_piece.setOpacity(visibility)
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
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from move_code
            for square in squares:
                square.draw()
            
            #if timer.getTime() > move_duration:
            #    continueRoutine = False
            
            # *moving_piece* updates
            
            # if moving_piece is starting this frame...
            if moving_piece.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                moving_piece.frameNStart = frameN  # exact frame index
                moving_piece.tStart = t  # local t and not account for scr refresh
                moving_piece.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(moving_piece, 'tStartRefresh')  # time at next scr refresh
                # update status
                moving_piece.status = STARTED
                moving_piece.setAutoDraw(True)
            
            # if moving_piece is active this frame...
            if moving_piece.status == STARTED:
                # update params
                moving_piece.setPos(((((1-min(move_duration,t)/move_duration)*col+min(move_duration,t)/move_duration*col_new)-7)/17, (15-((1-min(move_duration,t)/move_duration)*row+min(move_duration,t)/move_duration*row_new)-8)/17), log=False)
            
            # if moving_piece is stopping this frame...
            if moving_piece.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > moving_piece.tStartRefresh + move_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    moving_piece.tStop = t  # not accounting for scr refresh
                    moving_piece.frameNStop = frameN  # exact frame index
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
            if player_won == None:
                player_won = True
            num_wins = num_wins + 1
            practice_turns.finished = True
            if section == 1:
                turns.finished = True
            if section == 3:
                more_turns.finished = True
            if section == 4:
                turns_4.finished = True
            continueRoutine = False
        # the Routine "make_move" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "npc_wait" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from wait_code
        event.Mouse(visible=False)
        
        if practice_turns.finished:
            continueRoutine = False
        
        row = row_new
        col = col_new
        
        # select random opponent move
        moves = []
        Q_table = []
        
        if section != 4:
            optimal_moves = optimal_moves_wythoffs
        else:
            if int(expInfo['session']) % 2 == 0:
                optimal_moves = optimal_moves_euclid
            else:
                optimal_moves = optimal_moves_nim
        
        for r in range (row): # vertical moves
            move = (r, col)
            if section != 4 or int(expInfo['session']) % 2 == 1 or euclid_move(move):
                moves.append(move)
                if move in optimal_moves:
                    Q_table.append(1)
                else:
                    Q_table.append(0)
            
        for c in range (col): # horiz moves
            move = (row, c)
            if section != 4 or int(expInfo['session']) % 2 == 1 or euclid_move(move):
                moves.append(move)
                if move in optimal_moves:
                    Q_table.append(1)
                else:
                    Q_table.append(0)
            
        for d in range(1, min(row, col) + 1): # diag moves
            move = (row - d, col - d)
            if section != 4:
                moves.append(move)
                if move in optimal_moves:
                    Q_table.append(1)
                else:
                    Q_table.append(0)
        
        # action selection
        if len(moves) > 0:
            # calculate Boltzmann (softmax) action probs
            T = 0.55 # temperature parameter
            probs = np.exp(np.true_divide(Q_table,T))
            probs = np.true_divide(probs, sum(probs))
            action = np.random.choice(len(moves),p=probs)
            (row_new, col_new) = moves[action]
            # better to use np.random.Generator.choice
        npc.setPos(((col-7)/17, (15-row-8)/17))
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
        # Run 'End Routine' code from wait_code
        if practice_turns.finished == False:
            move_num = move_num + 1
            df = df.append(pd.Series(dtype = 'object'), ignore_index = True)
            df.loc[len(df) - 1, 'session'] = expInfo['session']
            df.loc[len(df) - 1, 'section'] = section
            df.loc[len(df) - 1, 'game'] = game
            df.loc[len(df) - 1, 'move_num'] = move_num
            df.loc[len(df) - 1, 'player'] = 'AI'
            df.loc[len(df) - 1, 'start_row'] = row
            df.loc[len(df) - 1, 'start_col'] = col
            df.loc[len(df) - 1, 'end_row'] = row_new
            df.loc[len(df) - 1, 'end_col'] = col_new
            df.loc[len(df) - 1, 'DT'] = 1.25
            #print(df.to_string())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.250000)
        
        # --- Prepare to start Routine "npc_move" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from npc_code
        event.Mouse(visible=False)
        
        #timer = core.Clock()
        #timer.reset()
        
        if practice_turns.finished or visibility == 0:
            continueRoutine = False
        moving_npc.setOpacity(visibility)
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
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from npc_code
            for square in squares:
                square.draw()
            
            #if timer.getTime() > move_duration:
            #    continueRoutine = False
            
            # *moving_npc* updates
            
            # if moving_npc is starting this frame...
            if moving_npc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                moving_npc.frameNStart = frameN  # exact frame index
                moving_npc.tStart = t  # local t and not account for scr refresh
                moving_npc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(moving_npc, 'tStartRefresh')  # time at next scr refresh
                # update status
                moving_npc.status = STARTED
                moving_npc.setAutoDraw(True)
            
            # if moving_npc is active this frame...
            if moving_npc.status == STARTED:
                # update params
                moving_npc.setPos(((((1-min(move_duration,t)/move_duration)*col+min(move_duration,t)/move_duration*col_new)-7)/17, (15-((1-min(move_duration,t)/move_duration)*row+min(move_duration,t)/move_duration*row_new)-8)/17), log=False)
            
            # if moving_npc is stopping this frame...
            if moving_npc.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > moving_npc.tStartRefresh + move_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    moving_npc.tStop = t  # not accounting for scr refresh
                    moving_npc.frameNStop = frameN  # exact frame index
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
            practice_turns.finished = True
            if section == 1:
                turns.finished = True
            if section == 3:
                more_turns.finished = True
            if section == 4:
                turns_4.finished = True
        # the Routine "npc_move" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 15.0 repeats of 'more_turns'
    
    
    # --- Prepare to start Routine "end_pause" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from end_code
    event.Mouse(visible=False)
    
    row = row_new
    col = col_new
    
    if visibility == 0:
        continueRoutine = False
    
    #print(df.to_string())
    end_blue.setOpacity(player_won)
    end_blue.setPos(((col-7)/17, (15-row-8)/17))
    end_red.setOpacity(1 - player_won)
    end_red.setPos(((col-7)/17, (15-row-8)/17))
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
    while continueRoutine:
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
            if tThisFlipGlobal > end_blue.tStartRefresh + end_pause_duration-frameTolerance:
                # keep track of stop time/frame for later
                end_blue.tStop = t  # not accounting for scr refresh
                end_blue.frameNStop = frameN  # exact frame index
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
            if tThisFlipGlobal > end_red.tStartRefresh + end_pause_duration-frameTolerance:
                # keep track of stop time/frame for later
                end_red.tStop = t  # not accounting for scr refresh
                end_red.frameNStop = frameN  # exact frame index
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
    # the Routine "end_pause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code
    event.Mouse(visible=True)
    
    if player_won:
        df.loc[(df.game==game) & (df.section==section), 'winner'] = 'human'
    else:
        df.loc[(df.game==game) & (df.section==section), 'winner'] = 'AI'
    feedback_win.setOpacity(player_won)
    feedback_lose.setOpacity(1 - player_won)
    status_text.setText('games played: ' + str(game) + ' of ' + str(num_games) + '\nwin percentage: ' + str(round (num_wins / game * 100)) + '%')
    # setup some python lists for storing info about the next_mouse
    next_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    feedbackComponents = [feedback_win, feedback_lose, status_text, button, button_text, next_mouse]
    for thisComponent in feedbackComponents:
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
    
    # --- Run Routine "feedback" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_win* updates
        
        # if feedback_win is starting this frame...
        if feedback_win.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_win.frameNStart = frameN  # exact frame index
            feedback_win.tStart = t  # local t and not account for scr refresh
            feedback_win.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_win, 'tStartRefresh')  # time at next scr refresh
            # update status
            feedback_win.status = STARTED
            feedback_win.setAutoDraw(True)
        
        # if feedback_win is active this frame...
        if feedback_win.status == STARTED:
            # update params
            pass
        
        # *feedback_lose* updates
        
        # if feedback_lose is starting this frame...
        if feedback_lose.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_lose.frameNStart = frameN  # exact frame index
            feedback_lose.tStart = t  # local t and not account for scr refresh
            feedback_lose.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_lose, 'tStartRefresh')  # time at next scr refresh
            # update status
            feedback_lose.status = STARTED
            feedback_lose.setAutoDraw(True)
        
        # if feedback_lose is active this frame...
        if feedback_lose.status == STARTED:
            # update params
            pass
        
        # *status_text* updates
        
        # if status_text is starting this frame...
        if status_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            status_text.frameNStart = frameN  # exact frame index
            status_text.tStart = t  # local t and not account for scr refresh
            status_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(status_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'status_text.started')
            # update status
            status_text.status = STARTED
            status_text.setAutoDraw(True)
        
        # if status_text is active this frame...
        if status_text.status == STARTED:
            # update params
            pass
        
        # *button* updates
        
        # if button is starting this frame...
        if button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button.frameNStart = frameN  # exact frame index
            button.tStart = t  # local t and not account for scr refresh
            button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
            # update status
            button.status = STARTED
            button.setAutoDraw(True)
        
        # if button is active this frame...
        if button.status == STARTED:
            # update params
            pass
        
        # *button_text* updates
        
        # if button_text is starting this frame...
        if button_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_text.frameNStart = frameN  # exact frame index
            button_text.tStart = t  # local t and not account for scr refresh
            button_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            button_text.status = STARTED
            button_text.setAutoDraw(True)
        
        # if button_text is active this frame...
        if button_text.status == STARTED:
            # update params
            pass
        # *next_mouse* updates
        
        # if next_mouse is starting this frame...
        if next_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next_mouse.frameNStart = frameN  # exact frame index
            next_mouse.tStart = t  # local t and not account for scr refresh
            next_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_mouse, 'tStartRefresh')  # time at next scr refresh
            # update status
            next_mouse.status = STARTED
            next_mouse.mouseClock.reset()
            prevButtonState = next_mouse.getPressed()  # if button is down already this ISN'T a new click
        if next_mouse.status == STARTED:  # only update if started and not finished!
            buttons = next_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(button, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(next_mouse):
                            gotValidClick = True
                            next_mouse.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
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
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for more_games (TrialHandler)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed num_games repeats of 'more_games'


# set up handler to look after randomisation of conditions etc
double_click_4 = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='double_click_4')
thisExp.addLoop(double_click_4)  # add the loop to the experiment
thisDouble_click_4 = double_click_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDouble_click_4.rgb)
if thisDouble_click_4 != None:
    for paramName in thisDouble_click_4:
        exec('{} = thisDouble_click_4[paramName]'.format(paramName))

for thisDouble_click_4 in double_click_4:
    currentLoop = double_click_4
    # abbreviate parameter names if possible (e.g. rgb = thisDouble_click_4.rgb)
    if thisDouble_click_4 != None:
        for paramName in thisDouble_click_4:
            exec('{} = thisDouble_click_4[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "section_4" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_4
    # generate shuffled list of who starts each game
    npc_starts = []
    for game in range(int(num_games/2)):
        npc_starts.append(True)
        npc_starts.append(False)
    random.shuffle(npc_starts)
    
    game = 0 # initialize game counter
    num_wins = 0 # initialize win counter
    visibility = 1 # pieces are visible for Section 3
    section = 4 # variable for experiment section
    move_duration = 1 # how long moves take
    end_pause_duration = 0.75 # game-end pause amt
    # setup some python lists for storing info about the mouse_4
    mouse_4.clicked_name = []
    gotValidClick = False  # until a click is received
    section_4_text.setText('In this last section you will be playing a game with new rules. Click the button below when you are ready to view the rules for the new game.')
    # keep track of which components have finished
    section_4Components = [title_4, button_4, button_4_text, mouse_4, section_4_text]
    for thisComponent in section_4Components:
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
    
    # --- Run Routine "section_4" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *title_4* updates
        
        # if title_4 is starting this frame...
        if title_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            title_4.frameNStart = frameN  # exact frame index
            title_4.tStart = t  # local t and not account for scr refresh
            title_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(title_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            title_4.status = STARTED
            title_4.setAutoDraw(True)
        
        # if title_4 is active this frame...
        if title_4.status == STARTED:
            # update params
            pass
        
        # *button_4* updates
        
        # if button_4 is starting this frame...
        if button_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_4.frameNStart = frameN  # exact frame index
            button_4.tStart = t  # local t and not account for scr refresh
            button_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            button_4.status = STARTED
            button_4.setAutoDraw(True)
        
        # if button_4 is active this frame...
        if button_4.status == STARTED:
            # update params
            pass
        
        # *button_4_text* updates
        
        # if button_4_text is starting this frame...
        if button_4_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_4_text.frameNStart = frameN  # exact frame index
            button_4_text.tStart = t  # local t and not account for scr refresh
            button_4_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_4_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            button_4_text.status = STARTED
            button_4_text.setAutoDraw(True)
        
        # if button_4_text is active this frame...
        if button_4_text.status == STARTED:
            # update params
            pass
        # *mouse_4* updates
        
        # if mouse_4 is starting this frame...
        if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_4.frameNStart = frameN  # exact frame index
            mouse_4.tStart = t  # local t and not account for scr refresh
            mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            mouse_4.status = STARTED
            mouse_4.mouseClock.reset()
            prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
        if mouse_4.status == STARTED:  # only update if started and not finished!
            buttons = mouse_4.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(button_4, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_4):
                            gotValidClick = True
                            mouse_4.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
        # *section_4_text* updates
        
        # if section_4_text is starting this frame...
        if section_4_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            section_4_text.frameNStart = frameN  # exact frame index
            section_4_text.tStart = t  # local t and not account for scr refresh
            section_4_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(section_4_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'section_4_text.started')
            # update status
            section_4_text.status = STARTED
            section_4_text.setAutoDraw(True)
        
        # if section_4_text is active this frame...
        if section_4_text.status == STARTED:
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
        for thisComponent in section_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "section_4" ---
    for thisComponent in section_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for double_click_4 (TrialHandler)
    # the Routine "section_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 2.0 repeats of 'double_click_4'


# set up handler to look after randomisation of conditions etc
new_games = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='new_games')
thisExp.addLoop(new_games)  # add the loop to the experiment
thisNew_game = new_games.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNew_game.rgb)
if thisNew_game != None:
    for paramName in thisNew_game:
        exec('{} = thisNew_game[paramName]'.format(paramName))

for thisNew_game in new_games:
    currentLoop = new_games
    # abbreviate parameter names if possible (e.g. rgb = thisNew_game.rgb)
    if thisNew_game != None:
        for paramName in thisNew_game:
            exec('{} = thisNew_game[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "countdown" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from countdown_code
    event.Mouse(visible=False)
    
    import random
    import math
    
    if section == 1 or section == 3 or section == 4:
        practice_turns.finished = False
    
    player_won = None
    npc_start = npc_starts[game]
    game = game + 1
    
    move_num = 0 # initialize move counter
    
    row = random.randint(0,14)
    col = random.randint(0,14)
    
    while row == col == 0:
        row = random.randint(0,14)
        col = random.randint(0,14)
    
    row_new = row
    col_new = col
    blue_piece.setOpacity(1 - npc_start)
    blue_piece.setPos(((col-7)/17, (15-row-8)/17))
    red_piece.setOpacity(npc_start)
    red_piece.setPos(((col-7)/17, (15-row-8)/17))
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
    turns_4 = data.TrialHandler(nReps=15.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='turns_4')
    thisExp.addLoop(turns_4)  # add the loop to the experiment
    thisTurn_4 = turns_4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTurn_4.rgb)
    if thisTurn_4 != None:
        for paramName in thisTurn_4:
            exec('{} = thisTurn_4[paramName]'.format(paramName))
    
    for thisTurn_4 in turns_4:
        currentLoop = turns_4
        # abbreviate parameter names if possible (e.g. rgb = thisTurn_4.rgb)
        if thisTurn_4 != None:
            for paramName in thisTurn_4:
                exec('{} = thisTurn_4[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "select_move" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        mouse.setPos(newPos=(0,0))
        event.Mouse(visible=True)
        
        if npc_start:
            continueRoutine = False
        
        timer = core.Clock()
        timer.reset()
        RT = 0
        
        row = row_new
        col = col_new
        
        mouse_still = True
        mouse_start = mouse.getPos()
        piece.setPos(((col-7)/17, (15-row-8)/17))
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
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
            # record mouse move onset time (RT)
            if mouse_still and any(mouse.getPos() != mouse_start):
                RT = timer.getTime()
                mouse_moved = True
            
            # on click, check for valid move selection
            if mouse.getPressed()[0] == 1:
                mouse_x, mouse_y = mouse.getPos()
                row_new = round(0 - ((mouse_y * 17) + 8 - 15))
                col_new = round((mouse_x * 17) + 7)
                if row_new <= row and col_new <= col:
                    if row_new >= 0 and col_new >= 0:
                        if row_new==row or col_new==col or (section != 4 and row-row_new == col-col_new):
                            if row_new != row or col_new != col:
                                if section != 4 or int(expInfo['session']) % 2 == 1 or euclid_move(move):
                                    continueRoutine = False
            
            # draw game board
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
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
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
        # Run 'End Routine' code from code
        if npc_start == False:
            move_num = move_num + 1
            df = df.append(pd.Series(dtype = 'object'), ignore_index = True)
            df.loc[len(df) - 1, 'session'] = expInfo['session']
            df.loc[len(df) - 1, 'section'] = section
            if section == 4 and int(expInfo['session']) % 2 == 0:
                df.loc[len(df) - 1, 'type'] = 'euc'
            if section == 4 and int(expInfo['session']) % 2 == 1:
                df.loc[len(df) - 1, 'type'] = 'nim'
            df.loc[len(df) - 1, 'game'] = game
            df.loc[len(df) - 1, 'move_num'] = move_num
            df.loc[len(df) - 1, 'player'] = 'human'
            df.loc[len(df) - 1, 'start_row'] = row
            df.loc[len(df) - 1, 'start_col'] = col
            df.loc[len(df) - 1, 'end_row'] = row_new
            df.loc[len(df) - 1, 'end_col'] = col_new
            df.loc[len(df) - 1, 'RT'] = RT
            df.loc[len(df) - 1, 'DT'] = timer.getTime()
            #print(df.to_string())
        # store data for turns_4 (TrialHandler)
        turns_4.addData('mouse.x', mouse.x)
        turns_4.addData('mouse.y', mouse.y)
        turns_4.addData('mouse.leftButton', mouse.leftButton)
        turns_4.addData('mouse.midButton', mouse.midButton)
        turns_4.addData('mouse.rightButton', mouse.rightButton)
        turns_4.addData('mouse.time', mouse.time)
        # the Routine "select_move" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "make_move" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from move_code
        event.Mouse(visible=False)
        
        #timer = core.Clock()
        #timer.reset()
        
        if npc_start or visibility == 0:
            npc_start = False
            continueRoutine = False
        moving_piece.setOpacity(visibility)
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
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from move_code
            for square in squares:
                square.draw()
            
            #if timer.getTime() > move_duration:
            #    continueRoutine = False
            
            # *moving_piece* updates
            
            # if moving_piece is starting this frame...
            if moving_piece.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                moving_piece.frameNStart = frameN  # exact frame index
                moving_piece.tStart = t  # local t and not account for scr refresh
                moving_piece.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(moving_piece, 'tStartRefresh')  # time at next scr refresh
                # update status
                moving_piece.status = STARTED
                moving_piece.setAutoDraw(True)
            
            # if moving_piece is active this frame...
            if moving_piece.status == STARTED:
                # update params
                moving_piece.setPos(((((1-min(move_duration,t)/move_duration)*col+min(move_duration,t)/move_duration*col_new)-7)/17, (15-((1-min(move_duration,t)/move_duration)*row+min(move_duration,t)/move_duration*row_new)-8)/17), log=False)
            
            # if moving_piece is stopping this frame...
            if moving_piece.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > moving_piece.tStartRefresh + move_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    moving_piece.tStop = t  # not accounting for scr refresh
                    moving_piece.frameNStop = frameN  # exact frame index
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
            if player_won == None:
                player_won = True
            num_wins = num_wins + 1
            practice_turns.finished = True
            if section == 1:
                turns.finished = True
            if section == 3:
                more_turns.finished = True
            if section == 4:
                turns_4.finished = True
            continueRoutine = False
        # the Routine "make_move" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "npc_wait" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from wait_code
        event.Mouse(visible=False)
        
        if practice_turns.finished:
            continueRoutine = False
        
        row = row_new
        col = col_new
        
        # select random opponent move
        moves = []
        Q_table = []
        
        if section != 4:
            optimal_moves = optimal_moves_wythoffs
        else:
            if int(expInfo['session']) % 2 == 0:
                optimal_moves = optimal_moves_euclid
            else:
                optimal_moves = optimal_moves_nim
        
        for r in range (row): # vertical moves
            move = (r, col)
            if section != 4 or int(expInfo['session']) % 2 == 1 or euclid_move(move):
                moves.append(move)
                if move in optimal_moves:
                    Q_table.append(1)
                else:
                    Q_table.append(0)
            
        for c in range (col): # horiz moves
            move = (row, c)
            if section != 4 or int(expInfo['session']) % 2 == 1 or euclid_move(move):
                moves.append(move)
                if move in optimal_moves:
                    Q_table.append(1)
                else:
                    Q_table.append(0)
            
        for d in range(1, min(row, col) + 1): # diag moves
            move = (row - d, col - d)
            if section != 4:
                moves.append(move)
                if move in optimal_moves:
                    Q_table.append(1)
                else:
                    Q_table.append(0)
        
        # action selection
        if len(moves) > 0:
            # calculate Boltzmann (softmax) action probs
            T = 0.55 # temperature parameter
            probs = np.exp(np.true_divide(Q_table,T))
            probs = np.true_divide(probs, sum(probs))
            action = np.random.choice(len(moves),p=probs)
            (row_new, col_new) = moves[action]
            # better to use np.random.Generator.choice
        npc.setPos(((col-7)/17, (15-row-8)/17))
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
        # Run 'End Routine' code from wait_code
        if practice_turns.finished == False:
            move_num = move_num + 1
            df = df.append(pd.Series(dtype = 'object'), ignore_index = True)
            df.loc[len(df) - 1, 'session'] = expInfo['session']
            df.loc[len(df) - 1, 'section'] = section
            df.loc[len(df) - 1, 'game'] = game
            df.loc[len(df) - 1, 'move_num'] = move_num
            df.loc[len(df) - 1, 'player'] = 'AI'
            df.loc[len(df) - 1, 'start_row'] = row
            df.loc[len(df) - 1, 'start_col'] = col
            df.loc[len(df) - 1, 'end_row'] = row_new
            df.loc[len(df) - 1, 'end_col'] = col_new
            df.loc[len(df) - 1, 'DT'] = 1.25
            #print(df.to_string())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.250000)
        
        # --- Prepare to start Routine "npc_move" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from npc_code
        event.Mouse(visible=False)
        
        #timer = core.Clock()
        #timer.reset()
        
        if practice_turns.finished or visibility == 0:
            continueRoutine = False
        moving_npc.setOpacity(visibility)
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
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from npc_code
            for square in squares:
                square.draw()
            
            #if timer.getTime() > move_duration:
            #    continueRoutine = False
            
            # *moving_npc* updates
            
            # if moving_npc is starting this frame...
            if moving_npc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                moving_npc.frameNStart = frameN  # exact frame index
                moving_npc.tStart = t  # local t and not account for scr refresh
                moving_npc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(moving_npc, 'tStartRefresh')  # time at next scr refresh
                # update status
                moving_npc.status = STARTED
                moving_npc.setAutoDraw(True)
            
            # if moving_npc is active this frame...
            if moving_npc.status == STARTED:
                # update params
                moving_npc.setPos(((((1-min(move_duration,t)/move_duration)*col+min(move_duration,t)/move_duration*col_new)-7)/17, (15-((1-min(move_duration,t)/move_duration)*row+min(move_duration,t)/move_duration*row_new)-8)/17), log=False)
            
            # if moving_npc is stopping this frame...
            if moving_npc.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > moving_npc.tStartRefresh + move_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    moving_npc.tStop = t  # not accounting for scr refresh
                    moving_npc.frameNStop = frameN  # exact frame index
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
            practice_turns.finished = True
            if section == 1:
                turns.finished = True
            if section == 3:
                more_turns.finished = True
            if section == 4:
                turns_4.finished = True
        # the Routine "npc_move" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 15.0 repeats of 'turns_4'
    
    
    # --- Prepare to start Routine "end_pause" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from end_code
    event.Mouse(visible=False)
    
    row = row_new
    col = col_new
    
    if visibility == 0:
        continueRoutine = False
    
    #print(df.to_string())
    end_blue.setOpacity(player_won)
    end_blue.setPos(((col-7)/17, (15-row-8)/17))
    end_red.setOpacity(1 - player_won)
    end_red.setPos(((col-7)/17, (15-row-8)/17))
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
    while continueRoutine:
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
            if tThisFlipGlobal > end_blue.tStartRefresh + end_pause_duration-frameTolerance:
                # keep track of stop time/frame for later
                end_blue.tStop = t  # not accounting for scr refresh
                end_blue.frameNStop = frameN  # exact frame index
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
            if tThisFlipGlobal > end_red.tStartRefresh + end_pause_duration-frameTolerance:
                # keep track of stop time/frame for later
                end_red.tStop = t  # not accounting for scr refresh
                end_red.frameNStop = frameN  # exact frame index
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
    # the Routine "end_pause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code
    event.Mouse(visible=True)
    
    if player_won:
        df.loc[(df.game==game) & (df.section==section), 'winner'] = 'human'
    else:
        df.loc[(df.game==game) & (df.section==section), 'winner'] = 'AI'
    feedback_win.setOpacity(player_won)
    feedback_lose.setOpacity(1 - player_won)
    status_text.setText('games played: ' + str(game) + ' of ' + str(num_games) + '\nwin percentage: ' + str(round (num_wins / game * 100)) + '%')
    # setup some python lists for storing info about the next_mouse
    next_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    feedbackComponents = [feedback_win, feedback_lose, status_text, button, button_text, next_mouse]
    for thisComponent in feedbackComponents:
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
    
    # --- Run Routine "feedback" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_win* updates
        
        # if feedback_win is starting this frame...
        if feedback_win.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_win.frameNStart = frameN  # exact frame index
            feedback_win.tStart = t  # local t and not account for scr refresh
            feedback_win.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_win, 'tStartRefresh')  # time at next scr refresh
            # update status
            feedback_win.status = STARTED
            feedback_win.setAutoDraw(True)
        
        # if feedback_win is active this frame...
        if feedback_win.status == STARTED:
            # update params
            pass
        
        # *feedback_lose* updates
        
        # if feedback_lose is starting this frame...
        if feedback_lose.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_lose.frameNStart = frameN  # exact frame index
            feedback_lose.tStart = t  # local t and not account for scr refresh
            feedback_lose.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_lose, 'tStartRefresh')  # time at next scr refresh
            # update status
            feedback_lose.status = STARTED
            feedback_lose.setAutoDraw(True)
        
        # if feedback_lose is active this frame...
        if feedback_lose.status == STARTED:
            # update params
            pass
        
        # *status_text* updates
        
        # if status_text is starting this frame...
        if status_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            status_text.frameNStart = frameN  # exact frame index
            status_text.tStart = t  # local t and not account for scr refresh
            status_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(status_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'status_text.started')
            # update status
            status_text.status = STARTED
            status_text.setAutoDraw(True)
        
        # if status_text is active this frame...
        if status_text.status == STARTED:
            # update params
            pass
        
        # *button* updates
        
        # if button is starting this frame...
        if button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button.frameNStart = frameN  # exact frame index
            button.tStart = t  # local t and not account for scr refresh
            button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
            # update status
            button.status = STARTED
            button.setAutoDraw(True)
        
        # if button is active this frame...
        if button.status == STARTED:
            # update params
            pass
        
        # *button_text* updates
        
        # if button_text is starting this frame...
        if button_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_text.frameNStart = frameN  # exact frame index
            button_text.tStart = t  # local t and not account for scr refresh
            button_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            button_text.status = STARTED
            button_text.setAutoDraw(True)
        
        # if button_text is active this frame...
        if button_text.status == STARTED:
            # update params
            pass
        # *next_mouse* updates
        
        # if next_mouse is starting this frame...
        if next_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next_mouse.frameNStart = frameN  # exact frame index
            next_mouse.tStart = t  # local t and not account for scr refresh
            next_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_mouse, 'tStartRefresh')  # time at next scr refresh
            # update status
            next_mouse.status = STARTED
            next_mouse.mouseClock.reset()
            prevButtonState = next_mouse.getPressed()  # if button is down already this ISN'T a new click
        if next_mouse.status == STARTED:  # only update if started and not finished!
            buttons = next_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(button, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(next_mouse):
                            gotValidClick = True
                            next_mouse.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
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
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for new_games (TrialHandler)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'new_games'


# --- Prepare to start Routine "end_screen" ---
continueRoutine = True
# update component parameters for each repeat
end_text.setText('You have now completed all sections of the experiment.\n\nPlease alert the experimenter that you are finished.\n\nThank you!\n')
# setup some python lists for storing info about the end_mouse
end_mouse.clicked_name = []
gotValidClick = False  # until a click is received
# Run 'Begin Routine' code from end_code_2
filepath = 'tidy_tables/' + expInfo['session'] + '_' + expInfo['participant'] + '.csv'

df.to_csv(filepath)

print(df.to_string())
# keep track of which components have finished
end_screenComponents = [end_title, end_button, end_button_text, end_text, end_mouse]
for thisComponent in end_screenComponents:
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

# --- Run Routine "end_screen" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_title* updates
    
    # if end_title is starting this frame...
    if end_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_title.frameNStart = frameN  # exact frame index
        end_title.tStart = t  # local t and not account for scr refresh
        end_title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_title, 'tStartRefresh')  # time at next scr refresh
        # update status
        end_title.status = STARTED
        end_title.setAutoDraw(True)
    
    # if end_title is active this frame...
    if end_title.status == STARTED:
        # update params
        pass
    
    # *end_button* updates
    
    # if end_button is starting this frame...
    if end_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_button.frameNStart = frameN  # exact frame index
        end_button.tStart = t  # local t and not account for scr refresh
        end_button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_button, 'tStartRefresh')  # time at next scr refresh
        # update status
        end_button.status = STARTED
        end_button.setAutoDraw(True)
    
    # if end_button is active this frame...
    if end_button.status == STARTED:
        # update params
        pass
    
    # *end_button_text* updates
    
    # if end_button_text is starting this frame...
    if end_button_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_button_text.frameNStart = frameN  # exact frame index
        end_button_text.tStart = t  # local t and not account for scr refresh
        end_button_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_button_text, 'tStartRefresh')  # time at next scr refresh
        # update status
        end_button_text.status = STARTED
        end_button_text.setAutoDraw(True)
    
    # if end_button_text is active this frame...
    if end_button_text.status == STARTED:
        # update params
        pass
    
    # *end_text* updates
    
    # if end_text is starting this frame...
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_text.started')
        # update status
        end_text.status = STARTED
        end_text.setAutoDraw(True)
    
    # if end_text is active this frame...
    if end_text.status == STARTED:
        # update params
        pass
    # *end_mouse* updates
    
    # if end_mouse is starting this frame...
    if end_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_mouse.frameNStart = frameN  # exact frame index
        end_mouse.tStart = t  # local t and not account for scr refresh
        end_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_mouse, 'tStartRefresh')  # time at next scr refresh
        # update status
        end_mouse.status = STARTED
        end_mouse.mouseClock.reset()
        prevButtonState = end_mouse.getPressed()  # if button is down already this ISN'T a new click
    if end_mouse.status == STARTED:  # only update if started and not finished!
        buttons = end_mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                clickableList = environmenttools.getFromNames(end_button, namespace=locals())
                for obj in clickableList:
                    # is this object clicked on?
                    if obj.contains(end_mouse):
                        gotValidClick = True
                        end_mouse.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # end routine on response
    
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
    for thisComponent in end_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end_screen" ---
for thisComponent in end_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "end_screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
