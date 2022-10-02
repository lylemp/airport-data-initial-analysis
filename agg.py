import pandas as po
def count_unique_carriers(df : po.DataFrame) -> int:
    list_of_carriers = (df.str.lower().str.split(",").values)

    set_of_carriers = set()
    for lst in list_of_carriers:
        set_of_carriers.update(lst)

    return len(set_of_carriers)

def unique_carriers(df : po.DataFrame) -> int:
    list_of_carriers = df.str.lower().str.split(",").values
    set_of_carriers = set()
    for lst in list_of_carriers:
        set_of_carriers.update(lst)

    return (set_of_carriers) 

