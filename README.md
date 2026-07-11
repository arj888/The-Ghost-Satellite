# The Ghost Satellite

I wanted to see if a space defense tracking system could run on a phone with zero graphics. So I built this. 

It is a text-based satellite monitoring tool built with Python on Google Colab. It pulls live space data, checks boundaries, and uses AI for security profiling.

## 🚀 How to Run (Quick Start)

Copy and paste these commands into any Google Colab notebook to run the system instantly:

```python
# Step 1: Install the secure package directly from GitHub
!pip install git+[https://github.com/arj888/The-Ghost-Satellite.git](https://github.com/arj888/The-Ghost-Satellite.git) -q

# Step 2: Import and fire up the defense core
import ghost_satellite
ghost_satellite.run_defense_core()

