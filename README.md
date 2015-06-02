# KeplerWorkFlow-To-Ipython
SDSC project

This project will print the workflow of kepler on the ipython notebook. 

#Instruction 
* Mac users have Python. For Windows users they have to install python on their machine. 
* Install [Kepler] (https://kepler-project.org/) 
* 1- clone this repository.
* 2- from terminal run: python setup.py install
   This will compile the python magic function

#What to do inside the Iphyton notebook

* First you need to import the function: import KeplerFunc
* You need to give the path of Kepler application: %KepPath (kepler.h path)  
* Type the workFlow Path: %WorkFlow (Work flow path)
* To run and generate the workflow:  %runTheKepler 
* Last to printout the workflow on the screen: %printWork  (workflow name)
