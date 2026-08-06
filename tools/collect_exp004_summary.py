import os
import csv

root="research_notes/experiments/exp004_full_baseline_600s"

rows=[]

for api in sorted(os.listdir(root)):
    stat=os.path.join(root,api,"stat.txt")

    if not os.path.exists(stat):
        continue

    data={}

    with open(stat) as f:
        for line in f:
            if ":" in line:
                k,v=line.strip().split(":",1)
                data[k.strip()]=v.strip()

    rows.append({
        "api":api,
        "rounds":data.get("rounds"),
        "invalid":data.get("invalid"),
        "valid":data.get("valid"),
        "validity_ratio":data.get("validity_ratio")
    })


out=os.path.join(root,"summary_by_api.csv")

with open(out,"w",newline="") as f:
    writer=csv.DictWriter(
        f,
        fieldnames=[
            "api",
            "rounds",
            "invalid",
            "valid",
            "validity_ratio"
        ]
    )
    writer.writeheader()
    writer.writerows(rows)

print(out)
