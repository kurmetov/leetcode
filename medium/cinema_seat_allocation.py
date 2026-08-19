class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()

            rows[row].add(seat)

        left = {2, 3, 4, 5}
        mid = {4, 5, 6, 7}
        right = {6, 7, 8, 9}


        res = (n - len(rows)) * 2

        
        for reserved in rows.values():

            left_free = not (reserved & left)
            mid_free = not (reserved & mid)
            right_free = not (reserved & right)

            if left_free and right_free:
                res += 2
            elif left_free or mid_free or right_free:
                res += 1

        return res



