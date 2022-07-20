from GetDetails import get_client_names, get_action_list

client_list = get_client_names()
action_list = get_action_list()

def main_list(client_list, actionlist):    
    print("hello from main_list")
    main_list = []
    for i in client_list:
        for j in actionlist:
            print("action name - ", j["Action Name"], j["Action Name"])
            # print
            # if i == j["client_name"]:
            #     main_list.append(j)
    print("main_list - ", main_list)
    return main_list

main_list(client_list, action_list)