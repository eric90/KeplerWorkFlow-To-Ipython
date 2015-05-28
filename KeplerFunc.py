
import os
import argparse
from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic) 
from KeplerLib import Kepler_Magic

@magics_class
class MainKepler(Magics):
	Path_Kep     = ''
	WorkFlowPath   = ''
	FilePath = ''
	wk =  Kepler_Magic()
	"""
	@line_magic
	def Kepler2(self,line):
		print(line)
		parser = argparse.ArgumentParser()
		parser.add_argument('-a','--add',type = int,default=10, help="creates a loval lin acc")
		args = parser.parse_args(line)
		print(args)
	"""
	"""
	def fib(n):
		a, b = 0, 1
		for i in range(n):
			a, b = b,a+b 
		return a
	def Main():

		parser = argparse.ArgumentParser()
		parser.add_argument("num", help="the fibo num" + " you wish to calc", type= int )

		args = parser.parse_args()
		result = fib(args.num)
		print "the " + str(args.num)+ " the fib is " + str(result)

	if __name__ == '__main__':
		Main()
	"""


	@line_magic
	def runTheKepler(self,line):
		if self.Path_Kep =='':
			if os.path.isfile('kppath.txt'):
				fh = open('kppath.txt','r')
				self.Path_Kep  = fh.readline()
		
		paramHolder = str(line)
		
		if os.path.isfile(self.WorkFlowPath):
			if os.path.isfile(self.Path_Kep):
				self.wk.runKepler(self.Path_Kep,self.WorkFlowPath,self.FilePath, paramHolder)
			else:
				return "Specify Kepler path "
		else:
			return "Specify workflow path "
	
	@line_magic
	def printWork(self,line):
		result = self.wk.readKeplerOutput(self.FilePath+'/'+line)
		if line.endswith('.png'):
			return result
		else:
			print result
		
	@line_magic
	def KepPath(self,line):
		if line :
			try:
				fh =  open('kppath.txt','w+')
				fh.truncate()
				fh.write(line)
				fh.close()
			except IOError as e:
				Error =  "You can not open This kepler file!"
			self.Path_Kep = line

	@line_magic
	def WorkFlow(self,line):	
		if line:
			if self.FilePath == '':
				self.FilePath =  os.path.dirname(os.path.realpath(line))
			self.WorkFlowPath = line

	@line_magic
	def TgConf(self,line):
		if line:
			self.FilePath = line

ip = get_ipython()
ip.register_magics(MainKepler)

