from loadotenv import load_env
load_env('/workspaces/fruit-classifier-mlops-class/app/.env')
import os
ORG = os.environ.get("WANDB_ORG")
print(ORG)


