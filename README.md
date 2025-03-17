# Jacob's Capstone Project

## Classes
- **alg.py** - File with all the calculations for surface area  
- **test_arm.py** - Class to control servo camera mount  
- **test_screen.py** - Class to control messages and button responses of LCD screen  
- **camera.py** - Class to link Py-cam and take/save photos  

## How to Run:
Do the following in the terminal:

```bash
cd  # Go to home directory
source env2/bin/activate  # Activate virtual env 
cd Capstone  # Go to dir with capstone files outlined above
python3 test_screen.py  # Run main program
```

Incase the virtual env gets deleated 
```bash
python3 -m venv --system-site-packages env2  # Create new virtual env
source env2/bin/activate  # Activate virtual env 
cd Capstone  # Go to dir with capstone files outlined above
pip3 install -r requirements.txt  # Install all necessary libraries
```