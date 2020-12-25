from day01.singleLinkList import SingleLinklist

class Solution:
    def find_public_node(self, sll1: SingleLinklist, sll2: SingleLinklist):
        sll1.reverse()
        sll2.reverse()
        r_head1 = sll1.head
        r_head2 = sll2.head
        while True:
            if not r_head1.next or not r_head2.next:
                return None
            if r_head1.next.value != r_head2.next.value:
                return r_head1
            r_head1 = r_head1.next
            r_head2 = r_head2.next

if __name__ == '__main__':
    ssl01 = SingleLinklist()
    ssl02 = SingleLinklist()
    ssl01.append(1)
    ssl01.append(3)
    ssl01.append(6)
    ssl01.append(8)
    ssl02.append(2)
    ssl02.append(4)
    ssl02.append(6)
    ssl02.append(8)
    s = Solution()
    print(s.find_public_node(ssl01, ssl02).value)
