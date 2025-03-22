import random

def generate_task(number_range, operation, tables=[]):
    operation_symbol = operation
    if operation == "mixed":
        operation = random.choice(["+", "-", "x", "/"])
        operation_symbol = operation
    if operation == "+":
        a = random.randint(1, number_range-1)
        b = random.randint(1, number_range-a)
        result = a + b
    elif operation == "-":
        a = random.randint(1, number_range)
        b = random.randint(1, a)
        result = a - b
    elif operation == "x":
        if len(tables) > 0:
            a = random.choice(tables)
        else:
            a = random.randint(1, number_range)
        b = random.randint(1, number_range)
        result = a * b
        operation_symbol = "·"
    elif operation == "/":
        b = random.randint(1, number_range)
        result = random.randint(1, number_range)
        a = b * result
        operation_symbol = ":"
    else:
        raise ValueError("Unknown Operation")

    return {"operand1": a, "operand2": b, "operator": operation, "symbol": operation_symbol, "result": result}

def generate_tasks(number_range, operation, num_tasks, tables=[]):
    tasks = []
    seen = set()
    counter = 0

    while len(tasks) < num_tasks and counter < 100:
        task = generate_task(number_range, operation, tables)

        key = (task["operand1"], task["operand2"], task["operator"])
        if key in seen:
            counter += 1
            continue
        seen.add(key)
        tasks.append(task)

    return tasks
