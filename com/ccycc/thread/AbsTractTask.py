'''

@author: v-chenyangchao-os
'''
import threading
from abc import ABCMeta, abstractmethod
class AbsTractTask(object):
    '''
    classdocs
    '''
    _metaclass_ = ABCMeta
    taskName = threading.current_thread().getName()

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    @abstractmethod
    def execute(self):pass
    
    def setTaskName(self, taskName=None):
        self.taskName=taskName
        
    def getTaskName(self):
        return self.taskName
        