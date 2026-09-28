import csv,statistics,sys
def analyze(path):
    rows=list(csv.DictReader(open(path,encoding="utf-8")))
    nums={k:[float(r[k]) for r in rows if r.get(k,"").strip()] for k in rows[0] if rows and all((r.get(k,"").strip().replace(".","",1).isdigit()) for r in rows)}
    print("Rows:",len(rows))
    for k,v in nums.items():
        if v: print(f"{k}: mean={statistics.mean(v):.2f} median={statistics.median(v):.2f} min={min(v):.2f} max={max(v):.2f}")
    missing={k:sum(not r.get(k,"").strip() for r in rows) for k in rows[0]}
    print("Missing:",missing)
if __name__=="__main__":analyze(sys.argv[1] if len(sys.argv)>1 else "sample.csv")
