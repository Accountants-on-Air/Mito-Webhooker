from monday import MondayClient
import json
client = MondayClient('eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjIyMDI0MjExNSwiYWFpIjoxMSwidWlkIjozNzc5MjU0MCwiaWFkIjoiMjAyMy0wMS0xMFQxNjowNzoxNS4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6NjkwOTQ3NCwicmduIjoidXNlMSJ9.ZiE5WtSS3eW5NgNLoOO7jHrDZvRBHMmmNApWhnfRIhk')
def executer(data): #Master Database
    client.items.change_multiple_column_values(5015701381,data['event']['value']['linkedPulseIds'][0]['linkedPulseId'],json.loads('{{\"connect_boards1\" : {{\"item_ids\" : {}}}}}'.format([data['event']['pulseId']])))

def executer2(data): #Tax Prep Assignments
    #client.items.change_multiple_column_values(1604758265,)
    print(data)
