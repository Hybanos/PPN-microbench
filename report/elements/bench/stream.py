from elements.bench.base import AbstractBench

import matplotlib.pyplot as plt
import numpy as np
import os

class Stream(AbstractBench):
    def __init__(self, obj, bench_obj):
        self.obj = obj
        self.bench_obj = bench_obj

    def to_html(self):
        self.gen_images()
        wd = os.getcwd()
        header = "<h2 id='STREAM'>Stream</h2>"
        imgs = f"<img src='{wd}/out/stream.svg'/>"
        p = f"<p>Stream-like benchmark, kernels are the following:</p>"
        ul = f"""<ul>
            <li>Copy: <span class="code-block">c[i] = a[i]</span></li>
            <li>Multiply: <span class="code-block">c[i] = alpha * a[i]</span></li>
            <li>Add: <span class="code-block">c[i] = a[i] + b[i]</span></li>
            <li>Tirad: <span class="code-block">c[i] = alpha * a[i] + b[i]</span></li>
        </ul>"""
        return header + imgs + p + ul

    def gen_images(self):
        stream_data = {
            "copy": self.bench_obj["copy"],
            "multiply": self.bench_obj["mul"],
            "add": self.bench_obj["add"],
            "triad": self.bench_obj["triad"],
        }

        fmts = ["-o", "-x", "-s", "-^"]

        sizes = np.array([2**i for i in range(27, 10, -1)])

        def compute_stats(data):
            arr = sizes / np.array(data)
            mean = np.mean(arr, axis=0)
            std = np.std(arr, axis=0)
            return mean, std

        plt.figure(figsize=(12, 6))

        i = 0
        for label, data in stream_data.items():
            mean, std = compute_stats(data)
            plt.errorbar(sizes / 1024, mean, yerr=std, label=label.capitalize(), capsize=4, fmt=fmts[i], alpha=0.7)
            i += 1

        plt.title("Stream bandwidth")
        plt.xlabel("Buffer size (KiB)")
        plt.ylabel("Bandwidth (GiB/s)")
        plt.xscale("log", base=2)
        plt.ylim(0)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("out/stream.svg")

    def get_index(self):
        return "<li><a href='#STREAM'>Stream</a></li>"


