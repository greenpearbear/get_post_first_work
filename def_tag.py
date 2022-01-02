def search_tag(list_data):
    dict_result = []
    for value in list_data:
        dict_result_all = value['content'].split()
        for str_in_dict in dict_result_all:
            if str_in_dict[0] == '#' and str_in_dict[-1].isalpha():
                dict_result.append(str_in_dict[1:])
            elif str_in_dict[0] == '#':
                dict_result.append(str_in_dict[1:-1])
    dict_result = sorted(set(dict_result))
    return dict_result