Quick Hug 🤗: Webhooks + Buckets + Jobs

What we're gonna do:

new CSV in Bucket ──▶ Webhook ──▶ Job ──▶ Parquet in a second bucket

1. Create an output bucket
2. create a job that runs convert-to-parquet.py
3. Add a webhook on prpatel/nyc-taxi-data
4. Upload new data (new file)
5. Watch it convert to Parquet!

NOTES
* New changes on specific repositories or buckets, or to all repositories
  belonging to particular set of users/organizations
  (not just your repos, but any repo)!
* Set your token as env var HF_TOKEN
* Output goes to a different bucket, or the Job triggers itself (BAD! lol)
* Reference: https://huggingface.co/docs/hub/webhooks-guide-bucket-jobs

List the current bucket:
hf buckets ls
hf buckets ls prpatel/nyc-taxi-data -R

Create second bucket:
hf buckets create nyc-taxi-parquet --private

We're going to use this pre-build script which converts a CSV file to a Parquet
file: https://huggingface.co/datasets/uv-scripts/data-processing/raw/main/optimize-parquet.py

Run this to create the job, using this specific script
hf jobs run --flavor cpu-upgrade --timeout 2h \
    -e OUTPUT_BUCKET=prpatel/nyc-taxi-parquet \
    ghcr.io/astral-sh/uv:python3.12-bookworm \
    uv run https://huggingface.co/datasets/uv-scripts/data-processing/raw/main/optimize-parquet.py

Take jobs id:
Job 6ac54a08404719ba37662799 completed

Create the webbook/trigger
export JOB_ID=6ac54a08404719ba37662799
hf webhooks create --job-id $JOB_ID \
    --watch bucket:prpatel/nyc-taxi-data \
    --domain repo --secrets HF_TOKEN

create a new CSV file, cp it to bucket:
head -n 100001 NYC.csv > trips-2026-10-06.csv
hf buckets cp trips-2026-10-06.csv hf://buckets/prpatel/nyc-taxi-data/trips-2026-10-06.csv
hf jobs ps -a
hf jobs logs <triggered job id>


# 7. The result
hf buckets ls prpatel/nyc-taxi-parquet -R
python -c "import pandas as pd; df = pd.read_parquet('hf://buckets/prpatel/nyc-taxi-parquet/trips-2026-10-06.csv/data/train-00000-of-00001.parquet'); print(f'{len(df):,} rows'); print(df.head())"
