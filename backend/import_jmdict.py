from __future__ import annotations

import json
import sqlite3
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def text_values(parent: ET.Element, path: str) -> list[str]:
    return [node.text for node in parent.findall(path) if node.text]


def import_jmdict(xml_path: Path, db_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(db_path)
    conn.execute("pragma journal_mode=wal")
    conn.execute(
        """
        create table entries (
            id integer primary key,
            expression text not null,
            reading text not null,
            glosses text not null
        )
        """
    )
    conn.execute("create table lookup (term text not null, entry_id integer not null)")
    conn.execute("create index lookup_term_idx on lookup(term)")

    count = 0
    for _, elem in ET.iterparse(xml_path, events=("end",)):
        if elem.tag != "entry":
            continue

        expressions = text_values(elem, "k_ele/keb")
        readings = text_values(elem, "r_ele/reb")
        glosses = text_values(elem, "sense/gloss")
        if not glosses:
            elem.clear()
            continue

        primary_expression = expressions[0] if expressions else readings[0]
        primary_reading = readings[0] if readings else ""
        cursor = conn.execute(
            "insert into entries(expression, reading, glosses) values (?, ?, ?)",
            (primary_expression, primary_reading, json.dumps(glosses[:12], ensure_ascii=False)),
        )
        entry_id = cursor.lastrowid
        for term in set(expressions + readings):
            conn.execute("insert into lookup(term, entry_id) values (?, ?)", (term, entry_id))

        count += 1
        if count % 5000 == 0:
            conn.commit()
            print(f"imported {count} entries")
        elem.clear()

    conn.commit()
    conn.close()
    print(f"done: imported {count} entries into {db_path}")


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: python import_jmdict.py path/to/JMdict_e.xml data/jmdict.sqlite")
        return 2
    import_jmdict(Path(sys.argv[1]), Path(sys.argv[2]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
