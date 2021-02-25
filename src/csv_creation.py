import csv
from tempfile import NamedTemporaryFile


fieldnames = [
    "Nombre",
    "Rfc",
    "SubTotal",
    "Fecha",
    "Folio",
    "Concepto 1",
    "Concepto 2",
    "Concepto 3",
]


def create_csv_file(csv_rows: list[dict[str, str]]) -> str:
    temp_file = NamedTemporaryFile()

    with open(temp_file.name, "w") as writer_file:
        writer = csv.DictWriter(writer_file, fieldnames=fieldnames)

        writer.writeheader()

        for row_dict in csv_rows:
            writer.writerow(row_dict)

    with open(temp_file.name) as reader_file:
        return reader_file.read()
