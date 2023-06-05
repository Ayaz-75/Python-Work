import random

total_pulse_per_minute = random.randint(60, 90)
get_pulse_in_hour = total_pulse_per_minute * 60
pulse_per_3times = get_pulse_in_hour / 3


def get_pulse():
    # 60 to 100 beats per minute
    total_pulse_in_4hours = pulse_per_3times * 4
    return f"Total pulse in 4 hours: {total_pulse_in_4hours}"


print(get_pulse())


def average_pulse(pul1, pul2, pul3):
    if pul1 > 0 and pul2 > 0 and pul3 > 0:
        total_pulse = pul1 + pul2 + pul3
        avg = total_pulse / 3
        return f"Average of three pulse per hour: {avg}"
    else:
        return None


pulse1 = pulse_per_3times
pulse2 = pulse1
pulse3 = pulse2
print(average_pulse(pulse1, pulse2, pulse3))
