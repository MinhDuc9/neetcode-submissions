class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        left = 0
        tracking = 0

        for right in range(len(s)):
            if s[right] not in count:
                count[s[right]] = 0
            count[s[right]] += 1

            tracking = max(tracking, count[s[right]])
            
            while right - left + 1 - tracking > k:
                """
                Truong hop nay khong can cap nhat tracking
                Vi dieu kien khi thu nho lai window la khi:
                - window size - So luong freq char > k
                - Co nghia la phai dung so luong lon hon k de thay doi char thi moi thoa de bai
                
                Nhung khong can cap nhat lai tracking vi:
                - Neu co sai cung khong sao.
                - Vi right va left se la bounding
                - Vi tracking >= real size of freq
                - Va vi the se ko anh huong toi res
                """
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res