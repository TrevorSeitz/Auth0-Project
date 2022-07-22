from asyncio import events
from GetDetails import get_client_names, get_action_list

client_list = get_client_names()
action_list = get_action_list()

def main_list():    
    client_list = get_client_names()
    actionlist = get_action_list()
    main_list = []
    length = len(client_list)
    for i in range(length):
        if client_list[i] == "All Applications":
            # print("main_list - ", main_list)
            return main_list
        elif (i % 2) == 0:
            client = [client_list[i]]
        elif (i % 2) != 0:
            actlength = len(actionlist)
            for j in range(actlength):               
                if client_list[i] in actionlist[j]["code"]:
                    client.append(actionlist[j]["Action Name"])
            main_list.append(client)

main_list()