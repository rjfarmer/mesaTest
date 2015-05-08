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
import sys
import config
import argparse

class inputProcess():
	def __init__(self,cfg):
		self.setCmdLine(cfg)
	
	def loadCfgFile(self,cfg):
		pass
	
	def setCmdLine(self,cfg):
		parser = argparse.ArgumentParser(description='Downloads, builds and tests MESAstar')
		
		parser.add_argument("-v","--verbosity", help="Increase output verbosity", action="count")
		parser.add_argument("--verbosity-file",help="File to store verbose output (Default stdout)", nargs='?', type=argparse.FileType('w'),
									default=sys.stdout,metavar='')
		parser.add_argument("-t","--temp-fold",type=str, help="Folder in which to build MESA in",metavar='')
		parser.add_argument("-i",'--id',nargs='+', type=int,help='One or more MESA versions to test',metavar='')
		parser.add_argument("-m",'--mode',type=str,help='VCS mode git or svn (Default svn)',default='svn',metavar='')
		parser.add_argument('--git-folder',type=str,help='If VCS is git must set git folder location',metavar='')
		
		parser.add_argument('--tests',nargs='+',help='List of MESA test_suite folders to run',metavar='')
		parser.add_argument("-l",'--log-file', help='Log file output (Default mesaTest.log)',
									default='mesaTest.log', nargs='?', type=argparse.FileType('w'),metavar='')
		
		parser.add_argument('--mesasdk',type=str,help="MESASDK path",metavar='')
		parser.add_argument('--omp',type=int,help="OMP_NUM_THREADS",metavar='')
		
		parser.add_argument('-f','--config-file',type=str,help="Config file to read input parameters from, rather than from stdin",metavar='')
		self.cmdLineArgs = parser.parse_args()
