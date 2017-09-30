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

src_dir = (env.p or pc_dir) and h5_dir

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
def log():
  with cd(src_dir):
    run('pm2 logs yohobuy-node')
