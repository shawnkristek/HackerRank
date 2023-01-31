from timeit import timeit

class LNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return str(self.data)

    def LinkedList(arr: list[int]):
        head = None
        for i in reversed(arr):
            node = LNode(i)
            if head is None:
                head = node
            else:
                node.next = head 
                head = node            

        return head


class Solution:
    def mergeLists(head1, head2):
        #help 
        #https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/

        # Write your code here
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        if head1.data < head2.data:
            head1.next = Solution.mergeLists(head1.next, head2)
            return head1
        else:
            head2.next = Solution.mergeLists(head1, head2.next)
            return head2

class Solution1:
    def mergeLists(head1, head2):
        head = None
        current = None

        if head1 is None:
            return head2
        elif head2 is None:
            return head1

        while head1 and head2:
            if head1.data < head2.data:
                if head is None:
                    head = head1
                    current = head
                else:
                    current.next = head1
                    current = current.next
                head1 = head1.next
            else:
                if head is None:
                    head = head2
                    current = head
                else:
                    current.next = head2
                    current = current.next
                head2 = head2.next
        else:
            if head1:
                current.next = head1
            elif head2:
                current.next = head2

        return head


# testing
tests = [
    (
        LNode.LinkedList([1, 2, 3]),
        LNode.LinkedList([3, 4]),
        [1, 2, 3, 3, 4]
    ),
    (
        LNode.LinkedList([4,5,6]),
        LNode.LinkedList([1,2,10]),
        [1,2,4,5,6,10]
    )
]

for head1, head2, solution in tests:
    sol = Solution1.mergeLists(head1, head2)
    p_sol = []
    while sol.next:
        # print(sol.data)
        p_sol.append(sol.data)
        sol = sol.next
    else:
        # print(sol.data)
        p_sol.append(sol.data)

    print(p_sol)
    assert p_sol == solution
