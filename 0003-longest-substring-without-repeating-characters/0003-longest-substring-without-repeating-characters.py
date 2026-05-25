class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # lp: 현재 substring의 시작인덱스(인덱스 포함)
        # rp: 현재 substring의 끝인덱스 (인덱스 미포함)
        lp = rp = 0
        max_length = 0

        # 현재 substring에 있는 모든 문자를 포함
        chars = set()

        # rp가 맨 끝에 도착하면 종료
        while rp < len(s):
            # 현재 substring에 있는 문자가 나올떄까지 rp를 이동한다.
            while rp <= len(s) - 1 and not s[rp] in chars:
                # print(f'add {s[rp]} in {chars}')
                chars.add(s[rp])
                rp = rp + 1

            # 현재 substring의 길이를 반영한다.
            max_length = max(max_length, rp - lp)
            print(f'{s[lp:rp]}')

            # 현재 rp가 가리키는 문자가 나올떄까지 lp를 이동한다.
            while rp <= len(s) - 1 and s[lp] != s[rp]:
                chars.remove(s[lp])
                lp = lp + 1

            if lp <= len(s) - 1:
                chars.remove(s[lp])
                lp = lp + 1
            print(f'{lp} {rp} {chars}')

        return max_length