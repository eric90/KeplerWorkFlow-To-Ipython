'''
Basic Command to run workflow with parameter and value from commandline:

./kepler.sh -runwf -nogui -NUM1 15 -redirectgui ~/Desktop ~/Desktop/addMod2.kar 

Switch to redirect any display output in the workflow to a DirPath: 

./kepler.sh -runwf -nogui -NUM1 15 -redirectgui ~/DirPath ~/Desktop/addMod2.kar 

This command will redirect any stdout due to the command execution to ~/Desktop/exe.txt and display the output of the workflow on console: 

./kepler.sh -runwf -nogui -NUM1 15 -redirectgui ~/Desktop ~/Desktop/addMod2.kar | tee > ~/Desktop/exe.txt ; cat ~/Desktop/addMod2.MonitorValue.txt
'''
import os, glob
from IPython.display import Image

class Kepler_Magic():
	def runKepler(self,Path_Kep,WorkFlowPath,FilePath,parameters):
		if os.path.isfile(str(Path_Kep)):		
			os.system(Path_Kep+' -runwf -nogui '+parameters+'-redirectgui '+FilePath+' '+WorkFlowPath)
 	
 	def readKeplerOutput(self,TargetFilekepler):
 		TempRead = ''
 		if  TargetFilekepler != '':
	 		try:
	 			'''
	 			for file in glob.glob(FilePath+ 'workflowname*'):
	 				if file ends with .kar:
	 					skip it
	 				do the rest and then retun
	 			'''
	 			if TargetFilekepler.endswith('.txt'):
	 				FileToread = open(TargetFilekepler)
			 		for line in FileToread.readlines():
			 			TempRead += line
			 	elif TargetFilekepler.endswith('.png'):
			 		#This is iPython class, do not use it outside
			 		TempRead = Image(filename=TargetFilekepler)
		 	except Exception, e:
		 		TempRead = "Cannot open output file(Did you setup your WorkFlowPath?)". format(e)
		else:
			TempRead = "File not found!!"
		return TempRead
	def removeKeplerOutputFile(self,TargetFilekepler):
		if os.path.isfile(TargetFilekepler):
			os.remove(self.TargetFilekepler)
			
if __name__ == "__mian__":main()