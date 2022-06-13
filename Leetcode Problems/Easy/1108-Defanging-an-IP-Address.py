'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
'''

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        addr = list(address)
        output = ""
        for i in range(len(addr)):
            if(addr[i] == '.'):
                addr[i] = '[.]'
        return output.join(addr)