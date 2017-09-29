# http://learn.codingdojo.com/m/7/3187/32645

class Call(object):
    def __init__(self,call_id,call_name,call_number,call_time,call_reason):
        self.call = {
            "call_id": call_id,
            "call_name": call_name,
            "call_number": call_number,
            "call_time": call_time,
            "call_reason": call_reason
        }
    def display(self):
        print self.call

class CallCenter(Call):
    def __init__(self):
        self.calls = []
        self.queue_size = 0
    def add(self,call_id,call_name,call_number,call_time,call_reason):
        super(CallCenter,self).__init__(call_id,call_name,call_number,call_time,call_reason)
        self.calls.append(self.call)
        # print self.calls
        self.queue_size += 1
        return self
    def remove(self):
        self.calls.pop(0)
        self.queue_size -= 1
        return self
    def info(self):
        for i in self.calls:
            print i[1], i[2]
        print "Queue size: ", self.queue_size
    def removePhone(self,phone_number):
        for i in range(self.queue_size-1):
            # print self.calls[i]["call_number"]
            if self.calls[i]["call_number"] == phone_number:
                self.calls.pop(i)
                self.queue_size -= 1
                i -= 1
        return self
    def sortQueue(self):
        # self.calls = sorted(self.calls, key=lambda x:x[3])
        print self.calls
        return self

callcenter = CallCenter()
callcenter.add(1,"Hieu","555-555-5555","05:56","Clouds looks ominous")
callcenter.add(2,"Cotton Eye Joe","111-111-1111","02:57","Got attacked by a bride")
callcenter.add(3,"John","888-888-8888","12:57","Does not have enough money for Uber")
callcenter.add(4,"Ein","222-222-2222","01:57","Wants a new chew toy")
callcenter.add(5,"Angela","444-444-4444","10:57","Boyfriend refuses to stop playing Call of Duty")
callcenter.sortQueue().removePhone("222-222-2222")