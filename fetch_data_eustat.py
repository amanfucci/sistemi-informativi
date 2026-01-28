import pandasdmx as sdmx
import duckdb

# Configuration
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
eustat_sdmx = sdmx.Request('ESTAT')

print("Fetching EUSTAT ICT datasets...\n")

for flow in DF_EUSTAT:
    print(f"Processing {flow}...")
    try:
        response = eustat_sdmx.data(flow)
        df = response.to_pandas()
        if df.empty:
            print(f"No data returned")
            continue
        df = df.reset_index()
        table_name = flow.lower()
        conn.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df")
        print(f"Loaded {len(df)} rows into {table_name}")
    except:
        print("Failed")

print("End")
conn.close()