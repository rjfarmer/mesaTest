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

from __future__ import print_function,unicode_literals
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
			if not cfg.debug:
				raise
			cfg.check_pass=False
	
class git():
	def __init__(self,cfg):
		pass
		
	def pre(self,cfg):
		self.cwd= os.getcwd()
		os.chdir(cfg.temp_fold)
		#Get SVN version id
		cfg.svn_version=self._getSVNByHash(cfg,cfg.version)
		
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

	def _getSVNByHash(self,cfg,gitHash):
		x=subprocess.check_output('git --work-tree '+cfg.vcs_git_base_folder
											+' --git-dir '+os.path.join(cfg.vcs_git_base_folder,'.git')+
											' show -s --format=%B '+str(gitHash),shell=True,executable="/bin/bash")
		return int(x.decode().split(' ')[-2].split('@')[-1])
		
	def _getAllHashs(self,cfg):
		cfg.git_hash_all=subprocess.check_output('git --work-tree '+cfg.vcs_git_base_folder
											+' --git-dir '+os.path.join(cfg.vcs_git_base_folder,'.git')+
											' log --pretty=format:"%H" git-svn',shell=True,executable="/bin/bash")
		cfg.git_hash_all=cfg.git_hash_all.decode().split('\n')
		#Invert list as oldest commit is last in list
		cfg.git_hash_all=cfg.git_hash[::-1]
		
	#def _getHashBySVN(self,svn_version):
		#for i, elem in enumerate(svn_version):
				#if svn_version == elem:
					#return cfg.git_hash_all[i]
					
	#def _getAllSVNs(self,cfg):
		#version=[]
		#for i in cfg.git_hash_all:
			#version.append(self._getSVNByHash(i))
		#cfg.svn_version_all=version
		
class svn():
	def __init__(self,cfg):
		pass
	
	def pre(self,cfg):
		self.cwd= os.getcwd()
		os.chdir(cfg.temp_fold)
		cfg.svn_version=cfg.version

	def checkout(self,cfg):
		p=subprocess.call('svn co -r '+cfg.version+' '+cfg.vcs_svn_url+' '+cfg.build_fold,
								shell=True,stdout=cfg.silent_file,stderr=cfg.silent_file,executable="/bin/bash")
		if os.path.isdir(cfg.build_fold) and p==0:
			cfg.check_pass=True
	
	def post(self,cfg):
		os.chdir(self.cwd)

		
	def getLatestVersion(self,cfg):
		p=subprocess.check_output('svn info '+cfg.vcs_svn_url+' -r HEAD',shell=True,stderr=cfg.silent_file,executable="/bin/bash")
		pl=p.decode().split()
		ind=pl.index('Revision:')
		return pl[ind+1]
		
			
		
		
		