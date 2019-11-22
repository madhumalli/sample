#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:18:00 2019

@author: ckotadiya
"""
import requests
from pathlib import Path
import fire
import json
import time
import multiprocessing

def callapi(path):
    # total_time=[]
    # for i in range(50):
        start_time= time.time()
        metric_file = Path(path)
        # Validating format of the file.
        if path.lower().endswith(('.json')):
            print("Correct file extenstion")
        else:
            print("Invalid file format. Use Json format file as input")
            return
        if metric_file.is_file():
            # file exists
            print("Input File exists")
        else:
            print("Invalid File path")
            return
        
        
        with open(path) as f:
            data = json.load(f)
            

        url="https://ks8rfv4o5m.execute-api.us-east-1.amazonaws.com/api/quote"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'x-api-key':'vhDp1TmV543bZp3KMGymy8EWbXLxvz9y67WGGWgt'}
        print("calling ECRP api")
        response = requests.post(url, data=json.dumps(data), headers=headers)
        print('*******Results*******\n',json.dumps(response.json(),indent=4))
        # print('\nElapsed Time', time.time()-start_time)
        j = json.dumps(response.json(),indent=4)
        path=path.replace("input","output")
        with open("C:\\Users\\mmalli\\Desktop\\vscode\\ouput_jsons\\output_json\\"+path, 'w') as f:
            f.write(j)
        
        elapsed_time = time.time()-start_time
        return elapsed_time,path
        # total_time.append(time.time()-start_time)
    # print("Average time taken:",sum(total_time)/len(total_time))

if __name__ == '__main__':
    
    fire.Fire(callapi)
    # for i in range(2):
    #     p = multiprocessing.Process(target = callapi)
    #     p.start()
    #     p.join()