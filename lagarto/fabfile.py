from fabric.api import *

# the user to use for the remote commands
env.user = 'wancharle'
# the servers where the commands are executed
env.hosts = ['wancharle.com.br',]

def dev():
    env.server = "wancharle.com.br"
    env.project_dir = "/home/wancharle/webapps/lagarto/"
dev()

def deploy():
    with cd(env.project_dir):
        run("git pull")
        run("apache2/bin/restart")

    
