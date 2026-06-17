class Solution:
    
    def multiply(self, num1: str, num2: str) -> str:
        # "abc" * "def" = "abc" * "d" + "abc" * "e" * 10 + "abc" * "f" * 100
        # first_res = ["abc" * "d", "abc" * "e" * 10, "abc" * "f" * 100]
        first_res = []
        max_len = 0

        if num1 == "0" or num2 == "0":
            return "0"

        def mult_a(num: str, digit: str):
            if digit == "0" or num == "0":
                return "0"

            res = ""
            carry = 0
            it = 0
            while it < len(num):
                mult = int(num[len(num) - it - 1]) * int(digit) + carry
                res = str(mult % 10) + res
                carry = mult // 10
                it = it+1

            if carry != 0:
                res = str(carry) + res

            return res

        for idx, c in enumerate(reversed(num2)):
            mult = mult_a(num1, c)
            first_res.append(mult + "0" * idx)
            max_len = max(max_len, len(mult) + idx)

        # print(first_res)

        res = ""
        carry = 0
        res_it = 0
        # print(max_len)
        while res_it < max_len:
            s = 0
            for num_str in first_res:
                s = s + ( int(num_str[len(num_str) - res_it - 1]) if res_it < len(num_str) else 0 )
        
            s = s + carry
            res = str(s % 10) + res
            carry = s // 10
            res_it = res_it + 1
            # print(res,carry)

        if carry != 0:
            res = str(carry) + res

        return res

        
            