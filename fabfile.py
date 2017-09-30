from fabric.api import *

env.user = 'root'
env.password = '123456'
env.hosts = [
  '192.168.104.37',
  '192.168.104.50',
  '192.168.104.65',
  '192.168.104.73',
  '192.168.104.77',
  '192.168.104.78',
  '192.168.104.82',
]

pc_dir = '/home/test/yohobuy-node'
h5_dir = '/home/test/yohobuywap-node'

pc_app = 'yohobuy-node'
h5_app = 'yohobuywap-node'

src_dir = h5_dir if env.has_key('p') else pc_dir
app = h5_app if env.has_key('p') else pc_app

@task
@parallel
def name():
  run('hostname')

@task
@parallel
def pull():
  with cd(src_dir):
    run('git pull')

@task
@parallel
def install():
  with cd(src_dir):
    run('npm i')

@task
@parallel
def deploy():
  with cd(src_dir):
    run('npm run prod')

@task
@parallel
def branch():
  with cd(src_dir):
    run('git branch')

@task
@parallel
def fetch():
  with cd(src_dir):
    run('git fetch -p')

@task
@parallel
def checkout():
  with cd(src_dir):
    run('git checkout feature/qps')

@task
@parallel
def start():
  with cd(src_dir):
    run('pm2 start process.json')

@task
# @parallel
def list():
  with cd(src_dir):
    run('pm2 list')

@task
@parallel
def log():
  with cd(src_dir):
    run('pm2 logs %s' % (app))
