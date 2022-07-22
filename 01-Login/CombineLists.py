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
            # print("main_list - ", type(main_list))
            # iterate(main_list)
            return main_list
        elif (i % 2) == 0:
            client = {}
            client.update({"Name":client_list[i]})
            main_list.append(client)
            # print("Client - ", type(client))
        elif (i % 2) != 0:
            actlength = len(actionlist)
            for j in range(actlength):           
                if client_list[i] in actionlist[j]["code"]:
                    # print("Action - ", type(actionlist[j]))
                    client.update({"Action Name":actionlist[j]["Action Name"]})
                    # print(client)
                else: client.update({"Action Name":"Nothing Specified"})

# def iterate(main_list):
#     for i in range(len(main_list)):
#         for key, value in main_list[i].items():
#             # print(key, value)
#             if key == "Name":
#                 # print("\n", "\n", value)
#             elif key == "Action Name":
#                 # print("  - ", value)

main_list()

