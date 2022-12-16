from database import get_data_for_grafic


def config_data():
    data = get_data_for_grafic()
    res = {}
    totalCount=[]
    labels=[]
    for el in data:
        if el[3] in res.keys():
            res[el[3]] += el[2]
        else:
            res[el[3]] = el[2]
    for key in res.keys():
        labels.append(key)
        totalCount.append(res[key])

    return (labels, totalCount)

