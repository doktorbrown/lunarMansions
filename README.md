# lunarMansions
astronomical clock

This is a simple astronomical clock based on pyastro and astral libraries.  The Tkinter interface is continuing to evolve.


Updates Sep 28, 2019:
A bug related to daylight vs. nighttime was discovered with the equinox.  As a result, lunarMansions.py has been frozen as of the July 1, 2019.

The current working and modulized App.py is where the main display loop occurs.  Just be sure other python files are in the same directory.  "python App.py" will run things.

Visually, the center black circle was changed to white to quickly differentiate this version. 


Known Issues Sep 28, 2019:
Debugging with the logger.py file has been commented out while we troubleshoot the 00:00:00 updates of the PlanetaryHourDisplay layer.  The hours should change to the next day at this time but currently freezes while the planets revert to their -24h location.


