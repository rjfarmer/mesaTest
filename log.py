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

class logger():
	def __init__(self,cfg):		
		#Does log file exist?
		try:
			#Yes then get last version
			with open(cfg.log_file,'r') as f:
				f.close
			cfg.last_version=self.getLastVersion(cfg)
		except IOError:
			#No, make new file and add header
			self.writeLogHeader(cfg)
			cfg.last_version=-1
		
	def writeLog(self,cfg):
		with open(cfg.log_file,'a') as f:
			print(cfg.version,cfg.check_pass,cfg.build_pass,cfg.build_file_err,end=' ',file=f)
			outStr=''
			for i in cfg.test_names:
				for j in cfg.test_res:
					if i==j[0]:
						outStr+=str(j[1])+' '+str(round(j[2],3))+' '
			print(outStr,file=f)
	
	def writeLogHeader(self,cfg):
		with open(cfg.log_file,'w') as f:
			print('#version checkout_pass build_pass build_error '+' '.join([str(x)+' '+str(x)+"_time" for x in cfg.test_names]),file=f)
			
	def getLastVersion(self,cfg):
		v=-1
		try:
			with open(cfg.log_file,'r') as f:
				for line in f:
					continue
				v=line.split(' ')[0]
				if '#' in v or len(v)==0:
					v=-1
		except:
			v=-1

		