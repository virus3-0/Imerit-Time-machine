import subprocess

# Function to install packages from requirements.txt
def install_requirements(file_path="requirements.txt"):
    try:
        subprocess.check_call(["pip", "install", "-r", file_path])
        print("✅ All packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print("❌ Failed to install packages.")
        print(e)

# Run the function
if __name__ == "__main__":
    install_requirements()
