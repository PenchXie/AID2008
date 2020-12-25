from month05.datastructure.day01.singleLinkList import SingleLinklist


class Solution:
    def merge(self, head1, head2):
        cur1 = head1
        cur2 = head2
        if cur1.value <= cur2.value:
            new_head = cur1
            cur1 = cur1.next
        else:
            new_head = cur2
            cur2 = cur2.next

        new_cur = new_head
        while cur1 and cur2:
            if cur1.value <= cur2.value:
                new_cur.next = cur1
                cur1 = cur1.next
                new_cur = new_cur.next
            else:
                new_cur.next = cur2
                cur2 = cur2.next
                new_cur = new_cur.next
        new_cur.next = cur1 if cur1 else cur2
        return new_head

if __name__ == '__main__':
    ssl01 = SingleLinklist()
    ssl02 = SingleLinklist()
    ssl01.append(1)
    ssl01.append(3)
    ssl01.append(6)
    ssl01.append(8)
    ssl02.append(2)
    ssl02.append(3)
    ssl02.append(5)
    ssl02.append(9)
    # for num in ssl01.traverse():
    #     print(num, end=' ')
    # for num in ssl02.traverse():
    #     print(num, end=' ')
    sol = Solution()
    new_head = sol.merge(ssl01.head, ssl02.head)
    print(new_head.value)
    while new_head:
        print(new_head.value)
        new_head = new_head.next