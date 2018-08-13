'''

@author: v-chenyangchao-os
'''
from com.ccycc.thread.ExecuteThread import ExecuteThread
from threading import Lock

class ExecuteThreadManager(object):
    '''
    classdocs
    '''

    threadList=[]
    taskList=[]
    MAX_THREAD_NUM = 5
    taskLock = Lock()

    def __init__(self, num=None):
        '''
        Constructor
        '''
        if(num is not None):
                self.MAX_THREAD_NUM=num;
                
    def executeTask(self, task=None):
        if(task is not None):
            
            self.taskLock.acquire()
            try:
                self.taskList.append(task)    
            finally:
                self.taskLock.release()
            
        
        if(len(self.taskList) > 0 and self.MAX_THREAD_NUM > len(self.threadList)):
            cet = ExecuteThread(self.taskList, self.taskLock);
            cet.start();
            self.threadList.append(cet)
            
    def taskIsFinish(self):
        if(len(self.taskList) > 0):
            return False;
        for thread in self.threadList:
            if(thread.isBusy()):
                return False
        return True
    
    def getTaskSize(self):
        return len(self.taskList)
    
    def getThreadSize(self):
        return len(self.threadList)
    
    def clear(self):
        for exe in self.threadList:
            exe.interrupt()
        self.threadList.clear()
        
    def halt(self):
        for exe in self.threadList:
            exe.halt()
            
    def go_on(self):
        for exe in self.threadList:
            exe.go_on()
    
        