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

class checkout():
	def __init__(self,cfg):
		
		if cfg.vcs_mode=='git':
			vcs=git(cfg)
		else:
			vcs=svn(cfg)
			
		try:
			vcs.pre(cfg)
			vcs.checkout(cfg)
			vcs.post(cfg)
		except:
			cfg.check_pass=False
	
class git():
	def __init__(self,cfg):
		pass
		
	def pre(self,cfg):
		self.cwd= os.getcwd()
		os.chdir(cfg.temp_fold)
		
	def checkout(self,cfg):
		p=subprocess.call('git clone '+cfg.vcs_git_base_folder+' '+cfg.build_fold,shell=True,
							stdout=cfg.silent_file,stderr=cfg.silent_file)
		#Check folder was made
		if os.path.isdir(cfg.build_fold) and p==0:
			cwd= os.getcwd()
			os.chdir(cfg.build_fold)
			p2=subprocess.call('git checkout '+str(cfg.version),shell=True,
								stdout=cfg.silent_file,stderr=cfg.silent_file)
			if p2==0:
				cfg.check_pass=True
			os.chdir(cwd)
		
	def post(self,cfg):
		os.chdir(self.cwd)

		
class svn():
	def __init__(self):
		pass
	
	def pre(self):
		pass

	def checkout(self):
		pass
	
	def post(self):
		pass