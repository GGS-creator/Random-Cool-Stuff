import printinfi
import gita 
import subprocess

if __name__=="__main__":
    result=subprocess.run(["python3","gita.py"], capture_output=True,text=True)
    output=result.stdout #this is used to print the output given by other program stdout
    
    printer=subprocess.run(["python3","printinfi.py"],capture_output=True,text=True,input=output)
    print(printer.stdout)
