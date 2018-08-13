'''

@author: v-chenyangchao-os
'''
from threading import Thread
import time
from com.ccycc.thread.AbsTractTask import AbsTractTask
from _ast import Try

class ExecuteThread(Thread):
    '''
    classdocs
    '''
    threadName = None
    run = True
    busy = False;
    taskList=None
    halt=False
    taskLock = None

    def __init__(self, taskList, taskLock):
        '''
        Constructor
        '''
        self.taskList = taskList
        self.taskLock = taskLock
        Thread.__init__(self)
        
    def run(self):
        threadName = '%s%s' %(self.getName(), '_IDLE')
        while(self.run):
          
            if(self.halt()):
                time.sleep(1)
                continue
          
            task=None
            try:
                
                self.taskLock.acquire()
                try:
                    if(len(self.taskList) > 0):
                        task=self.taskList.pop()
                finally:
                    self.taskLock.release()
                
                if(task is None):
                    time.sleep(1)
                    continue
                
                self.setName(task.getTaskName())
                self.busy=True
                task.execute()
            except Exception as e:
                print('&&& %s' % str(e))
                pass
            finally:
                self.busy=False
                self.setName(threadName)
              
    
    def isBusy(self):
        return self.busy
    
    def interrupt(self):
        self.run=False
    
    def halt(self):
        halt=True
    
    def go_on(self):
        halt=False