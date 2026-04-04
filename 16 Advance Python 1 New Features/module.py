def hello():
    print("Hello World!")

if __name__ == "__main__":
    hello()
    print("we are directly running the module.py")

print(__name__)
# PRINTS: __main__ [if we run module.py]
# PRINTS: module [if we run name.py]