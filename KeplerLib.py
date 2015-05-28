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
	 			'''
	 			if TargetFilekepler.endswith('.txt'):
	 				FileToread = open(TargetFilekepler)
			 		for line in FileToread.readlines():
			 			TempRead += line
			 	elif TargetFilekepler.endswith('.png'):
			 		TempRead = Image(filename=TargetFilekepler)
		 	except Exception, e:
		 		TempRead = "Cannot open output ". format(e)
		else:
			TempRead = "File not found!!"
		return TempRead
	def removeKeplerOutputFile(self,TargetFilekepler):
		if os.path.isfile(TargetFilekepler):
			os.remove(self.TargetFilekepler)
			
if __name__ == "__mian__":main()