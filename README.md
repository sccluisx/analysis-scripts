# Analysis scripts

## For running analysis

### Install python
We recomand that you activate a virtual environement before.

```bash
sh python_install.sh
```

### Install docker
```bash
sh docker_install.sh
```

### Run docker
```bash
sh docker_run.sh
```


### Run the scripts

Run those scripts only once for initialization:

```bash
python analysis/scripts/01_init_db.py
python analysis/scripts/02_upload_geo_data.py
```

Run those scripts when you want to update database.

To upload new data:

```bash
# in case of access to API
python analysis/scripts/03_download_report.py
```

```bash
# in case of not access to API
# then ask for a sample datasets
# that you can load with this script
# the dataset should be put in:
# - backup/documents/<whatever>/<file.json>
python analysis/scripts/90_reload_db_from_json.py
```

To run analysis:

```bash
python analysis/scripts/05_script_analysis.py
```

To run export to csv:

```bash
python analysis/scripts/06_export_csv.py
```

To run export to geocoding:
```bash
# need to be done only if change in geo location
python analysis/scripts/90_export_geocoding.py
```