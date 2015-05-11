#!/usr/bin/env python
#Note its this is both python2.7 and 3 compatible (other versions may work)

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
import inputCfg
import config
import checkout as c
import log as l
import build as b
import test as t

cfg=config.config()
inp=inputCfg.inputProcess(cfg)

#test suites to run
cfg.test_names=['0.001M_tau1_atm','15M_dynamo']
#cfg.version_list=["cabecd188bb18003ada7c9470d005ac007d1be2c","597e4d662bb9f56cc9f1005d00210293072b5066"]

#List of versions
cfg.version_list=["7518","7525"]
#Results
cfg.log_file='/home/rob/Desktop/mesaTest.log'
#Somewhere to build MESA
cfg.temp_fold='/media/data/mesa/temp/'

cfg.mesasdk_root='/media/data/mesa/sdk/mesasdk-20141212'
cfg.omp_num_threads='8'

#Ignore for now
cfg.vcs_mode='svn'
cfg.vcs_git_base_folder='/media/data/mesa/mesa/dev/'


for cfg.version in cfg.version_list:
	print("Running "+cfg.version)
	cfg.setDefaults()
	cfg.setPaths()
	log=l.logger(cfg)
	check=c.checkout(cfg)
	gb=b.build(cfg)
	tt=t.test(cfg)
	log.writeLog(cfg)
	cfg.cleanup()
	print("Done "+cfg.version)


