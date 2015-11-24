import os


def pip_install(package):
    os.system('pip install {0}'.format(package))


def git_clone(repository):
    os.system('git clone --depth 1 {0}'.format(repository))


def install_fuel_client():
    git_clone('https://github.com/openstack/python-fuelclient')
    os.chdir('python-fuelclient')
    pip_install('-r requirements.txt')
    os.system('python setup.py install')
    os.chdir('..')


def install_fuel_devops():
    pip_install('git+https://github.com/openstack/fuel-devops.git@2.9.12 --upgrade')


def install_fuel_qa():
    git_clone('https://github.com/openstack/fuel-qa')
    os.chdir('fuel-qa')
    pip_install('-r ./fuelweb_test/requirements.txt --upgrade')
    os.chdir('..')
