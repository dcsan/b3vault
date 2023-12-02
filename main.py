import yaml

# Load the YAML file
with open('autorepos/AutoGPT/ai_settings.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Extract the fields
ai_name = data['ai_name']
api_budget = data['api_budget']

# Create custom variables
ai_purpose = """an AI assistant specialized in doing research on a topic and building a markdown file .md"""
topic = """Cat videos"""
context = """The user is a young adult, with a passion for understanding the world mathematically"""

# Function to write back to the YAML file
def write_to_yaml(data, filename='autorepos/AutoGPT/ai_settings.yaml'):
    with open(filename, 'w') as file:
        yaml.safe_dump(data, file)

# Update the data
# data['ai_purpose'] = ai_purpose
# data['context'] = context
ai_role = ai_purpose + context
data['ai_role'] = ai_purpose + context


data['ai_goals'] = [
    "Utilize web search capabilities to gather a summary of information on the {} as it relates to {}.".format(topic, context),
    "Filter and curate into a single markdown file",
    "Add a summary and tags using '#'"
]

# Write back to the YAML file
write_to_yaml(data)

import subprocess

subprocess.call(["bash", "run_continuous.sh", '-y'], cwd="/home/lightsong/Central/Projects/hackathons/b3vault/autorepos/AutoGPT")
