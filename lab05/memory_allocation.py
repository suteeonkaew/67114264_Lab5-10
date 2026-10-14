# memory_allocation.py
import os
import psutil
import time

def current_rss_mb():
    try:
        return psutil.Process(os.getpid()).memory_info().rss / (1024 * 1024)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        # Some containers expose a procfs namespace different from getpid().
        # Read real RSS for this process, not a simulated memory value.
        with open("/proc/self/status") as status:
            for line in status:
                if line.startswith("VmRSS:"):
                    print("[OS Monitor] RSS source: /proc/self/status (psutil fallback)")
                    return int(line.split()[1]) / 1024
        raise RuntimeError("Cannot obtain process RSS")


def print_memory_usage():
    """Fetches the actual RAM usage of this Python process from the OS"""
    mem_mb = current_rss_mb()
    print(f"[OS Monitor] Current Physical RAM Usage: {mem_mb:.2f} MB")

def main():
    print(f"--- AI Model Memory Allocation (PID: {os.getpid()}) ---")
    print_memory_usage()

    print("\nLoading a large Neural Network layer into memory...")
    # Creating a massive array of 10 million floating-point numbers
    # In Python, this requests a large continuous logical memory block from the OS
    time.sleep(2)
    ai_model_weights = [0.0] * 10_000_000 

    print("Model Loaded successfully!")
    print_memory_usage()

    # Keeping the program alive so you can inspect it
    print("\nProgram is sleeping. Open another terminal and run 'htop'")
    time.sleep(30)

if __name__ == "__main__":
    main()
