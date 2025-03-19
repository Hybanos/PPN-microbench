from elements.bench.base import AbstractBench

import matplotlib.pyplot as plt
import numpy as np
import os

class Memory(AbstractBench):
    def __init__(self, obj, bench_obj):
        self.obj = obj
        self.bench_obj = bench_obj

    def to_html(self):
        self.gen_images()
        wd = os.getcwd()
        header = "<h2 id='Memory'>Memory</h2>"
        imgs = f"<img src='{wd}/out/cache_latency.png'/>"
        return header + imgs 

    def gen_images(self):
        # Load data
        data = self.obj
        memory_sizes = np.array(self.bench_obj["Results"][0]["Memory_Size"])
        latencies = np.array(self.bench_obj["Results"][1]["Latency"])

        # Convert to KiB
        memory_sizes_kib = memory_sizes / 1024
        
        

        # Detect closest cache sizes
        theoretical_cache_sizes = [
            data["meta"]["mem_info"]["l1d"] / 1024,
            data["meta"]["mem_info"]["l2"] / 1024,
            data["meta"]["mem_info"]["l3"] / 1024
        ]
       
        
        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.scatter(memory_sizes_kib, latencies, label='Experimental Data', color='blue')
        
        for i, (theoretical_size, label) in enumerate(zip(theoretical_cache_sizes, ['L1 Cache', 'L2 Cache', 'L3 Cache'])):
            plt.axvline(x=theoretical_size, color='green', linestyle='--', label=f'Theoretical {label} size: {theoretical_size:.1f} KiB')
            plt.text(theoretical_size, plt.ylim()[1] * 0.9, f'{label}', verticalalignment='bottom', horizontalalignment='right', color='green', fontsize=12)
        
        plt.xscale("log", base=2)
        plt.yscale("log", base=10)
        plt.xlabel("Buffer Size (KiB)")
        plt.ylabel("Latency (ns)")
        plt.title("Cache Latency")
        plt.grid(True, which="both", ls="--")
        plt.legend()

        # Save the plot
        os.makedirs("out", exist_ok=True)
        plt.savefig("out/cache_latency.png")

    def get_index(self):
        return "<li><a href='#Memory'>Memory</a></li>"
    
    
    
