arr = [
    {"id": 1, "start": 1, "end": 5},
    {"id": 2, "start": 2, "end": 6},
    {"id": 3, "start": 4, "end": 7},
    {"id": 4, "start": 4, "end": 8},
    {"id": 5, "start": 7, "end": 10},
]

server = []
add_server = True
for i in arr:
    start_time_of_server = i["start"]
    if len(server) == 0:
        server.append({
                    "id": i["id"],
                    "end_time": i["end"]
                })
    else:
        for j in server:
            if j["end_time"] <= i["start"]:
                add_server = False
                server[server.index(j)] = {
                    "id": i["id"],
                    "end_time": i["end"]
                }
         
        
        if add_server:       
            server.append({
                    "id": i["id"],
                    "end_time": i["end"]
                })
    add_server = True
        
   
print(len(server))
            
    
            