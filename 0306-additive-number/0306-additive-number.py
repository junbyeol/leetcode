class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def is_leading_zero(num: str):
            if num.startswith('0') and not int(num) == 0:
                return True
            return False

        def rec(pred: str, next_pred: str, follow: str):
            if follow == "":
                return True

            if is_leading_zero(pred) or is_leading_zero(next_pred) or is_leading_zero(follow):
                return False

            s = str(int(pred) + int(next_pred))
            if follow.startswith(s):
                return rec(next_pred, s, follow[len(s):])
            return False
            
        first_len = 1
        while first_len < len(num) - first_len:
            second_len = 1
            while max(first_len, second_len) <= len(num) - first_len - second_len:
                if rec(num[:first_len], num[first_len:first_len+second_len], num[first_len+second_len:]):
                    return True
                second_len = second_len + 1
            first_len = first_len + 1
        
        return False