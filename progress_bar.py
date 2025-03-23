from tqdm import tqdm
import time

# Simulate a download
for i in tqdm(range(100), desc="Downloading..."):
    time.sleep(0.05)  # Simulates time delay
