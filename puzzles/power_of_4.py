# Check if a number is power of 4 e.g. 16 is 4 ^ 4 
# 1 is also a power of 4 as 4 ^ 0 = 1
def is_power_of_four(num):
	if num == 1:
		return True
	if num < 4:
		return False
	return is_power_of_four(float(num) / 4)
	
if __name__ == "__main__":
	print is_power_of_four(4)
	print is_power_of_four(0)
	print is_power_of_four(1)
	print is_power_of_four(64)
	print is_power_of_four(1000)