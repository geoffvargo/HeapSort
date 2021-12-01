import math
import os
import random
import re
import sys

from heapq import *


#
# Complete the 'heapsort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def heapsort(arr):
	h = []
	for elem in arr:
		heappush(h, elem)
	
	return [heappop(h) for i in range(h.__len__())]
