# This class works as a container, we can say as it' an modified dict
class TagCloud:
    def __init__(self) -> None:
        self.tags = {}

    def __str__(self):
        pass
    
    def add(self,tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(),0) + 1
    
    def __getitem__(self,tag): # what to retrun when we use this expression: -access object as accessing dict - object ['key'] 
        return self.tags.get(tag,0)
    
    def __setitem__(self,tag,count): # what to retrun when we use object ['key'] = 
        self.tags[tag.lower()] = count

    def __len__(self):                # what to return when we apply len on the object
        return len(self.tags)
    

    def __iter__(self):                # we determine what to iterate when we iterate on the object
        return iter(self.tags)


cloud = TagCloud()

print(cloud['python'])      # get number of items

cloud['java'] = 3           # add item with the value we need

print(len(cloud))           # when i apply the len on the object return the len of the dict

for i in cloud:             #iterate over the object
    print(i)

print(cloud.__dict__['tags']['java']) #we use dict to list all the properities inside the class and therfore access them, even if it was a private attribute
