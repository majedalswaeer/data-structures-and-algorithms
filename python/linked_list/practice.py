class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node

    def includes(self,data):
        cur=self.head
        while cur:
            if cur.value==data:
                return True
            cur=cur.next
        return False

    def append(self,new_value):
        new_node=Node(new_value)
        cur=self.head
        while cur:
            if cur.next==None:
                cur.next=new_node
                break
            cur=cur.next
    def insert_before(self,s_value,n_value):
        cur=self.head

        while cur:
            if cur.next.value==s_value:
                new=Node(n_value)
                temp=cur.next
                cur.next=new
                new.next=temp
                break
            cur=cur.next
    def insert_after(self,s_value,n_value):
        cur=self.head

        while cur:
            if cur.value==s_value:
                new=Node(n_value)
                temp=cur.next
                cur.next=new
                new.next=temp
                break
            cur=cur.next

    def kfromend(self,k):
        cur=self.head
        c=0
        while cur:
            c+=1
            cur=cur.next
        cur=self.head

        diff=c-k
        for i in range(c):
            print(i)
            if i == diff:
                return cur.value
            cur = cur.next


    def __str__(self):
        li = []
        cur = self.head
        while cur!=None:
            li= li + [(f"{ { cur.value } }").replace("'", " ")]
            cur=cur.next
        return ' -> '.join(li + ["NULL"])

    def reverse(self):
            prev=None
            cur=self.head
            while(cur is not None):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            self.head = prev

def linked_list_zip(list1,list2):
    new_list = LinkedList()

    cur1 = list1.head
    cur2 = list2.head
    new_list.insert(cur1.value)
    cur1 = cur1.next
    while cur2:
            new_list.append(cur2.value)
            cur2= cur2.next
    while cur1:
        new_list.append(cur1.value)
        cur1 = cur1.next

    if not (cur2 or cur1):
        return new_list


if __name__ =='__main__':
    l=LinkedList()
    l.insert(1)
    l.insert(2)
    l.append('wh')
    l.insert_after(1,'majed')
    l.insert('ww')
    l2=LinkedList()
    l2.insert('ee')
    l2.insert('pp')
    l.reverse()

    print(str(l))

