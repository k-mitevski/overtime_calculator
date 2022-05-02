from datetime import datetime
from tabulate import tabulate
import calendar
import click

time_now = datetime.now()
calendar = calendar.Calendar()

# filter out saturdays and sundays
working_days = len([x for x in calendar.itermonthdays2(time_now.year, time_now.month) if x[0] != 0 and x[1] < 5])

tax = 10
tax_net = 11.11
personal_release = 8788
# total contributions (pension: 18.80%, medical 7.5%, employment 1.2%, insurance 0.5%)
total_contributions = 28
# percentage increase used to calculate from net to gross salary
net_gross_tax = 38.8886366731738


@click.command()
@click.option('--salary', '-s', type=int, help='Your net salary', required=True)
@click.option('--overtime', '-o', type=int, help='Your total overtime hours', required=True)
@click.option('--overtime-percentage', '-p', type=int, default=35, show_default=True,
              help='Overtime percentage increase')
def overtime_calculator(salary: int, overtime: int, overtime_percentage: int) -> None:
    """CLI based calculator for estimating overtime compensation."""

    gross = net_to_gross(salary)
    net = salary

    gross_per_hour, net_per_hour = hourly_salary(salary)
    overtime_gross_hours, total_overtime = add_overtime_gross(salary, overtime, overtime_percentage)
    total_pay_gross = gross + total_overtime
    total_pay_net = gross_to_net(total_pay_gross)
    overtime_net = round((total_pay_net - net))

    print('')
    print(f'Calculating based on {overtime_percentage}% hourly increase.')
    print(f'Total working days in {time_now.strftime("%B")}: {working_days}, number of overtime hours {overtime}.')
    print('')
    print(tabulate([
            ['Net', net, net_per_hour, overtime_net, total_pay_net],
            ['Gross', gross, gross_per_hour, total_overtime, total_pay_gross]],
            headers=['Type', 'Salary', 'Per hour', 'Overtime total', 'Total Pay'],
            tablefmt='orgtbl'))


def net_to_gross(salary: int) -> float:
    salary_personal = salary - personal_release
    salary_personal_tax = round(salary + (salary_personal * (tax_net / 100)))
    gross_salary = round(salary_personal_tax + (salary_personal_tax * (net_gross_tax / 100)))

    return gross_salary


def add_overtime_gross(net_salary: int, overtime_hours: int, overtime_percentage) -> tuple:
    gross_per_hour, _ = hourly_salary(net_salary)
    overtime_gross_per_hour = gross_per_hour + (gross_per_hour * overtime_percentage / 100)
    total_overtime_pay = overtime_gross_per_hour * overtime_hours

    return round(overtime_gross_per_hour), round(total_overtime_pay)


def hourly_salary(net_salary) -> tuple:
    per_hour_gross = net_to_gross(net_salary) / working_days / 8
    per_hour_net = net_salary / working_days / 8
    return round(per_hour_gross), round(per_hour_net)


def gross_to_net(gross_salary: int | float) -> int | float:
    gross_contrib = gross_salary - (gross_salary * (total_contributions / 100))
    gross_personal_contrib = gross_contrib - personal_release
    net_salary = gross_personal_contrib - gross_personal_contrib * (tax / 100) + personal_release + 1
    return round(net_salary)


if __name__ == '__main__':
    overtime_calculator()
