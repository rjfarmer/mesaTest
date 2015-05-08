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
import shutil
import sys

class config():
	def __init__(self):
		#Build
		self.temp_fold=''
		self.build_fold=''
		self.version=''
		self.version_list=[]
		self.mesa_version=''
		
		self.build_pass=False
		self.build_log_file=''
		self.build_file_err='"N/A"'
		
		#MESA
		self.mesa_path=''
		self.mesassdk_path=''
		self.omp_num_threads=0
		self.svn_version=-1
		
		
		#Checkout
		self.vcs_mode='svn'
		#Git
		self.vcs_git_base_folder=''
		#svn
		self.vcs_svn_url='svn://svn.code.sf.net/p/mesa/code/trunk'
		self.check_pass=False
		
		self.prefix_build_fold='mesa-test-'
		
		#Test
		self.test_names=[]
		self.test_res=[]
		self.test_rerun=5
		
		#Logging
		self.log_file=''
		
		#Utils
		self.silent=True
		if self.silent:
			self.silent_file=open(os.devnull, 'wb')
		else:
			#self.silent_file=open("mesaTest.stderr", 'wb')
			self.silent_file=sys.stdout
		self.debug=False
	
	def setPaths(self):
		self.build_fold=os.path.join(self.temp_fold,self.prefix_build_fold+self.version)
		self.build_log_file=os.path.join(self.build_fold,'build.log')
		
		self.mesa_path=self.build_fold
		os.environ['MESA_PATH']=self.mesa_path
		os.environ['MESASDK_ROOT']=self.mesasdk_root
		os.environ['OMP_NUM_THREADS']=self.omp_num_threads
		#Skip source the mesasdk and just set the path varaible its the only thing we need
		os.environ['PATH']=os.path.join(self.mesasdk_root,'bin:')+os.getenv("PATH")
		os.environ['PGPLOT_DIR']=os.path.join(self.mesasdk_root,'pgplot')
		
	def getVersion(self):
		self.mesa_version=-1
		version_path=os.path.join(self.mesa_path,'data','version_number')
		try:
			with open(version_path,'r') as f:
				mesa_version=f.readline()
				if len(mesa_version)>0:
					self.mesa_version=int(mesa_version)
		except IOError:
			raise ValueError("Cant read "+version_path)
		
	def cleanup(self):
		shutil.rmtree(self.build_fold,ignore_errors=True)
		
	def runComNull(self,command):
		with open(os.devnull, 'w') as devnull:
			p=subprocess.call(command, shell=True,stdout=self.silent_file,stderr=self.silent_file)
		if p is not 0:
			return False
		return True
		
	def setDefaults(self):
		#Build
		self.build_fold=''
		self.mesa_version=''
		self.build_pass=False
		self.build_file_err='"N/A"'
		self.mesa_path=''
		self.check_pass=False
		self.test_res=[]
