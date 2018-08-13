'''
@author: v-chenyangchao-os
'''
from com.ccycc.thread.ExecuteThreadManager import ExecuteThreadManager
from com.ccycc.thread.TestTask import TestTask
from time import sleep
etm = ExecuteThreadManager()

i=0
while(i<100):
    i+=1
    tt=TestTask()
    etm.executeTask(tt)
    sleep(0.1)

while (not etm.taskIsFinish()):
    continue
print('---finish---')

etm.clear()