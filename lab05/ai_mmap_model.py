# ai_mmap_model.py
import mmap
import os
import psutil

def current_rss_mb():
    try:
        return psutil.Process(os.getpid()).memory_info().rss / (1024 * 1024)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        # Container-compatible reading of actual process resident memory.
        with open("/proc/self/status") as status:
            for line in status:
                if line.startswith("VmRSS:"):
                    print("[OS Monitor] RSS source: /proc/self/status (psutil fallback)")
                    return int(line.split()[1]) / 1024
        raise RuntimeError("Cannot obtain process RSS")


def print_memory():
    print(f"[OS Monitor] Physical RAM Usage: {current_rss_mb():.2f} MB")

def main():
    file_path = "fake_llm_weights.bin"

    # 1. Create a fake 50MB model weight file on the hard drive
    print("Creating a 50MB fake LLM file on Disk...")
    with open(file_path, "wb") as f:
        f.write(b'\x00' * (50 * 1024 * 1024))

    print_memory()

    # 2. Use OS mmap to map the file to Virtual Memory (Page Table)
    print("\nMapping the 50MB file into Virtual Memory...")
    with open(file_path, "r+b") as f:
        # We map it, but the OS doesn't load it into physical RAM yet!
        mm = mmap.mmap(f.fileno(), 0)
        print_memory()

        # 3. Triggering a Page Fault
        print("\nAccessing weight at index 25,000,000 (Triggers OS Page Fault)...")

        weight = mm[25000000]
        print(f"Weight value accessed successfully: {weight}")

        mm.close()

    os.remove(file_path) # Cleanup

if __name__ == "__main__":
    main()
