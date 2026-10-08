# simple-buckets-demo

Demo code and notes for my Hugging Face Storage Buckets videos.

| File | What it's for |
|---|---|
| `webhooks-jobs-buckets-demo.md` | Quick Hug: Webhooks + Buckets + Jobs. Commands to have a bucket webhook start a Job that converts each new CSV to Parquet in a second bucket. |
| `convert_to_parquet.py` | Converts `NYC.csv` to `NYC.parquet` with PyArrow. |
| `prepend_parquet.py` | Prepends new rows to `NYC.parquet`, writing with `use_content_defined_chunking=True` so Xet re-uploads only what changed. |

## Data

The data is the [NYC Taxi Trip Duration](https://www.kaggle.com/c/nyc-taxi-trip-duration) dataset from Kaggle, saved as `NYC.csv` (~191 MB). It isn't in this repo; download it from Kaggle.

## Links

- [Hands-on with Buckets](https://huggingface.co/blog/prpatel/hands-on-with-buckets)
- [Webhooks guide: bucket to Jobs](https://huggingface.co/docs/hub/webhooks-guide-bucket-jobs)
