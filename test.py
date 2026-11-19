#!/usr/bin/env python3
import os
import statistics

def main():
    print("=" * 50)
    print("DATA ANALYSIS RUNNING IN KUBERNETES")
    print("=" * 50)
    
    # Sample dataset
    data = [23, 45, 12, 67, 34, 89, 56, 78, 91, 43]
    
    print(f"\nDataset: {data}")
    print(f"Count: {len(data)}")
    print(f"Mean: {statistics.mean(data):.2f}")
    print(f"Median: {statistics.median(data):.2f}")
    print(f"Std Dev: {statistics.stdev(data):.2f}")
    print(f"Min: {min(data)}, Max: {max(data)}")
    
    # Pod information
    hostname = os.getenv('HOSTNAME', 'unknown')
    print(f"\nRunning on pod: {hostname}")
    print("=" * 50)

if __name__ == "__main__":
    main()