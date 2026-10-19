import os
from dotenv import load_dotenv

load_dotenv()

# add this to check whether you can access you environment variable here
print(os.environ.get("OPENAI_API_KEY"))