
import subprocess
import os
cur_dir = 'F:\\oldboy\network_programming\ftp_task\ftp\dir\home'
proc = subprocess.Popen('cd ' + cur_dir, shell=True,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out,err) = proc.communicate()
print('out=',out,'err=',err)

proc = subprocess.Popen('dir', shell=True,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out,err) = proc.communicate()
print('out=',out.decode('gbk'),'err=',err)
# 参数bufsize：指定缓冲。我到现在还不清楚这个参数的具体含义，望各个大牛指点。
# 参数executable用于指定可执行程序。一般情况下我们通过args参数来设置所要运行的程序。如果将参数shell设为 True，executable将指定程序使用的shell。在windows平台下，默认的shell由COMSPEC环境变量来指定。
# 参数stdin, stdout, stderr分别表示程序的标准输入、输出、错误句柄。他们可以是PIPE，文件描述符或文件对象，也可以设置为None，表示从父进程继承。
# 参数preexec_fn只在Unix平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用。
# 参数Close_sfs：在windows平台下，如果close_fds被设置为True，则新创建的子进程将不会继承父进程的输入、输出、错误管 道。我们不能将close_fds设置为True同时重定向子进程的标准输入、输出与错误(stdin, stdout, stderr)。
# 如果参数shell设为true，程序将通过shell来执行。
# 参数cwd用于设置子进程的当前目录。
# 参数env是字典类型，用于指定子进程的环境变量。如果env = None，子进程的环境变量将从父进程中继承。
# 参数Universal_newlines:不同操作系统下，文本的换行符是不一样的。如：windows下用’/r/n’表示换，而Linux下用 ‘/n’。如果将此参数设置为True，Python统一把这些换行符当作’/n’来处理。
# 参数startupinfo与createionflags只在windows下用效，它们将被传递给底层的CreateProcess()94mysql函数，用 于设置子进程的一些属性，如：主窗口的外观，进程的优先级等等。
# subprocess.PIPE
# 在创建Popen对象时，subprocess.PIPE可以初始化stdin, stdout或stderr参数，表示与子进程通信的标准流。
# subprocess.STDOUT
# 创建Popen对象时，用于初始化stderr参数，表示将错误通过标准输出流输出。
# Popen的方法：
# Popen.poll()
# 用于检查子进程是否已经结束。设置并返回returncode属性。
# Popen.wait()
# 等待子进程结束。设置并返回returncode属性。
# Popen.communicate(input=None)
# 与子进程进行交互。向stdin发送数据，或从stdout和stderr中读取数据。可选参数input指定发送到子进程的参数。 Communicate()返回一个元组：(stdoutdata, stderrdata)。注意：如果希望通过进程的stdin向其发送数据，在创建Popen对象的时候，参数stdin必须被设置为PIPE。同样，如 果希望从stdout和stderr获取数据，必须将stdout和stderr设置为PIPE。
# Popen.send_signal(signal)
# 向子进程发送信号。
# Popen.terminate()
# 停止(stop)子进程。在windows平台下，该方法将调用Windows API TerminateProcess（）来结束子进程。
# Popen.kill()
# 杀死子进程。
# Popen.stdin
# 如果在创建Popen对象是，参数stdin被设置为PIPE，Popen.stdin将返回一个文件对象用于策子进程发送指令。否则返回None。
# Popen.stdout
# 如果在创建Popen对象是，参数stdout被设置为PIPE，Popen.stdout将返回一个文件对象用于策子进程发送指令。否则返回 None。
# Popen.stderr
# 如果在创建Popen对象是，参数stdout被设置为PIPE，Popen.stdout将返回一个文件对象用于策子进程发送指令。否则返回 None。
# Popen.pid
# 获取子进程的进程ID。
# Popen.returncode
# 获取进程的返回值。如果进程还没有结束，返回None。