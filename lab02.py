# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Just replace each `pass` with your code, using `return` to send the answer
# back (not `print`).


def seconds_to_hms(total_seconds):
    hours: int = total_seconds // (60*60)
    minutes: int = (total_seconds - H*60*60)//60
    seconds: int = total_seconds - M*60 - H*60*60
    print(f"{hours:2d}:{minutes:02d}:{seconds:02d}")
    # TODO (Part 1): return the time as a string "H:MM:SS"
    #   e.g. seconds_to_hms(3661) should return "1:01:01"
    return hours,minutes,seconds


def admission_price(age):
    if(age < 5):
        price: float = 0.00
    elif(age <= 12):
        price : float = 8.00
    elif(age <= 64):
        price : float = 15.00
    else:
        price : float = 10.00
    

    # TODO (Part 2): return the ticket price (a number) for someone of this age
    return price


def sum_multiples(limit):
    total = 0
    for i in range(limit):
        if i %3 == 0:
            total += 3
        if i %5 ==0:
            total += 5
   
    # TODO (Part 3): return the sum of every whole number below `limit`
    #   that is a multiple of 3 or of 5
    return total


def total_of_positives(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    # TODO (Part 4 - STRETCH, optional): return the sum of just the
    #   positive numbers in the list `numbers`
    return total


def main():
    # Optional scratch space - use this to try your functions with sample values.
    # Uncomment a line and run `python lab02.py` to see the result.
    print(seconds_to_hms(3661))            # 1:01:01
    print(admission_price(10))             # 8
    print(sum_multiples(10))               # 23
    print(total_of_positives([1, -2, 3]))  # 4
    pass


if __name__ == "__main__":
    main()

