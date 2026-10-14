Operating Systems Labs 5–10
Course: COE67-222 Operating Systems
Name: Sutee Onkaew
Student ID: 67114264
Environment: GitHub Codespaces (Linux), Python
Overview
This repository contains Python experiments and reports covering memory management, CPU scheduling, disk I/O, file security, and a simulated AI cluster orchestrator.
Folder	Topic	Report
lab05	Paging, address translation, and memory-mapped files	Lab05_Report.txt
lab06	FIFO, LRU, and a thrashing simulation	Lab06_Report.txt
lab07	FCFS, Round Robin, and inference request scheduling	Lab07_Report.txt
lab08	Disk scheduling and dataset I/O	Lab08_Report.txt
lab09	Inodes and file permissions	Lab09_Report.txt
lab10	AI cluster OS integration	Lab10_Report.txt


Setup
Open the repository in GitHub Codespaces. From the repository root, create a virtual environment and install the dependency:
python -m venv .venv
source .venv/bin/activate
python -m pip install psutil
Activate .venv again when opening a new terminal. Run the experiments as a normal user without sudo, especially for the file-permission tests.
Run the Experiments
Run these commands in order, starting from the repository root:
# Lab 5
cd lab05
python memory_allocation.py
python page_table_sim.py
python ai_mmap_model.py
cd ..

# Lab 6
cd lab06
python page_replacement.py
python ai_thrashing.py
cd ..

# Lab 7
cd lab07
python cpu_scheduler.py
python ai_inference_scheduler.py
cd ..

# Lab 8
cd lab08
python disk_scheduler.py
python ai_dataset_io.py
cd ..

# Lab 9
cd lab09
python inode_inspector.py
python os_security.py
python ai_weight_protection.py
cd ..

# Lab 10
cd lab10
python ultimate_cluster_os.py
cd ..
Lab 5 pauses for 30 seconds after allocation. During this pause, another terminal can inspect the printed PID using top -p PID, replacing PID with the process number.
Observed Results
The following values were recorded from my Codespaces runs. Timing, memory usage, and inode numbers may differ between runs.
Lab	Recorded result
5	Allocation RSS increased from 13.84 MB to 90.14 MB. RSS before and after mapping the 50 MB file was 13.96 MB; the accessed byte was 0.
6	FIFO: 9 faults; LRU: 7 faults. RAM processing: 0.4492 s; file-based processing: 1.4319 s, approximately 3.19× longer.
7	FCFS average waiting/turnaround: 7.33 / 12.33 units. RR with quantum 3: 4.33 / 9.33 units. The short inference request finished first under RR.
8	FCFS/SCAN head movement: 640 / 331 cylinders. Reading 1,000 files: 0.0232 s; reading one packed file: 0.0016 s.
9	Dataset inode: 1442922; size: 43 bytes; initial mode: 666. Both protected-file write attempts were denied.
10	A, B, and C overlapped using 58/64 GB of simulated RAM. A used GPUs 0–2, B used no GPUs, and C used GPU 3. D was rejected, and all resources were released at shutdown.


Interpretation Notes
- Address translation, disk head movement, and cluster resources are simulations. Lab 10 does not allocate real GPUs or 64 GB of RAM.
- Lab 6 uses file I/O to illustrate slowdown; it does not measure actual OS swapping. Lab 8 compares many-file and packed-file reads, not a controlled randomized-seek benchmark.
- Lab 5 did not measure RSS after accessing the mapped byte. Lab 7 did not measure TTFT, and Lab 8 did not measure GPU utilization.
- Lab 9's printed Created On field uses Linux st_ctime, which is metadata-change time. The rename behavior has not yet been experimentally checked.
- Mode 444 allows everyone to read but denies ordinary writes. Read confidentiality requires suitable ownership and permissions.
- Lab 10 checks file existence, not actual read permission. Workload D references a missing file; its job dispatch queue is not a Round Robin scheduler.
Reports and Submission
Keep terminal output or screenshots as evidence. Record results and explain observations in the corresponding report files using your own words. Combine the results and analysis for Labs 5–10 into one PDF named:
67114264_Lab5-10.pdf