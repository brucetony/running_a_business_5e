import argparse

from random import randint


def calculate_profit(modifier: int, expenses: int, interval: int = 10) -> int:
    """Calculate the net profit for a given interval of days, taking into account expenses (in gp) and modifiers.

    Parameters
    ----------
    modifier : int
        Any penalties or rewards to apply to the result roll. Advertisement of business typically results in a positive
        modifier while damage or rumor can lead to penalties being applied.
    expenses : int
        Total cost of expenses (AKA maintenance) in gold pieces.
    interval : int
        Period of days for which the net profit is calculated. This interval value is added to the roll.

    Returns
    -------
    net : int
        The net profit in gold pieces.
    """
    roll = randint(1, 100)
    result = roll + modifier + interval

    if 1 <= result <= 20:
        net = -1.5 * expenses

    elif 21 <= result <= 30:
        net = -1 * expenses

    elif 31 <= result <= 40:
        net = 0.5 * expenses

    elif 41 <= result <= 60:
        net = 0

    elif 61 <= result <= 80:
        net = randint(1, 6) * 5

    elif 81 <= result <= 90:
        net = (randint(1, 8) + randint(1, 8)) * 5

    else:  # 91+
        net = (randint(1, 10) + randint(1, 10) + randint(1, 10)) * 5

    return net


def period_calculation(days: int, modifier: int, expenses: int, round_up: bool = False, interval: int = 10):
    """Calculate the net profit over several days.

    Parameters
    ----------
    days : int
        Number of days for which the net profit is calculated.
    modifier : int
        Any penalties or rewards to apply to the result roll. Advertisement of business typically results in a positive
        modifier while damage or rumor can lead to penalties being applied.
    expenses : int
        Total cost of expenses (AKA maintenance) in gold pieces.
    interval : int
        Period of days for which the net profit is calculated. This interval value is added to the roll.
    round_up : bool
        If True, will round uneven period / interval ratio up.

    Returns
    -------
    net_profit, periods : Tuple(int, int)
        The net profit in gold pieces and the number of periods calculated.
    """
    periods = days // interval
    if round_up:
        periods += 1

    net_profit = 0
    for i in range(periods):
        net_profit += calculate_profit(modifier, expenses, interval)

    return net_profit, periods


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="5e Business Profit Calculator")
    parser.add_argument("days",
                        type=int,
                        help="Number of days for which the profit should be calculated")
    parser.add_argument("expenses",
                        type=int,
                        help="Total cost of expenses (AKA maintenance) in gold pieces.")
    parser.add_argument("-i",
                        "--interval",
                        type=int,
                        default=10,
                        help="Period of days for which the net profit is calculated.")
    parser.add_argument("-m",
                        "--modifier",
                        type=int,
                        default=0,
                        help="Net penalty or bonus to apply to the result roll.")
    parser.add_argument("-r",
                        "--round-up",
                        action='store_true',
                        help="If True, will round uneven period / interval ratio up.")

    args = parser.parse_args()

    net_profit, periods = period_calculation(days=args.days,
                                             modifier=args.modifier,
                                             expenses=args.expenses,
                                             interval=args.interval,
                                             round_up=args.round_up)

    print(f"""Total number of days: {args.days}
Interval length: {args.interval} days
Number of periods calculated: {periods}
Given expense amount per interval: {args.expenses} gp
Modifier applied: {args.modifier}
Round up: {args.round_up}
Net profit calculated: {net_profit} gp""")
