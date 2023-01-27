def get_stores_names(stores):
    name_list = []

    for store in stores:
        if store.store_name not in name_list:
            name_list.append(store.store_name)

    name_list = list(filter(len, name_list))

    return name_list
