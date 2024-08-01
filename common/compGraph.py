def compareStateAndDyn(states, dyns):
    for index, state in enumerate(states):
        if len(dyns) > index:
            for item in state:
                index_dyn = -1
                for dyn in dyns:
                    if item in dyn:
                       index_dyn = 0
                if index_dyn == -1:
                   print(f"lost {item}")
