import csv, pygit2
import subprocess, time, os, tempfile
from multiprocessing import Pool
from pymongo import MongoClient
from utils.clone_repo import CloneRepo
from joblib import Parallel, delayed


# Define the number of workers to use for parallel processing
NUM_WORKERS = -1

# Function to clone a Git repo, run a Java program, and parse the output
def process_repo(repo_details):
    
    
    # Clone the repo
    # subprocess.call(["git", "clone", repo_link])
    # repo_name = repo_link.split("/")[-1].split(".")[0]

    uuid,cloned_path = CloneRepo(repo_details[0], repo_details[1]).clone_repo()
    if os.path.exists(os.path.join(tempfile.gettempdir(),uuid)):
        subprocess.call(["rm","-rf",os.path.join(tempfile.gettempdir(),uuid)])
    print(cloned_path)
    
    # # Run the Java program
    
    # # Parse the output
    
    # # Update the result in MongoDB
    
    # # Clean up cloned repo

# Read the CSV file and extract the repo links
with open("/home/ip1102/Playground/multi_tp/data/input.csv", "r") as f:
    reader = csv.reader(f)
    repo_details = [(row[0],row[1]) for row in reader]
t = time.time()
# Use multiprocessing to process the repos in parallel
# with Pool(NUM_WORKERS) as p:
#     p.map(process_repo, repo_details)

#Use Joblib
Parallel(n_jobs=NUM_WORKERS)(delayed(process_repo)(repo_detail) for repo_detail in repo_details)

print(time.time()-t)

