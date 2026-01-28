import pandasdmx as sdmx

# Configuration
DF_ISTAT = "istat_dataflows.temp"
DF_EUSTAT = "eustat_dataflows.temp"

# ISTAT
try:
    istat_sdmx = sdmx.Request('ISTAT')
    istat_dataflows = istat_sdmx.dataflow()
    with open(DF_ISTAT, "w", encoding="utf-8") as out:
        for df_id, df in istat_dataflows.dataflow.items():
            out.write(f"{df_id}\t{df.name['en']}\n")
except:
    print("Failed istat")

# EUSTAT
try:
    eustat_sdmx = sdmx.Request('ESTAT')
    eustat_dataflows = eustat_sdmx.dataflow()
    with open(DF_EUSTAT, "w", encoding="utf-8") as out:
        for df_id, df in eustat_dataflows.dataflow.items():
            out.write(f"{df_id}\t{df.name['en']}\n")
except:
    print("Failed eustat")

print("End")