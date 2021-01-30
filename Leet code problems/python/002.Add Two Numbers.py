#my 1st attempt
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a,b=[],[]
        while True:
            a.append(l1.val)
            if l1.next==None:
                break
            l1=l1.next
        while True:
            b.append(l2.val)
            if l2.next==None:
                break
            l2=l2.next
        a.reverse()
        b.reverse()
        n1=""
        for i in a:
            n1=n1+str(i)
        n2=""
        for i in b:
            n2=n2+str(i)
        n3=int(n1)+int(n2)
        n3=str(n3)
        new=[]
        for i in n3:
            new.append(int(i))
        l3=ListNode(new[0])
        for i in new[1:]:
            l3=ListNode(i,l3)
        return l3
        
        
