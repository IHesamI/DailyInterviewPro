def room_is_free(start, end, lectures):
    for each_lecture in lectures:
        lec_start = each_lecture[0]  
        lec_end = each_lecture[1]   
        if lec_start > end or lec_end > start or (lec_start < start and lec_end > end) or (lec_start > start and lec_end < end):
            return False
    return True
  
def meeting_rooms(meetings):
    rooms_dict = {}
    room_count = 1
    for lecture in meetings:
        start = lecture[0]
        end = lecture[1]
        if len(rooms_dict.keys()) == 0:
            key = 'room'+str(room_count)
            rooms_dict[key] = [lecture]
            room_count += 1
        else:
            should_add_room = True
            for key, value in rooms_dict.items():

                if room_is_free(start=start, end=end, lectures=value):
                    value.append(lecture)
                    rooms_dict[key] = value
                    should_add_room = False
                    break
                 
            if should_add_room:
                key = 'room'+str(room_count)
                rooms_dict[key] = [lecture]
                room_count += 1

    return len(rooms_dict.keys())


# print 1
print(meeting_rooms([(0, 10), (10, 20)]))
# 1

print(meeting_rooms([(20, 30), (10, 21), (0, 50)]))
# 3 (all meetings overlap at time 20)
