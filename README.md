<div align="center">

# 🖥️ Operating Systems Labs 5–10

### COE67-222 Operating Systems

**Sutee Onkaew · Student ID 67114264**

`Python` · `Linux` · `GitHub Codespaces` · `Operating Systems`

</div>

---

## 📌 About This Repository

This repository contains the source code and reports for Operating Systems Labs 5–10. The experiments connect OS concepts with AI and MLOps workloads, including memory allocation, CPU scheduling, dataset I/O, file security, and cluster resource management.

## 📚 Lab Contents

| Lab | Topic | Main Concepts |
|:---:|---|---|
| **05** | Memory Management | Paging, address translation, page tables, `mmap` |
| **06** | Virtual Memory | FIFO, LRU, page faults, thrashing |
| **07** | CPU Scheduling | FCFS, Round Robin, convoy effect, fairness |
| **08** | I/O Management | FCFS/SCAN disk scheduling, dataset I/O |
| **09** | File Security | Inodes, metadata, POSIX permissions |
| **10** | AI Cluster Integration | Memory, GPU locks, queues, deadlock avoidance |

## 📁 Project Structure

```text
67114264_Lab5-10/
├── lab05/                 # Paging and address translation
│   └── Lab05_Report.txt
├── lab06/                 # Page replacement and thrashing
│   └── Lab06_Report.txt
├── lab07/                 # CPU scheduling
│   └── Lab07_Report.txt
├── lab08/                 # I/O and disk scheduling
│   └── Lab08_Report.txt
├── lab09/                 # Inodes and file permissions
│   └── Lab09_Report.txt
├── lab10/                 # AI cluster OS integration
│   └── Lab10_Report.txt
└── README.md
```

## 🚀 Quick Start

Open the repository in GitHub Codespaces, then run:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install psutil
```

Run the experiments as a regular user. Lab 9 uses Linux file permissions, so do not run its scripts with `sudo`.

<details>
<summary><b>Lab 5 — Memory Management</b></summary>

```bash
cd lab05
python memory_allocation.py
python page_table_sim.py
python ai_mmap_model.py
cd ..
```

The allocation script pauses for 30 seconds. During the pause, open another terminal and inspect its PID with `top -p PID`.

</details>

<details>
<summary><b>Lab 6 — Virtual Memory and Thrashing</b></summary>

```bash
cd lab06
python page_replacement.py
python ai_thrashing.py
cd ..
```

</details>

<details>
<summary><b>Lab 7 — CPU Scheduling</b></summary>

```bash
cd lab07
python cpu_scheduler.py
python ai_inference_scheduler.py
cd ..
```

</details>

<details>
<summary><b>Lab 8 — I/O Management</b></summary>

```bash
cd lab08
python disk_scheduler.py
python ai_dataset_io.py
cd ..
```

</details>

<details>
<summary><b>Lab 9 — File Management and Security</b></summary>

```bash
cd lab09
python inode_inspector.py
python os_security.py
python ai_weight_protection.py
cd ..
```

</details>

<details>
<summary><b>Lab 10 — AI Cluster OS Integration</b></summary>

```bash
cd lab10
python ultimate_cluster_os.py
cd ..
```

</details>

## 📊 Experimental Results

| Lab | Result |
|:---:|---|
| **05** | Process RAM increased from **13.84 MB** to **90.14 MB**. Mapping the 50 MB file kept the observed RAM at **13.96 MB**. |
| **06** | FIFO produced **9 page faults**, while LRU produced **7**. The file-I/O simulation was about **3.19× slower**. |
| **07** | Average waiting time decreased from **7.33** with FCFS to **4.33** with Round Robin. |
| **08** | Disk movement decreased from **640** cylinders with FCFS to **331** with SCAN. The packed-file read was faster than 1,000 separate-file reads. |
| **09** | The tested files became read-only, and unauthorized write attempts raised `PermissionError`. |
| **10** | Training, preprocessing, and inference ran concurrently with **6/64 GB** of simulated RAM remaining. All resources returned to idle after completion. |

## 🔍 Key Findings

- LRU reduced page faults by keeping recently accessed pages in memory.
- Round Robin allowed short tasks to finish without waiting for a long task to complete.
- SCAN reduced disk-head movement by servicing requests in one direction before reversing.
- Packing a dataset into one file reduced repeated open/read/close overhead.
- Linux permissions protected configuration files and model weights from accidental writes.
- Consistent GPU lock ordering prevented circular-wait deadlocks in the cluster simulation.

## ⚠️ Experiment Notes

- The address translation, disk head, RAM, and GPU resources in the scripts are simulations.
- Lab 6 uses file I/O to demonstrate a slowdown; it does not measure actual OS swap activity.
- Lab 8 does not measure real GPU utilization.
- Lab 9 mode `444` prevents ordinary writes but still allows every user to read the file.
- Lab 10 checks whether a dataset exists; it does not perform a complete permission check.

## 📝 Reports

Each lab folder contains its own report file. The final submission combines the results and analysis for Labs 5–10 into:

```text
(ส่งแก้)67114264_Lab5-10.pdf
```

---

<div align="center">

**COE67-222 Operating Systems · Sutee Onkaew · 67114264**

</div>
