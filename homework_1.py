
def total_salary(path):
    try:
        with open(path, 'r') as file:
            total = 0
            count = 0
            for line in file:
                parts = line.split(',') 
                salary = parts[1]
                salary = int(salary)
                total += salary
                count += 1
            average = total // count 
            return total, average         
    except FileNotFoundError:
        print('file not found')
        
total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

                
                
                
                