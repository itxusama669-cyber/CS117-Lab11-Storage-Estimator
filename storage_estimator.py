# Storage Estimator
# Estimates storage usage in megabytes and gigabytes.

def main():
    try:
        size_mb = float(input("Enter file size in megabytes (MB): "))

        if size_mb < 0:
            print("File size cannot be negative.")
            return

        size_gb = size_mb / 1024

        print("\nStorage Estimate")
        print(f"File size: {size_mb:.2f} MB")
        print(f"File size: {size_gb:.4f} GB")

    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
