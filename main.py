# python3

class Query:
    const = 263
    remainder = 1000003
    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.buckets = [[] for _ in range(bucket_count)]
            
    def hash_function(self,string):
        hashCodeResult = 0 
        for count in reversed(string):
            hashCodeResult = (hashCodeResult * self.const + ord(count)) % self.remainder
        return hashCodeResult

    def addCaller(self, phoneNumber, phoneCallerName):
        hashCode = self.hash_function(phoneNumber)
        bucket = self.buckets[hashCode]
        if phoneNumber not in bucket:
            self.buckets[hashCode] = [phoneNumber]+[phoneCallerName]+ bucket
        else:
            for i in range(0,len(bucket)-1,2):
                if bucket[i] == phoneNumber:
                    bucket[i+1] == phoneCallerName
        
    def deleteCaller(self, phoneNumber):    
        hashCode = self.hash_function(phoneNumber)
        bucket = self.buckets[hashCode]
        for i in range(len(bucket)):
            if bucket[i] == phoneNumber:
                bucket.pop(i)
                bucket.pop(i)                
                break

    def findCaller(self, phoneNumber):
        hashCode = self.hash_function(phoneNumber)
        bucket = self.buckets[hashCode]
        for i in range(0,len(bucket)-1,2):
            if bucket[i] == phoneNumber:
                return bucket[i + 1]
            return "not found"
    
def read_queries():
    countOfContacts = int(input())
    return [Query(input().split()) for i in range(countOfContacts)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    for cur_query in queries:
        commandArray = list(cur_query.split())
        if commandArray[0] == 'add':
           contacts.addCaller(commandArray[1],commandArray[2])           
        elif commandArray[0]  == 'del':
           contacts.deleteCaller(commandArray[1])           
        elif commandArray[0] == 'find':         
            result.append(contacts.findCaller(commandArray[1]))
    return result

if __name__ == '__main__':
    countOfContacts = int(input())
    contacts = Query(countOfContacts)
    write_responses(process_queries([input() for i in range(countOfContacts)]))

