#!/usr/bin/env python

import argparse
import os

from install import install_fuel_client
from install import install_fuel_devops
from install import install_fuel_qa


parser = argparse.ArgumentParser(description='fuel virtual environment')
parser.add_argument('name', help='Environment name')
parser.add_argument('-iso', '--iso', help='ISO-file')

args = parser.parse_args()

virtual_env_dir = os.path.join(os.getcwd(), args.name)

print 'Name: {0}'.format(args.name)

os.system('virtualenv {0}'.format(args.name))

activate_this = os.path.join(virtual_env_dir, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

os.chdir(virtual_env_dir)

install_fuel_devops()
install_fuel_qa()
install_fuel_client()

# build iso

os.environ['ISO_PATH'] = args.iso
os.environ['NODES_COUNT'] = '4'
os.environ['ENV_NAME'] = args.name
os.environ['VENV_PATH'] = virtual_env_dir

os.chdir('fuel-qa')

os.system('./utils/jenkins/system_tests.sh -t test -w {0} -j fuelweb_test'
          ' -i {1} -o --group=setup'.format(os.getcwd(), args.iso))
