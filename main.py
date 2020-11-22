from indeed import get_jobs as get_indeed_jobs
from st import get_jobs as get_st_jobs
from save import save_to_file

indeed_jobs = get_indeed_jobs()
st_jobs = get_st_jobs()

jobs = st_jobs + indeed_jobs
save_to_file(jobs)









