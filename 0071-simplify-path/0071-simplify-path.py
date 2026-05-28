class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        tokens = path.split("/")
        for token in tokens:
            if token == "":
                continue
            if token == ".":
                continue
            if token == "..":
                if len(st) > 0:
                    st.pop(-1)
                continue
            st.append(token)

        return "/" + "/".join(st)
        