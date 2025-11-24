def filter_by_name(contacts, name):
    name = name.lower()
    return [c for c in contacts if name in c["full name"].lower()]


def filter_by_street(contacts, street):
    street = street.lower()
    return [c for c in contacts if street in c["address"].lower()]


def filter_by_month(contacts, month):
    # month 可以是 "04", "April", "apr", "4"
    month = month.lower()

    # 先把各种格式统一成数字
    month_map = {
        "jan": 1, "january": 1,
        "feb": 2, "february": 2,
        "mar": 3, "march": 3,
        "apr": 4, "april": 4,
        "may": 5,
        "jun": 6, "june": 6,
        "jul": 7, "july": 7,
        "aug": 8, "august": 8,
        "sep": 9, "september": 9,
        "oct": 10, "october": 10,
        "nov": 11, "november": 11,
        "dec": 12, "december": 12,
    }

    # 如果是数字格式（04, 4）
    if month.isdigit():
        month_num = int(month)
    else:
        month_num = month_map.get(month, None)

    if month_num is None:
        raise ValueError(f"Unsupported month format: {month}")

    # birthday 是 datetime.date 类型 → 用 date.month
    return [c for c in contacts if c["birthday"].month == month_num]



def limit_results(contacts, n):
    return contacts[:n]
