import yaml

HEADER = "# YAP_ONLY\n"

def load_contacts(path):
    with open(path, "r") as f:
        data = f.read()
        if not data.startswith(HEADER):
            raise ValueError("File not readable by this program.")
        content = yaml.safe_load(data[len(HEADER):])
    return content


def save_contacts(path, contacts):
    with open(path, "w") as f:
        f.write(HEADER)
        yaml.safe_dump(contacts, f)
