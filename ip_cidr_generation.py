# !/usr/bin/env python

# Usage  python range_2_ip.py 1.1.1.1/24
# returns all the ip addresses in the range including those provide
# only works from /32 to /10 to avoid overrun
# coverts and print the ip addresses with the CIRD



import sys
ip_start = sys.argv[1]
print ip_start
ip_start_string = str(ip_start)     # ensure actual string
tango = ip_start_string.split("/")  # parse by the slash
ipvalue = tango[0]                  # ip address
subnetvalue = int(tango[1])         # CIDR
bits_value = 2**(32-subnetvalue)    # possible addresses
print 'printing', bits_value, 'values' # count

def dqn_to_int(st):
    """
    code from http://code.activestate.com/recipes/users/4175534/
    Convert dotted quad notation to integer
    "127.0.0.1" => 2130706433
    """
    st = st.split(".")
    ###
    # That is not so elegant nor extensible but works well
    ###
    return int("%02x%02x%02x%02x" % (int(st[0]),int(st[1]),int(st[2]),int(st[3])),16)

def int_to_dqn(st):
    """
    code from http://code.activestate.com/recipes/users/4175534/
    Convert integer to dotted quad notation
    """
    st = "%08x" % (st)
    ###
    # The same issue as for `dqn_to_int()`
    ###
    return "%i.%i.%i.%i" % (int(st[0:2],16),int(st[2:4],16),int(st[4:6],16),int(st[6:8],16))



def main():
    if bits_value <= 8388608 and bits_value >= 0:
        ipstart = int(dqn_to_int(ipvalue))
        i = 0
        while i < bits_value:
            print int_to_dqn(ipstart + i)
            i = i + 1
    else:
        print 'not printing, too many or too few addresses'
if __name__ == '__main__':
        main()

