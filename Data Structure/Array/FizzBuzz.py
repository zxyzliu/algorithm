"""
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
Example:
n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""


class solution(object):
    def fizzbuzz(self, n):
        result = []
        fizz_time = 0
        buzz_time = 0
        fizzbuzz_time = 0

        for i in range(1, n + 1):
            fizz_time += 1
            buzz_time += 1
            fizzbuzz_time += 1

            if fizz_time == 15:
                result.append("FizzBuzz")
                fizzbuzz_time = 0
                fizz_time = 0
                buzz_time = 0
                continue
            if fizz_time == 3:
                fizz_time = 0
                result.append("Fizz")
                continue
            if buzz_time == 5:
                buzz_time = 0
                result.append("Buzz")
                continue
            result.append(str(i))
        return result

