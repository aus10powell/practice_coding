import time
import math
def main(timer_minutes=25,splits=5):
    segments = (60*timer_minutes) / splits
    print('Minute updates: {}'.format(segments/60))
    timer = 0
    for idx in range(splits):
        # print start
        if idx == 0:
            print('Starting timer')
        else:
            timer += segments
            time.sleep(timer)
            print('Elapsed time: {}'.format(timer/60))


if __name__ == '__main__':
    main(timer_minutes=25)
