import os

def main():
    name = os.getenv("Username")
    print(f"Hello, {name} from Github!")

if __name__ == "__main__":
    main()