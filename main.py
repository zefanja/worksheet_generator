import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Erzeuge Mathematik-Arbeitsblätter als PDF.")
    parser.add_argument("-t", "--template", type=str, default="simple.html",
                        help="Name des Jinja2 Templates")
    parser.add_argument("-o", "--output", type=str, default="worksheet.pdf",
                        help="Pfad zur Ausgabedatei")
    parser.add_argument("-z", "--zahlenraum", type=int, choices=[10, 20, 100], default=10,
                        help="Maximalwert im Zahlenraum")
    parser.add_argument("-op", "--operation", type=str, choices=["+", "-", "x", "/", "gemischt", "+/-", "*/"], default="gemischt",
                        help="Rechenoperationen")
    parser.add_argument("-n", "--num_tasks", type=int, default=10,
                        help="Anzahl der Aufgaben")
    parser.add_argument("--ab-version", action="store_true",
                        help="Erzeuge zwei verschiedene Versionen (A/B)")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    # Hier kann dann die Logik zum Erzeugen der Aufgaben aufgerufen werden
    print(args)

    if args.ab_version:
        tasks_a = generate_tasks(args.zahlenraum, args.operation, args.num_tasks)
        tasks_b = generate_tasks(args.zahlenraum, args.operation, args.num_tasks)
        # Optional: Mische Aufgabenbögen neu, solange keine Duplikate entstehen.
        context_a = {"title": "Mathematik Arbeitsblatt", "tasks": tasks_a, "version": "A"}
        context_b = {"title": "Mathematik Arbeitsblatt", "tasks": tasks_b, "version": "B"}
        html_a = render_template(args.template, context_a)
        html_b = render_template(args.template, context_b)
        html_to_pdf(html_a, "worksheet_A.pdf")
        html_to_pdf(html_b, "worksheet_B.pdf")
    else:
        tasks = generate_tasks(args.zahlenraum, args.operation, args.num_tasks)
        context = {"title": "Mathematik Arbeitsblatt", "tasks": tasks, "version": "A"}
        html = render_template(args.template, context)
        html_to_pdf(html, args.output)