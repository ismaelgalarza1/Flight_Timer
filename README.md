# Flight_Timer

- This timer is used to calculate the total flight hour that a UAS Operator conducted during their mission.

Language used: `Python`
GUI: `CustomTkinter`

# GUI
![MainGUI](/Assets/MainGui.png)

- The operator enters the `Date (12APR2025)` and `Launch time (1400)` as well as the date and time of landing.
- The Operator has the choice to include and use the date in the calculation. This can be used if the operator has flights lasting more than 24 hours.

# Convert to EXE
- In your terminal install auto-py-to-exe command `pip install auto-py-to-exe`
- Once complete, type the command `auto-py-to-exe`
- A GUI will appear see image below:

![Auto-py-to-exe](/Assets/Auto.png)

- Script Location - navigate to the `main.py` 
- OneFile - Seelect `One File`
- Console Window - Select `Windows Base (hide the console)`
- Select `CONVERT .PY TO .EXE` Button and stand by until it completed.
- In your project will be an `Output` folder where the `.exe` will be located.