class Solution(object):
    def restoreIpAddresses(self, s):
        result = []
        self.BTrestoreIpAddresses(0, s, [], result)
        return result

    def BTrestoreIpAddresses(self, sect, s, ip, result):
        if not s:
            if sect == 4:
                result.append( '.'.join(ip))
            return
        elif sect==4:
            return
        self.BTrestoreIpAddresses(sect+1 , s[1:] , ip+[s[:1]] , result)
        if s[0] != '0':
            if len(s) >=2 :
                self.BTrestoreIpAddresses(sect+1, s[2:] , ip+[s[:2]], result)
            if len(s) >=3 and int(s[:3]) <= 255:
                self.BTrestoreIpAddresses(sect+1 ,s[3:] , ip+[s[:3]], result)






'''
        if not s:
            if sect == 4:
                result.append('.'.join(ip))
            return
        elif sect == 4:
            return
        self._restoreIpAddresses(sect + 1, s[1:], ip + [s[:1]], result)
        if s[0] != '0':
            if len(s) >= 2:
                self._restoreIpAddresses(sect + 1, s[2:], ip + [s[:2]], result)
            if len(s) >= 3 and int(s[:3]) <= 255:
                self._restoreIpAddresses(sect + 1, s[3:], ip + [s[:3]], result)
'''
print Solution().restoreIpAddresses("25525511135")
