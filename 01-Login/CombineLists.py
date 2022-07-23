from asyncio import events
from GetDetails import get_client_names, get_action_list

# client_list = get_client_names()
# action_list = get_action_list()

def main_list():    
    client_list = get_client_names()
    action_list = get_action_list()
    main_list = []
    length = len(client_list)
    for i in range(length):
        client = {}
        actions = []
        if client_list[i] == "All Applications":
            print("main_list - ", main_list)
            # iterate(main_list)
            return main_list
        elif (i % 2) == 0:
            client.update({"Name":client_list[i]})
            main_list.append(client)
        alength = len(action_list)
        # print("i - ", i)
        for j in range(alength):    
            # print("j - ", j)       
            if client_list[i] in action_list[j]["code"]:
                # print("Action - ", action_list[j])
                actions.append({"Action Name":action_list[j]["Action Name"]})
            client.update({"Actions":actions})
            # print(i, " - client - ", client)

    
main_list()

