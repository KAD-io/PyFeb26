"""hm14_job3"""


from datetime import datetime
from dateutil.relativedelta import relativedelta
from logging import getLogger, ERROR, basicConfig

DATE_FORMAT = "%Y-%m-%d"
LOGGER = getLogger()
FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
basicConfig(level=ERROR, format=FORMAT)


def get_days_diff(date_str1, date_str2):
    try:
        date1 = datetime.strptime(date_str1, DATE_FORMAT)
        date2 = datetime.strptime(date_str2, DATE_FORMAT)

        diff = relativedelta(date1, date2)

        return (f"Difference: "
                f"{abs(diff.years)} years, "
                f"{abs(diff.months)} months, "
                f"{abs(diff.days)} days")

    except ValueError:
        LOGGER.error('Check the date format (it should be YYYY-MM-DD)')
        return None


def check_date(date_str):
    today = datetime.now().date()
    try:
        date = datetime.strptime(date_str, DATE_FORMAT).date()

        if date > today:
            return f"{date} — future"
        elif date < today:
            return f"{date} — past"
        else:
            return f"{date} — now"

    except ValueError:
        LOGGER.error('Check the date format (it should be YYYY-MM-DD)')
        return None


input_date1 = input("Enter the first date (YYYY-MM-DD): ")
input_date2 = input("Enter the second date (YYYY-MM-DD): ")
print(get_days_diff(input_date1, input_date2))

input_date = input("Enter the first date (YYYY-MM-DD): ")
print(check_date(input_date))
