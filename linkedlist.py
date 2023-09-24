class node:
    def __init__(self,item):
        self.data= item
        self.next= None 
        
class linked_list:
    def __init__(self):
        self.head=None
        self.n=0    
    def prepend(self,item):
        new_node=node(item)
        new_node.next=self.head
        self.head=new_node
        self.n+=1
    def display(self):
        result=''
        current= self.head
        while current !=None:
           result=result+ str(current.data) +'->'
           current= current.next
        print( result[:-2]  )  
    def append(self,item):
        new_node=node(item)
        if self.head== None :
            self.head=new_node
            return
        current=self.head
        while current.next!=None:
            current= current.next
        current.next=new_node
        self.n+=1
    def append_middel(self,after,item):
        new_node=node(item)
        current=self.head
        while current!=None:
            if current.data==after:
                break
            current=current.next
        if current==None:
            return 'item not found'
        else :
            new_node.next=current.next
            current.next=new_node
            self.n+=1    
    def delet_head(self):
        if self.head == None:
            print('No elements in linked list')
            return
        self.head= self.head.next
        self.n-=1
    def delet_last(self):
        current= self.head
        if current== None:
            print("No elements in linkedlist")
            return 
        if current.next==None:
            self.head=None
            self.n -=1
            return 
        while current.next.next!=None:
            current=current.next
        current.next=None
        self.n -=1
    def delet(self,item):
        current= self.head
        if current==None:
            print('No elements in linkedlist')
            return
        if current.data==item:
            self.delet_head()
            return
        while current.next.next!=None:
            if current.next.data==item:
                break
            current=current.next
        if current.next.data==item:
            if current.next.next==None:
                self.pop()
                return
        if current.next.next==None:
            print('Item not found')
            return
        current.next=current.next.next
        self.n-=1
