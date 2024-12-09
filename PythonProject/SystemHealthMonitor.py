import psutil
import logging
import time

# Set logging configuration
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
    handlers=[
        logging.StreamHandler(),  # Output to console
        logging.FileHandler("system_health.log")  # Log to file
    ]
)

# Thresholds for alerts
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90

# Check CPU usage
def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    logging.info(f"CPU Usage: {cpu_usage}%")
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU Usage: {cpu_usage}% exceeds threshold!")

# Check memory usage
def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    logging.info(f"Memory Usage: {memory_usage}%")
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High Memory Usage: {memory_usage}% exceeds threshold!")

# Check disk usage
def check_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    logging.info(f"Disk Usage: {disk_usage}%")
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"High Disk Usage: {disk_usage}% exceeds threshold!")

# Check running processes
def check_running_processes():
    processes = [proc.info for proc in psutil.process_iter(['pid', 'name', 'cpu_percent'])]
    logging.info(f"Running Processes: {len(processes)}")
    for proc in processes[:5]:  # Display the first 5 processes
        logging.info(f"PID: {proc['pid']} - Process: {proc['name']} - CPU Usage: {proc['cpu_percent']}%")

# Main function to monitor system health
def monitor_system():
    while True:
        check_cpu_usage()
        check_memory_usage()
        check_disk_usage()
        check_running_processes()
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    logging.info("System Health Monitoring Started")
    monitor_system()
