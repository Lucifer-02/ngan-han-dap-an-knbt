import requests
import subprocess

# data = requests.get(
#     'https://onlinecourses.uet.vnu.edu.vn/mod/quiz/review.php?attempt=210274&cmid=578&showall=1')

cmd = 'curl https: // onlinecourses.uet.vnu.edu.vn / mod / quiz / review.php?attempt = 210281 & cmid = 578 & showall = 1'
data = subprocess.check_output(cmd, shell=True)


file = open('raw_data.html', 'w')

file.write(data.text)
