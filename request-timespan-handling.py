requests = [
    {"user_id": 1, "timestamp": 1},
    {"user_id": 1, "timestamp": 2},
    {"user_id": 1, "timestamp": 3},
    {"user_id": 1, "timestamp": 4},
    {"user_id": 1, "timestamp": 5},
    {"user_id": 2, "timestamp": 6},
    {"user_id": 1, "timestamp": 8}
]


window = 5
limit = 3
a = {}
for i in requests:
    if window == 0:
        window = 5
        for j,request in a.items():
            a[j] = 0
            
        
    else:
        request_counter = a.get(i["user_id"], False)
        if request_counter != False and request_counter > limit:
            print("user not allowed")
        else:
            if request_counter == False:
                a[ i["user_id"]] = 1
                
            else:
                a[ i["user_id"]] = a[ i["user_id"]] + 1
            
            
    window = window - 1
    
    
    