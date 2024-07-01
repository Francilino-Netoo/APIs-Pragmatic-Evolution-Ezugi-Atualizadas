import time 
import subprocess
while True:
    
    try:
        returned_value =subprocess.Popen(["./API_EVOLUTION"])
        returned_value.wait()

    except:
        time.sleep(3)
        print('oo')
        
        pass