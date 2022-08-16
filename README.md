# niceGUI
GUI for checking codes obtained during school games

# Description
`OrsiGame.py` is a python script to create a Graphical User Interface (GUI) using tkinter. 

The goal of the GUI is to allow students to check codes obtained during an outreach activity.

It is organised in two levels:
  1) **top level**: GUI to choose your team (group A, B or C)
  2) **child levels**: GUI to control your codes (three codes per team, each obtained with a different game)
  
 
# How to use it

Create a conda env with python v3.9.13 with tkinter installed, and activate it.
``` 
conda env create -f env/env_GUI.yml 
conda activate GUI
```

Run python script
``` 
python OrsiGame.py
```

The GUI will run till the user closes the window of the top level.



  
  
