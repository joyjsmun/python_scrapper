from indeed import get_jobs as get_indeed_jobs
from st import get_jobs as get_st_jobs

indeed_jobs = get_indeed_jobs()
st_jobs = get_st_jobs()

jobs = st_jobs + indeed_jobs








