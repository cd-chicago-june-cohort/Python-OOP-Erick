class Call(object):
    def __init__(self, id, callerName, callerNum, timeOfCall, reasonOfCall):
        self.id = id
        self.callerName = callerName
        self.callerNum = callerNum
        self.timeOfCall = timeOfCall
        self.reasonOfCall = reasonOfCall
    def display_call(self):
        print('\nCall Information')
        print('Unique ID: ' + str(self.id))
        print('Caller Name: ' + self.callerName)
        print('Phone Number: ' + str(self.callerNum))
        print('Time Of Call: ' + self.timeOfCall)
        print('Reason For Call: ' + self.reasonOfCall + '\n')

class CallCenter(object):
    def __init__(self, callObjects):
        self.callObjects = callObjects
        self.queue = len(callObjects)
    def add(self, call):
        self.callObjects.append(call)
        self.queue += 1
    def remove(self):
        del self.callObjects[0] 
        return self
    def removeByNumber(self, num):
        for i in self.callObjects:
            if(i.callerNum == num):
                self.callObjects.remove(i)
                self.queue -= 1
        return self
    def display_call(self):
        for i in self.callObjects:
            print('Name of caller: ' + i.callerName + ' | Phone Numner: ' + str(i.callerNum) + ' | Lenght of queue ' + str(self.queue))
            print('*') * 75

call1 = Call(1, 'Erick', 7736291914, '7:45', 'Tech Support')
call2 = Call(3, 'Tania', 7736648939, '8:30', 'Customer Service')
call3 = Call(4, 'Picasso', 7735124192, '4:50', 'Help Desk')
listOfCallers = [call1, call2]

caller = CallCenter(listOfCallers)
caller.add(call3)
caller.remove()
caller.display_call()
caller.removeByNumber(7735124192)
caller.display_call()