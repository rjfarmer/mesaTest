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


import os
import subprocess

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
		
		
		#Checkout
		self.vcs_mode='svn'
		#Git
		self.vcs_git_base_folder=''
		#svn
		self.vcs_svn_url=''
		self.check_pass=False
		
		#Test
		self.test_names=[]
		self.test_res=[]
		
		#Logging
		self.log_file=''
		
		#Utils
		self.silent=True
		self.silent_file=open('log.txt', 'wb')
		#self.silent_file=open(os.devnull, 'wb')
	
	def setPaths(self):
		self.build_fold=os.path.join(self.temp_fold,'mesa-test-'+self.version)
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
					selmesa_version=int(mesa_version)
		except IOError:
			raise ValueError("Cant read "+version_path)
		
	def cleanup(self):
		os.rmdir(self.build_fold)
		
	def runComNull(self,command):
		with open(os.devnull, 'w') as devnull:
			p=subprocess.call(command, shell=True,stdout=self.silent_file,stderr=self.silent_file)
		if p is not 0:
			return False
		return True