from utils import load_contacts, save_contacts
from filters import filter_by_name, filter_by_street, filter_by_month, limit_results
from visualize import visualize_birthdays
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file")
parser.add_argument("--name")
parser.add_argument("--street")
parser.add_argument("--month")
parser.add_argument("--limit")
parser.add_argument("--save")
parser.add_argument("--visualize", action="store_true")
args = parser.parse_args()

contacts = load_contacts(args.file)

if args.name:
    contacts = filter_by_name(contacts, args.name)

if args.street:
    contacts = filter_by_street(contacts, args.street)

if args.month:
    contacts = filter_by_month(contacts, args.month)

if args.limit:
    contacts = limit_results(contacts, int(args.limit))

print(contacts)   # 可保留

if args.visualize:
    visualize_birthdays(contacts)

if args.save:
    save_contacts(args.save, contacts)
    print(f"Saved to {args.save}")


