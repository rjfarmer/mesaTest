#Copyright (c) 2015, Robert Farmer rjfarmer@asu.edu

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


from __future__ import print_function
import os
import subprocess
import time

class test():
	def __init__(self,cfg):
		if cfg.build_pass:
			cfg.testsuite=os.path.join(cfg.build_fold,'star','test_suite')
			for i in cfg.test_names:
				cfg.curr_test=i
				self.pre(cfg)
				self.test(cfg)
				self.post(cfg)
		else:
			for i in cfg.test_names:
				cfg.curr_test=i
				cfg.test_res.append([cfg.curr_test,False,-1])
			
		
	def pre(self,cfg):
		self.cwd= os.getcwd()
		os.chdir(os.path.join(cfg.testsuite,cfg.curr_test))
	
	def test(self,cfg):
		self._buildTest(cfg)
		self._runTest(cfg)
	
	def post(self,cfg):
		cfg.test_res.append([cfg.curr_test,self.run,self.time])
		os.chdir(self.cwd)
		
	def _buildTest(self,cfg):
		self.build=cfg.runComNull('./mk')
		
	def _runTest(self,cfg):
		start=time.time()
		retCode=cfg.runComNull('./rn')
		end=time.time()
		self.run=retCode
		if retCode:
			self.time=end-start
		else:
			self.time=-1
		
	def checktest(self,cfg):
		pass
