"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2
"""

timetable = [(30, 75), (0, 50), (60, 150), (51,59)]

bin_list = []

ctr = 0

def try_1(timetable, bin_list, ctr):
	sorted_timetable = sorted(timetable)

	for klass in sorted_timetable:
		print(range(klass[0], klass[1]+1))
		print(bin_list)
		if (bool(set(range(klass[0], klass[1]+1)) & set(bin_list))) :
			print(1)
			bin_list.extend(range(klass[0], klass[1]+1))
			ctr +=1
		else:
			print(2)
			ext = list(set(range(klass[0], klass[1]+1)) - set(bin_list))
			bin_list.extend(ext)

	print(ctr)

# this system is not robust, must have a release class room system1, could be a way out of it but not sure how

def try_2(timetable):
	start = sorted(list(t[0] for t in timetable))
	end = sorted(list(t[1] for t in timetable))

	max_room = room_occupied = 0
	n = len(start)
	i = j = 0

	while i < n and j < n:
		if start[i] < end[j]:
			room_occupied += 1
			max_room = max(max_room, room_occupied)
			# similar solution to longest substring, D13
			i += 1
		else:
			room_occupied -=1
			j += 1
	print(max_room)

try_2(timetable)