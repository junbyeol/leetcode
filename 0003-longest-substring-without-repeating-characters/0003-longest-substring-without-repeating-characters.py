class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # lp: 현재 substring의 시작인덱스(인덱스 포함)
        # rp: 현재 substring의 끝인덱스 (인덱스 미포함)
        lp = rp = 0
        max_length = 0

        # 현재 substring에 있는 모든 문자를 포함
        chars = {}

        # rp가 맨 끝에 도착하면 종료
        while rp < len(s):
            # 현재 substring에 있는 문자가 나올떄까지 rp를 이동한다.
            # 그동안 등장한 문자들을 dict에 추가해둔다.
            while rp < len(s) and not s[rp] in s[lp:rp]:
                chars[s[rp]] = rp
                rp = rp + 1

            # 현재 substring의 길이를 반영한다.
            max_length = max(max_length, rp - lp)
            print(f'{s[lp:rp]}')

            # 현재 rp가 가리키는 문자가 처음 등장한 곳, 바로 다음으로 lp를 옮긴다
            # 현재 rp가 가리키는 문자의 인덱스를 rp로 맞춰 고쳐둔다
            if rp < len(s):
                lp = chars[s[rp]] + 1
                chars[s[rp]] = rp
            print(f'{lp} {rp} {chars}')

        return max_length