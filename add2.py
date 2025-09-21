"""
File: add2.py
Name: wei chen
------------------------
將ListNode的value取出後，反向排列成為一正整數，將兩組ListNode的正整數相加，再將正整數的數字拆解，並反向儲存。
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    cur1 = l1  # 第一條ListNode
    count1 = 0  # 第一條ListNode的index
    total = 0  # 數字*(10**count1)，將數字轉成正整數
    while cur1:
        n1 = int(cur1.val)  # 取ListNode的值
        total += n1 * (10 ** count1)
        count1 += 1
        cur1 = cur1.next

    cur2 = l2   # 第二條ListNode
    count2 = 0  # 第二條ListNode的index
    while cur2:
        n2 = int(cur2.val)
        total += n2 * (10 ** count2)  # 兩條ListNode轉成正整數相加
        count2 += 1
        cur2 = cur2.next

    ans = None
    # ans = ListNode()  # 起始的ListNode會是0
    cur = ans
    if total == 0:
        new_node = ListNode(0, None)
        ans = new_node
        return ans
    else:
        while total >= 1:
            num = total % 10  # 取total最後的數字，為data
            new_node = ListNode(num, None)
            total = total // 10
            if not ans:
                # First data
                cur = new_node
                ans = new_node
            else:
                cur.next = new_node
                cur = cur.next
        return ans
    #######################

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
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
