import os

print(os.getcwd())
# Note the / dir seperators
# Not working in windows for some reason.
# Use linux path instead!?
# os.chdir(r'C:/Users/Richard/OneDrive/My Documents/Machine Learning')
os.chdir('/mnt/c/Users/Richard/OneDrive/My Documents/GitHubRich')
print(os.getcwd())