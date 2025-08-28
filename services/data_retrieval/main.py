#Lib's
import uvicorn
import os

#Classes
import routs

app = routs.app

API_PORT = int(os.getenv("API_PORT",8000))

if __name__ == "__main__":
    print("Starting server...")
    uvicorn.run(app, host="0.0.0.0", port=API_PORT)