

# 📄 **README.md**

```markdown
# YaP — Yet Another Phonebook  
COMP0233 Week 8 Agile Practice

## 📌 Overview
YaP (Yet another Phonebook) is a command-line application designed to load, filter, visualise, and save contact information stored in a YAML file.  
Each contact entry includes:

- `full name`
- `address`
- `birthday` (parsed as `datetime.date`)

The project was developed during a group Agile exercise using Scrum-style 10-minute sprints and GitHub Issues for task tracking.

---

## ✨ Features

### ✔ Load YAML Contacts  
- Reads YAML files containing contact entries  
- Only accepts files with the custom header `# YAP_ONLY` for security  
- Converts birthdays into Python `datetime.date` objects  

---

### ✔ Filter Functions  
Users can filter contacts based on different criteria:

| Filter | CLI Flag | Example |
|--------|----------|---------|
| Name | `--name` | `--name Alice` |
| Street (address) | `--street` | `--street Road` |
| Birth month | `--month` | `--month 04` or `--month April` |
| Limit number of results | `--limit` | `--limit 3` |

Filtering is case-insensitive and supports partial matches.

---

### ✔ Visualise Birthdays  
Displays which people have birthdays in each month.

Example output:

```

01: Ethan Chen
03: Alice Smith, Fiona Davis
04: Bob Johnson, Charlie Brown
12: Diana Lee

```

Run visualisation with:

```

python yap.py --file sample.yaml --visualize

```

This works on both the full list and filtered results.

---

### ✔ Save Filtered Results  
Filtered results can be saved back into a YAML file using:

```

python yap.py --file sample.yaml --month 04 --save april.yaml

```

Saved files automatically include the header:

```

# YAP_ONLY

```

This ensures the file is readable **only** by this program.

---

## 🚀 Usage Examples

### Load all contacts
```

python yap.py --file sample.yaml

```

### Filter by name
```

python yap.py --file sample.yaml --name Alice

```

### Filter by street
```

python yap.py --file sample.yaml --street Street

```

### Filter by birth month
```

python yap.py --file sample.yaml --month 04

```

### Limit results
```

python yap.py --file sample.yaml --limit 2

```

### Visualise birthdays
```

python yap.py --file sample.yaml --visualize

```

### Save filtered contacts
```

python yap.py --file sample.yaml --month 12 --save december.yaml

```

---

## 📂 YAML File Format

A valid YAML file must start with:

```

# YAP_ONLY

````

Example format:

```yaml
# YAP_ONLY
- full name: Alice Smith
  address: 123 London Road
  birthday: 1998-03-12
````

If the header is missing, YaP will reject the file for safety.

---

## 🧱 Project Structure

```
comp0233_week8_practice/
├── yap.py
├── utils.py
├── filters.py
├── visualize.py
├── sample.yaml
└── README.md
```

* **yap.py** – main CLI entry point
* **utils.py** – YAML loading/saving (with security header)
* **filters.py** – filtering logic
* **visualize.py** – birthday visualisation
* **sample.yaml** – example contact file

---

## 🛠 Installation

Required dependency:

```
pip install pyyaml
```

(Optional) If you add graphical plots later:

```
pip install matplotlib
```

---

## 👥 Agile Development Notes

This project was developed following Agile and Scrum principles:

* 10-minute sprint cycles
* GitHub Issues used for task management
* Each Issue included:

  * a clear description
  * acceptance criteria / Definition of Done (DoD)
  * assigned team member
* Roles included:

  * Product Owner
  * Developers
  * Testers
  * Scrum Master

The workflow included repeated cycles of planning, coding, reviewing, testing, and updating the backlog.

---

## 📜 License

This project is intended for educational use under COMP0233 at UCL.



