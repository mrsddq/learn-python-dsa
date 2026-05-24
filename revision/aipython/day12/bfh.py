# with open('bfh.txt', 'w') as f:
#     print(f.write("\nI am Laraib through file handling!"))

# with open('bfh.txt', 'a') as f:
#     print(f.write("25!"))

# with open('bfh.txt', 'r') as f:
#     print(f.read())

# import csv
# with open('bfh.csv', 'w', newline='') as f:
#     writer=csv.writer(f)
#     writer.writerow(['col1','col2'])
#     writer.writerow(['data1','data2'])

import pandas as pd
print(pd.read_csv('bfh.csv'))