# Running a Business Calculator - 5e
A script for calculating how much money a business makes in a given period of time for 5th edition Dungeons &amp; Dragons. 

## Calculation
This calculator uses the table shown on page 129 of the Dungeon Master's Guide. Generally, the profits/costs are calculated every tenday (10 days), but the interval can be modified (see [Usage](#usage)). Here is a brief summary of the table:

| d100 + days  | Result                                                                                                |
|--------------|-------------------------------------------------------------------------------------------------------|
| 01-20        | You must pay one and a half times the business's maintenance cost for each of the days.               |
| 21-30        | You must pay the business's full maintenance cost for each of the days.                               |
| 31-40        | You must pay half the business's maintenance cost for each of the days. Profits cover the other half. |
| 41-60        | The business covers its own maintenance cost for each of the days.                                    |
| 61-80        | The business covers its own maintenance cost for each of the days. It earns a profit of ld6 x 5 gp.   |
| 81-90        | The business covers its own maintenance cost for each of the days. It earns a profit of 2d8 x 5 gp.   |
| 91+          | The business covers its own maintenance cost for each of the days. It earns a profit of 3dl0 x 5 gp.  |

### Example
If calculating within a tenday interval, a d100 is rolled and a +10 is added to the result and used to determine which result row to use. If calculating using a different interval, that interval (in days) is applied to the roll instead before determining the result.

## Usage
The script requires one to put in how many days have passed and the cost of expenses (in gold pieces [gp]) for the given interval. If using the standard tenday interval one can simply run:
```bash
python business.py 100 60
```
Here, the script will determine the total profit over a 100 day period, in tenday intervals, where each interval requires 60gp in expenses.

### Modifying the Interval
One can change the interval for which the profits are calculated using the `-i` option:
```bash
python business.py 100 60 -i 5
```
Now the script will calculate total profits over a 100 day period, using 5 day intervals, where each 5 day interval requires 60gp in expenses. It is very important to adjust expenses based on interval length!  

#### Rounding
If the interval length does not divide evenly into the period, the calculator will round down e.g. 66 days with a tenday interval results in 6 "tendays" worth of profit being calculated. Using the `-u` option will change it to round up instead
