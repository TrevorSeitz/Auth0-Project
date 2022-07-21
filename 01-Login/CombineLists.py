from GetDetails import get_client_names, get_action_list

client_list = get_client_names()
action_list = get_action_list()

def main_list(client_list, actionlist):    
    print("hello from main_list")
    main_list = []
    length = len(client_list)
    # print("length - client_list - ", len(client_list))
    for i in range(length):
        print("  ----  hello from first loop round: ", i)
        # print("client_list i - ", i)
        # print("type- client_list[i] - ", type(client_list[i]))
        print("clientlist - i - ", client_list[i])
        actlength = len(actionlist)
        for j in range(actlength):
            print("      ----      hello from second loop round: ", j)
            # print("ActionList j - ", j)
            # print("type- actionlist[j] - ", type(actionlist[j]["code"]))
            print("This is avtionlist[j] - ", actionlist[j]["code"])
            
            if client_list[i] in actionlist[j]["code"]:
                print("is this true?")
                print("client_list[i] - ", client_list[i])
                print("actionlist[j]['Action Name'] - ", actionlist[j]["Action Name"])
                print("actionlist[j]['code'] - ", actionlist[j]["code"])
                
                main_list.append(actionlist[j])
            # print(actionlist[j])
        #     print("actionlist - - ", action_list[i])
        #     print("action name i  - ", i)
        #     # if i == j["client_name"]:
        #     #     main_list.append(j)
            # print("main_list - ", main_list)
    return main_list

main_list(client_list, action_list)