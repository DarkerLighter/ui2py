# ui2py
Containning ui2py script


Make sure you imported the right liberaries.

The script should do the following when you run it:
-Open file explorer
-Convert .ui to .py 
(Creates additional file with same name and location but different extention when converted!)

Might need to pip install in cmd(if using venv/PyCharm) the correct liberaries



as for Fullscreen MainWindow, add these:(works on QtDesigner converted files from .ui to .py)
MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint) # Set window to fullscreen
MainWindow.showMaximized()                              # Set Window to fullscreen


Hi Saaed.
