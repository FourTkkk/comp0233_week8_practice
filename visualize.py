def visualize_birthdays(contacts):
    """
    Print a month-by-month list of birthdays.
    Contacts: list of dicts with birthday as datetime.date
    """
    months = {i: [] for i in range(1, 13)}  # 1–12 月

    for c in contacts:
        month = c["birthday"].month
        months[month].append(c["full name"])

    # 输出结果
    for m in range(1, 13):
        if months[m]:  # 只打印有人的月份
            names = ", ".join(months[m])
            print(f"{m:02d}: {names}")
