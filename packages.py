import subprocess
import sys

# List of libraries to install
libraries = [
    "matplotlib",
    "pandas",
    "numpy",
    "scipy",
    "sympy"
]

# Function to install a package using pip
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install each library
for library in libraries:
    install(library)

print("All libraries installed successfully!")
