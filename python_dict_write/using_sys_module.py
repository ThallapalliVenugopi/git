import sys
#
# sys.version
# '3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)]'
# sys.version_infosys.getwindowsversion()
# sys.getwindowsversion(major=10, minor=0, build=22621, platform=2, service_pack='')
#
#sys.version_info(major=3, minor=11, micro=1, releaselevel='final', serial=0)
x = [1, 2]
y = [21, 45, 67, 34, 67, 89]
z = [23, 56, 78, 90]
print(sys.getsizeof(x))
print(sys.getsizeof(y))
print(sys.getsizeof(z))