import pandas as pd
import pandasdmx as sdmx
import duckdb


DUCKDB_PATH = "/home/manfucci/github.com/amanfucci/sistemi-informativi/my_db.duckdb"
DF_EUSTAT = [
    "ISOC_CISCE_RA",
    "ISOC_CISCE_IC",
    "ISOC_CISCI_PRV20",
    "TIN00074",
    "TIN00085",
    "TIN00086"
]

conn = duckdb.connect(DUCKDB_PATH)
eustat_sdmx = sdmx.Request("ESTAT", log_level="DEBUG")

print("Fetching EUSTAT ICT codelists...")

for flow in DF_EUSTAT:
    print(f"Processing {flow}...")
    try:
        response = eustat_sdmx.dataflow(flow)
        dsd = next(iter(response.structure.values()))
        if not dsd:
            print("No data returned")
            continue


        for dim in dsd.dimensions.components:
            rows = []
            rep = dim.local_representation
            if rep and rep.enumerated:
                codelist = rep.enumerated
                for code in codelist:
                    rows.append({
                        "code": code.id,
                        "label_en": code.name.localized_default('en')
                    })

            df = pd.DataFrame(rows)
            table_name = dim.id.lower()
            if len(df) > 0 :
                conn.execute(f"DROP TABLE IF EXISTS {table_name}")
                conn.execute(f"CREATE TABLE {table_name} AS SELECT * FROM df")
                print(f"Loaded {len(df)} rows into {table_name}")

    except Exception as e:
        print(f"Failed {repr(e)}")

print("End")
conn.close()