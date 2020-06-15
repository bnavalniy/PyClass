from statistics import mean
import json


def get_firms_info_from_file(file_name):
    firms = {}
    with open(file_name) as file:
        for line in file:
            (name, prop_type, income, outcome) = line.split(" ")
            firms[name] = dict(prop_type=prop_type, income=int(income), outcome=int(outcome))
    return firms


def get_list_of_firms_with_profit_calculated(firms):
    firms = dict(firms)
    return [{firm[0]: (firm[1].get('income') - firm[1].get('outcome'))} for firm in firms.items()]


def get_average_profit(firms):
    profits = []
    for firm in firms:
        profits.append((list(firm.items())[0])[1])
    return {"average_profit": mean(profits)}


def write_to_json(firms_with_profit, average_profit, file_name):
    d = [firms_with_profit, average_profit]
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(d, file, ensure_ascii=False)


firms = get_list_of_firms_with_profit_calculated(get_firms_info_from_file("text_7.txt"))
av_pr = get_average_profit(firms)
write_to_json(firms, av_pr, "final.json")
