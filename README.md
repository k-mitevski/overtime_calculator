# CLI based salary overtime calculator
#### Built with Python using the [Click library](https://click.palletsprojects.com/en/8.1.x/)

#### Calculates your total monthly compensation including overtime hours. Based on labor laws in Republic of Macedonia.
#### It works by taking the current month workdays, adding your overtime hours and calculating your total compensation based on your net salary.

https://user-images.githubusercontent.com/51249239/166264532-92be131e-72df-4479-831b-71ac74f1ff1f.mp4

```
Usage: main.py [OPTIONS]

  CLI based calculator for estimating overtime compensation.

Options:
  -s, --salary INTEGER            Your net salary  [required]
  -o, --overtime INTEGER          Your total overtime hours  [required]
  -p, --overtime-percentage INTEGER
                                  Overtime percentage increase  [default: 35]
  --help                          Show this message and exit.
```

### Install and usage

Create a virtual environement, install the libraries and run the main.py.

```
pip install -r requirements.txt
```

```
python main.py --salary 30000 --overtime 5

Calculating based on 35% hourly increase.
Total working days in May: 22, number of overtime hours 5.

| Type   |   Salary |   Per hour |   Overtime total |   Total Pay |
|--------+----------+------------+------------------+-------------|
| Net    |    30000 |        170 |             1116 |       31116 |
| Gross  |    44940 |        255 |             1721 |       46661 |
```
You can also use shortened options:
```
python main.py -s 100000 -o 5 -p 50
Calculating based on 50% hourly increase.
Total working days in May: 22, number of overtime hours 5.

| Type   |   Salary |   Per hour |   Overtime total |   Total Pay |
|--------+----------+------------+------------------+-------------|
| Net    |   100000 |        568 |             4224 |      104224 |
| Gross  |   152964 |        869 |             6518 |      159482 |
```

# TODO
- Fix rounding errors
- Add option to choose a month
