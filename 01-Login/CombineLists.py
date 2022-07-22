from asyncio import events
from GetDetails import get_client_names, get_action_list

client_list = get_client_names()
action_list = get_action_list()

def main_list(client_list, actionlist):    
    print("hello from main_list")
    main_list = []
    length = len(client_list)
    for i in range(length):
        # print("  ----  hello from first loop round: ", i)
        if (i % 2) == 0:
            client = [client_list[i]]
        if (i % 2) != 0:
            actlength = len(actionlist)
            for j in range(actlength):
                # print("      ----      hello from second loop round: ", j)                
                if client_list[i] in actionlist[j]["code"]:
                    client.append(actionlist[j]["Action Name"])
                    # print("====================================================", "\n", "\n", "\n", "\n")
                    # print("is this true?")
                    # print("client_list[", i, "] - ", client_list[i])
                    # print("actionlist[j]['Action Name'] - ", actionlist[j]["Action Name"])
                    # print("actionlist[j]['code'] - ", actionlist[j]["code"])
                    
                    # main_list.append(actionlist[j])
            main_list.append(client)
            print("main_list - ", main_list)
    return main_list

main_list(client_list, action_list)