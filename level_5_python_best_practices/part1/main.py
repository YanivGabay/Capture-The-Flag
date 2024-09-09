import env

def main():
    
    print(f"Running in {env.ENV} environment")
    print(f"This is the endpoint: {env.ENDPOINT}")


    if (env.ENV == "development"):
        print("Do not run this in production!")
    if (env.ENV == "production"):
        print("You are running in production. Be careful!")