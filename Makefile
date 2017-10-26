install_python:
    sudo add-apt-repository -y ppa:fkrull/deadsnakes
	sudo apt-get update
    sudo apt-get install -y python3.6 python3.6-dev python3.6-venv cython

local_install_fant:
    python3.6 setup.py install

pypi_install_fant:
    python3.6 -m pip install fant_sizer

venv_init:
    export XXHASH_FORCE_CFFI=1
	if [ ! -d "venv" ]; then python3.6 -m venv venv ; fi;
	bash -c "source venv/bin/activate && \
		pip install --upgrade wheel pip setuptools && \
		pip install --upgrade --requirement requirements.txt"

build:
    rm -rf build/ dist/ fant_sizer.egg-info/
    python3.6 -m pip install wheel
    python3.6 setup.py sdist bdist_wheel

pypi_upload:
    python3.6 -m pip install twine
    twine upload dist/*
