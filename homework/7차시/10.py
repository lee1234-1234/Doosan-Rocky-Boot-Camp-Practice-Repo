num_list = [10, 20, 30, 40, 50]
def calculate_average(num_list):
    average = sum(num_list) / len(num_list)
    return average

average = calculate_average(num_list)
print("평균: ", average)