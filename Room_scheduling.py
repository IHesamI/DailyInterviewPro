def room_is_free(start, end, lectures):
    for each_lecture in lectures:
        lec_start = each_lecture[0]  
        lec_end = each_lecture[1]   
        if lec_start > end or lec_end > start or (lec_start < start and lec_end > end) or (lec_start > start and lec_end < end):
            return False
    return True


def Scheduler(arr):
    rooms_dict = {}
    room_count = 1
    for lecture in arr:
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

    print(rooms_dict)
    return len(rooms_dict.keys())


print(Scheduler([(30, 75), (0, 50), (60, 150),(30,40)]))
# 3
