import time
import csv

def compare_functions(start, end, step, *arg):
    """Takes in * functions and a range and outputs time taken into a csv file"""
    fieldnames = []
    for func in arg:
        fieldnames.append(func.__name__)
    output = []
    filename = 'Comparison_' + time.strftime("%c") + '.csv'
    for i in range(start, end + 1, step):
        current = [i]
        for f in arg:
            f_start = time.time()
            f(i)
            f_time = time.time() - f_start
            current.append(f_time)
        output.append(current)

    csv_file = open(filename,'wb')
    writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    fieldnames.insert(0, 'Value')
    writer.writerow(fieldnames)
    for row in output:
        writer.writerow(row)                        
    return

# compare_functions(1, 100000, 2, is_prime)

