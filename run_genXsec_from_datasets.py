#!/usr/bin/env python3

import argparse
import subprocess
import os
import shlex

def get_first_file(dataset):
    """Query DAS and return the first valid file for the dataset."""
    try:
        cmd = f'dasgoclient --query="file dataset={dataset} status=valid"'
        output = subprocess.check_output(shlex.split(cmd), universal_newlines=True)
        files = [line.strip() for line in output.strip().split('\n') if line.strip()]
        if not files:
            print(f"[WARNING] No files found for {dataset}")
            return None
        return files[0]
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] DAS query failed for {dataset}: {e}")
        return None

def sanitize_filename(name):
    return name.strip('/').replace('/', '__')

def main():
    parser = argparse.ArgumentParser(description="Run genXsec on datasets from a file")
    parser.add_argument('-f', '--filelist', required=True, help='Path to text file with dataset names (one per line)')
    parser.add_argument('-n', '--events', required=True, type=int, help='Number of events for each run')
    args = parser.parse_args()

    if not os.path.isfile(args.filelist):
        print(f"[ERROR] File {args.filelist} not found.")
        return

    with open(args.filelist) as f:
        datasets = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]

    for dataset in datasets:
        print(f"\n[INFO] Processing dataset: {dataset}")
        first_file = get_first_file(dataset)
        if first_file:
            sanitized_name = sanitize_filename(dataset)
            log_file = f"xsec_{sanitized_name}.log"
            remote_file = f"root://cms-xrd-global.cern.ch/{first_file}"
            cmd = f'cmsRun genXsec_cfg.py inputFiles={remote_file} maxEvents={args.events} 2>&1 | tee {log_file}'
            print(f"[INFO] Running: {cmd}")
            subprocess.run(cmd, shell=True)
        else:
            print(f"[WARNING] Skipping dataset {dataset} due to missing files.")

if __name__ == "__main__":
    main()
