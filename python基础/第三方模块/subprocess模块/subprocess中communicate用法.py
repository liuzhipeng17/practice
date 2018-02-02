import subprocess

proc = subprocess.Popen(...)
try:
    outs, errs = proc.communicate(timeout=15)
except subprocess.TimeoutExpired:
    proc.kill()
    outs, errs = proc.communicate() # 仍然要设置stdout= PIPE等

# Note The data read is buffered in memory,
# so do not use this method if the data size is large or unlimited