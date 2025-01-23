# 1: Somatory of the first 13 numbers
def calculate_sum():
    INDICE = 13
    SOMA = 0
    K = 0
    while K < INDICE:
        K += 1
        SOMA += K
    return SOMA

# 2: Sequence Fibonacci checker
def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or num == 0

# 3: Revenue analysis 
import json

def analyze_revenue(filename):
    with open(filename) as f:
        data = json.load(f)
    
    values = [day['value'] for day in data if day['value'] > 0]
    
    min_value = min(values)
    max_value = max(values)
    avg_value = sum(values) / len(values)
    days_above_avg = sum(1 for v in values if v > avg_value)
    
    return min_value, max_value, days_above_avg

# Challenge 4: State percentage
def calculate_state_percentages():
    revenues = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }
    
    total = sum(revenues.values())
    percentages = {state: (value/total)*100 
                  for state, value in revenues.items()}
    
    return percentages

# Challenge 5: String reversal
def reverse_string(text):
    reversed_text = ''
    for i in range(len(text)-1, -1, -1):
        reversed_text += text[i]
    return reversed_text

# Main execution
if __name__ == "__main__":
    # Test Challenge 1
    print(f"Sum result: {calculate_sum()}")
    
    # Test Challenge 2
    number = 34
    print(f"Is {number} in Fibonacci? {is_fibonacci(number)}")
    
    # Test Challenge 3
    try:
        min_rev, max_rev, days = analyze_revenue('revenue.json')
        print(f"Min revenue: {min_rev}")
        print(f"Max revenue: {max_rev}")
        print(f"Days above average: {days}")
    except FileNotFoundError:
        print("Revenue data file not found")
    
    # Test Challenge 4
    percentages = calculate_state_percentages()
    for state, percentage in percentages.items():
        print(f"{state}: {percentage:.2f}%")
    
    # Test Challenge 5
    text = "Hello, World!"
    print(f"Reversed: {reverse_string(text)}")

