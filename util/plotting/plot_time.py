import pandas as pd
import json
import re
from io import StringIO



gpu = pd.read_csv("time.csv")
gpu['args'] = gpu['args'].replace(regex=r"[^a-z^A-Z^0-9]",value="_")
cpu = pd.read_json("./util/job_launching/logfiles/node_details.maggio.23.05.08-Monday.txt").T.reset_index()
cpu.columns = ["pid", "host", "thing", "time_cpu"]
cpu2 = pd.read_csv('./util/job_launching/logfiles/sim_log.maggio.23.05.08-Monday.txt',sep=r"\s+",header=None)
cpu2.columns = ["submission_time", "pid", "bench", "args","profile","commit"]
time = pd.concat([gpu, cpu, cpu2], axis=0).reset_index()
time.drop(["index","pid","host","thing","submission_time","commit"],axis=1, inplace=True)


breakpoint()
#re.sub(r"[^a-z^A-Z^0-9]", "_", str(args).strip())



