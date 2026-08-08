import os
# print(os.name)

# print(os.environ)

# print(os.environ["TMP"])

for key, value in os.environ.items():
    print(key, "=", value)
