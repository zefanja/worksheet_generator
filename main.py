import argparse
import json
from generator import generate_tasks
from pdf_creator import render_template
from pdf_creator import html_to_pdf

def parse_args():
    parser = argparse.ArgumentParser(description="Erzeuge Mathematik-Arbeitsblätter als PDF.")
    parser.add_argument("-t", "--template", type=str, default="simple.html",
                        help="Name of Jinja2 Template")
    parser.add_argument("-o", "--output", type=str, default="output/worksheet.pdf",
                        help="Output File")
    parser.add_argument("-r", "--number_range", type=int, choices=[10, 20, 100], default=10,
                        help="Max Value for Number Range")
    parser.add_argument("-op", "--operation", type=str, choices=["+", "-", "x", "/", "+-", "*/", "mixed"], default="mixed",
                        help="Operationen")
    parser.add_argument("-ta", "--tables", type=str, default=[],
                        help="Set Tables for Mulitplication")
    parser.add_argument("-n", "--num_tasks", type=int, default=10,
                        help="Number of Tasks")
    parser.add_argument("--ab-version", action="store_true",
                        help="Create two versions (A/B)")
    parser.add_argument("-ti", "--title", type=str,
                        help="Title for Worksheet")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    title = "Mathematik Arbeitsblatt"
    if args.title:
        title = args.title

    if args.tables:
        tables = json.loads(args.tables)
    else:
        tables = []

    if args.ab_version:
        tasks_a = generate_tasks(args.number_range, args.operation, args.num_tasks, tables)
        tasks_b = generate_tasks(args.number_range, args.operation, args.num_tasks, tables)
        # Optional: Mische Aufgabenbögen neu, solange keine Duplikate entstehen.
        context_a = {"title": title, "tasks": tasks_a, "version": "A", "school": "CDSC"}
        context_b = {"title": title, "tasks": tasks_b, "version": "B", "school": "CDSC"}
        html_a = render_template(args.template, context_a)
        html_b = render_template(args.template, context_b)
        html_to_pdf(html_a, f"{args.output.split(".pdf")[0]}_A.pdf")
        html_to_pdf(html_b, f"{args.output.split(".pdf")[0]}_B.pdf")
    else:
        tasks = generate_tasks(args.number_range, args.operation, args.num_tasks, tables)
        context = {"title": title, "tasks": tasks, "school": "CDSC"}
        html = render_template(args.template, context)
        html_to_pdf(html, args.output)