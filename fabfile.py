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

src_dir = pc_dir

@task
def name():
  run('hostname')

@task
def pull():
  with cd(src_dir):
    run('git pull')

@task
def install():
  with cd(src_dir):
    run('npm i')

@task
def deploy():
  with cd(src_dir):
    run('npm run prod')

@task
def branch():
  with cd(src_dir):
    run('git branch')
