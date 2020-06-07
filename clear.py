import psutil
import os

def clean(mpid, id, cnt):
	for i in range(1,cnt+1):
		os.system('del T'+str(id)+'_'+str(i)+'.py')
	pids=psutil.pids()
	for tmp in pids:
		try:
			p =psutil.Process(tmp)
			if p.name() == 'python.exe' and str(tmp)!=mpid:
				os.system('taskkill /F /pid '+str(tmp))
		except psutil.NoSuchProcess:
			print("DONE")
