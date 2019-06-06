#! /bin/env python

import os, shutil, subprocess

Reference_dirs = ["WkkToRWToTri_conf"]
for Reference_dir in Reference_dirs:
	prefixington = Reference_dir.replace('_conf','')

	FinalStates = ["ZA","WW"]
	Masses = [[1500,[100,180,200,300]],[2000,[100,180,200,300]],[2500,[100,180,200,300]],[3000,[100,180,200,300]],[3500,[100,180,200,300]],[4000,[100,180,200,300]],[4500,[100,180,200,300]],[5000,[100,180,200,300]]]



	for state in FinalStates:
		for wkkmass in Masses:
			for rmass in wkkmass[1]:
							
							sampleName = prefixington+'_Wkk'+str(wkkmass[0])+'R'+str(rmass)+'_'+state
							print sampleName
							#remove dir if already exists and create
							if os.path.isdir(sampleName):
								shutil.rmtree(sampleName)
							os.makedirs(sampleName)
							# Copy cards
							shutil.copyfile(Reference_dir+'/'+'run_card.dat',sampleName+'/'+sampleName+'_run_card.dat')
							shutil.copyfile(Reference_dir+'/'+state+'_madspin_card.dat',sampleName+'/'+sampleName+'_madspin_card.dat')
							shutil.copyfile(Reference_dir+'/'+state+'_proc_card.dat',sampleName+'/'+sampleName+'_proc_card.dat')
							shutil.copyfile(Reference_dir+'/'+state+'_customizecards.dat',sampleName+'/'+sampleName+'_customizecards.dat')
							shutil.copyfile(Reference_dir+'/extramodels.dat',sampleName+'/'+sampleName+'_extramodels.dat')
							#customization
							with open("{0}/{0}_proc_card.dat".format(sampleName), "a") as f:
								f.write("output "+sampleName)
							with open("{0}/{0}_customizecards.dat".format(sampleName), "a") as f:
								f.write("set param_card MASS 9000025 %e\n" % rmass)
								f.write("set param_card KKINPUTS 5 %e\n" % wkkmass[0])
								
