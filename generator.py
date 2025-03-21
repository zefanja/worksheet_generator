import random

def generate_task(zahlenraum, operation):
    if operation == "gemischt":
        operation = random.choice(["+", "-", "x", "/"])
    if operation == "+":
        a = random.randint(1, zahlenraum)
        b = random.randint(1, zahlenraum)
        result = a + b
    elif operation == "-":
        a = random.randint(1, zahlenraum)
        b = random.randint(1, a)  # Damit das Ergebnis nicht negativ wird
        result = a - b
    elif operation == "x":
        a = random.randint(1, zahlenraum)
        b = random.randint(1, zahlenraum)
        result = a * b
    elif operation == "/":
        b = random.randint(1, zahlenraum)
        result = random.randint(1, zahlenraum)
        a = b * result
    else:
        raise ValueError("Unbekannte Operation")

    return {"operand1": a, "operand2": b, "operator": operation, "result": result}

def generate_tasks(zahlenraum, operation, num_tasks):
    tasks = []
    seen = set()
    while len(tasks) < num_tasks:
        task = generate_task(zahlenraum, operation)
        # Erzeuge eine kanonische Darstellung (z.B. bei Addition/Tausch)
        key = (min(task["operand1"], task["operand2"]),
               max(task["operand1"], task["operand2"]),
               task["operator"])
        if key in seen:
            continue
        seen.add(key)
        tasks.append(task)
    return tasks
