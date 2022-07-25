from GetDetails import get_client_names, get_action_list

def main_list():    
    client_list = get_client_names()
    action_list = get_action_list()
    main_list = []
    length = len(client_list)
    for i in range(length):
        client = []
        actions = []
        if client_list[i] == "All Applications":
            return main_list
        elif (i % 2) == 0: 
            client.append({"Name":client_list[i]})
        else:
            alength = len(action_list)
            for j in range(alength):    
                if client_list[i] in action_list[j]["code"]:
                    actions.append({"Action Name":action_list[j]["Action Name"]})
            main_list.append({"Name":client_list[i-1], "Actions":actions})