import cli as cl
import os, json
import pandas as pd

path_to_json = './'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
print(json_files)
time=[]
filenmae=[]
opfilenmae=[]
for i in json_files:
    #print(i)
    elapsedTime,path=cl.callapi(i)

    time.append(elapsedTime)
    filenmae.append(i)
    opfilenmae.append(path)
data = {'FileName':filenmae, 'Time':time, 'opfilenmae':opfilenmae} 
  
# Create DataFrame 
df = pd.DataFrame(data) 
  
# Print the output. 
print(df) 