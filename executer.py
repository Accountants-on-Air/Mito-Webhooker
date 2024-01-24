from monday import MondayClient
import json
client = MondayClient('eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjIyMDI0MjExNSwiYWFpIjoxMSwidWlkIjozNzc5MjU0MCwiaWFkIjoiMjAyMy0wMS0xMFQxNjowNzoxNS4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6NjkwOTQ3NCwicmduIjoidXNlMSJ9.ZiE5WtSS3eW5NgNLoOO7jHrDZvRBHMmmNApWhnfRIhk')
def executer(data): #Master Database
    ITEM = client.items.fetch_items_by_id(data['event']['value']['linkedPulseIds'][0]['linkedPulseId'])
    try:
        PULSES_DICT = [json.loads(i['value'])['linkedPulseIds'] for i in ITEM['data']['items'][0]['column_values'] if i['id']=='connect_boards1'][0]
        CONNECTION_IDS = [i['linkedPulseId'] for i in PULSES_DICT]
        CONNECTION_IDS.append(data['event']['pulseId'])
        print(client.items.change_multiple_column_values(5015701381,data['event']['value']['linkedPulseIds'][0]['linkedPulseId'],json.loads('{{\"connect_boards1\" : {{\"item_ids\" : {}}}}}'.format(CONNECTION_IDS))))
    except:
        print(client.items.change_multiple_column_values(5015701381,data['event']['value']['linkedPulseIds'][0]['linkedPulseId'],json.loads('{{\"connect_boards1\" : {{\"item_ids\" : {}}}}}'.format([data['event']['pulseId']]))))

def executer2(data): #Tax Prep Assignments
    client.items.change_multiple_column_values(1604758265,data['event']['value']['linkedPulseIds'][0]['linkedPulseId'],json.loads('{{\"connect_boards8\" : {{\"item_ids\" : {}}}}}'.format([data['event']['pulseId']])))
