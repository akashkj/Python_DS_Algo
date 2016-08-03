class Tower(object):

	def __init__(self, tower_index, towers_info):
		self.height = towers_info[tower_index]
		if tower_index == 0:
			self.left_max = 0
		else:
			self.left_max = max(towers_info[:tower_index])
		if tower_index == len(towers_info) - 1:
			self.right_max = 0
		else:
			self.right_max = max(towers_info[tower_index:])
		
def get_trapped_water_amount(towers_info):
	towers = []
	water_trapped = 0
	for i in range(len(towers_info)):
		towers.append(Tower(i, towers_info))
	for tower in towers:
		current_tower_water = max(min(tower.left_max, tower.right_max) - tower.height, 0)
		water_trapped += current_tower_water
	return water_trapped
	
if __name__ == "__main__":
	assert get_trapped_water_amount([2, 0, 2]) == 2
	assert get_trapped_water_amount([3, 0, 0, 2, 0, 4]) == 10
	assert get_trapped_water_amount([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
	