apartment = int(input())
floor = 5
our_froor = 1
apartment_one_floor = 4
entrance = 1
while apartment > floor*apartment_one_floor:
	apartment -= floor*apartment_one_floor
	entrance += 1
print(str(entrance) + "Подъезд")

while apartment > apartment_one_floor:
	apartment -= 4
	our_froor += 1 
print(str(our_froor) + "этаж")
	
