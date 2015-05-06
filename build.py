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

class build():
	def __init__(self,cfg):
		if cfg.check_pass:
			self.pre(cfg)
			self.build(cfg)
			self.post(cfg)
		else:
			cfg.build_pass=False
		
	def pre(self,cfg):
		self.cwd=os.getcwd()
		os.chdir(cfg.mesa_path)
		
	def build(self,cfg):
		with open(cfg.build_log_file,'w') as f:
			with subprocess.Popen('./install', shell=True,
											stdout=subprocess.PIPE,stderr=subprocess.STDOUT, 
											bufsize=1, universal_newlines=True) as p:
				for line in p.stdout:
					if "exported" in line and not cfg.silent:
						print(line.replace('\n',''),file=cfg.silent_file)
					f.write(line)
		self._checkBuild(cfg)
		
	def post(self,cfg):
		os.chdir(self.cwd)
					
	def _checkBuild(self,cfg):
		#Lets just reparse the build log to find first failue
		cfg.build_pass=False
		with open(cfg.build_log_file,'r') as f:
			lines=f.readlines()
			for ind,line in enumerate(lines):
				if "Error:" in line:
					lineErr=lines[ind-4]
					cfg.build_file_err=lineErr.split(':')[0].split('/')[-1]
					break
			cfg.build_pass=True
		return
		