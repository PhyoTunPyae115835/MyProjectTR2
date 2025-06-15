"""
Refactored cumulative total income program with function and SRP compliance
"""


def main():
    """Get income data and display a formatted income report."""
    number_of_months = get_month_count()
    incomes = get_monthly_incomes(number_of_months)
    print_income_report(incomes)


def get_month_count():
    """Prompt user for number of months and return it."""
    return int(input("How many months? "))


def get_monthly_incomes(months):
    """Get a list of incomes for the given number of months."""
    incomes = []
    for month in range(1, months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    return incomes


def print_income_report(incomes):
    """Print the income and cumulative total for each month."""
    print("\nIncome Report\n-------------")
    total = 0
    for month_index, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month_index:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


if __name__ == "__main__":
    main()
