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

def callapi(path,conn):
    # total_time=[]
    # for i in range(50):
        start_time= time.time()
        metric_file = Path(path)
        # Validating format of the file.
        # if path.lower().endswith(('.json')):
        #     # print("Correct file extenstion")
        # else:
        #     # print("Invalid file format. Use Json format file as input")
        #     return
        # if metric_file.is_file():
        #     # file exists
        #     # print("Input File exists")
        # else:
        #     print("Invalid File path")
        #     return
        
        
        with open(path) as f:
            data = json.load(f)
            

        url="https://ks8rfv4o5m.execute-api.us-east-1.amazonaws.com/api/quote"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'x-api-key':'vhDp1TmV543bZp3KMGymy8EWbXLxvz9y67WGGWgt'}
        # print("calling ECRP api")
        response = requests.post(url, data=json.dumps(data), headers=headers)
        # print('*******Results*******\n',json.dumps(response.json(),indent=4))
        # print('executed')
        # j = json.dumps(response.json(),indent=4)
        # path=path.replace("output","input")
        # with open(path, 'w') as f:
    
        #     f.write(j)
        elapsed_time = time.time() - start_time
        conn.send((elapsed_time))
        conn.close()
        # total_time.append(time.time()-start_time)
    # print("Average time taken:",sum(total_time)/len(total_time))

if __name__ == '__main__':

    #  fire.Fire(callapi)
    processes = []
    parent_connections= []
    t1=[]
    n = 10
    for i in range(n):
        parent_conn, child_conn = multiprocessing.Pipe()
        parent_connections.append(parent_conn)
        p = multiprocessing.Process(target = callapi('C:\\Users\\mmalli\\Desktop\\vscode\\ouput_jsons\\output_4sh_2B_1.json', child_conn))
        processes.append(p)
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    for parent_connection in parent_connections:
        t1.append(parent_connection.recv())
    print(t1)
    
    print("average time taken for {} requests: {}".format(n,sum(t1)/len(t1)))

