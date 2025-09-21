"""
File: new_head.py
Name: wei chen
------------------------
將大於x的數字依原本ListNode的順序，往後移。
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def new_head(head: ListNode, x: int) -> ListNode:
    #######################
    cur = head
    large_lst = []  # 裝大於x的data
    low_lst = []  # 裝小於x的data
    while cur:
        if cur.val < x:
            low_lst.append(cur.val)
        else:
            large_lst.append(cur.val)
        cur = cur.next
    dummy = ListNode()  # TA: 要創造一個新的鏈，只用另一個變數head2 = head，還是同一個記憶體位址
    cur = dummy
    for num in low_lst:  # 先鏈小於x的data
        cur.next = ListNode(data=num)
        cur = cur.next
    for num in large_lst:  # 再鏈大於x的data
        cur.next = ListNode(data=num)
        cur = cur.next
    #######################
    return dummy.next

####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 new_head.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(9, None)
            l1.next = ListNode(6, None)
            l1.next.next = ListNode(3, None)
            l1.next.next.next = ListNode(8, None)
            ans = new_head(l1, 8)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(1, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l1.next.next.next = ListNode(2, None)
            l1.next.next.next.next = ListNode(5, None)
            l1.next.next.next.next.next = ListNode(1, None)
            ans = new_head(l1, 3)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 new_head.py test1"')


if __name__ == '__main__':
    main()
