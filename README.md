[![Build Status](https://travis-ci.org/ripiuk/fant_sizer.svg?branch=master)](https://travis-ci.org/ripiuk/fant_sizer)
[![PyPI](https://img.shields.io/pypi/v/fant-sizer.svg)](https://pypi.python.org/pypi/fant-sizer)
[![PyPI](https://img.shields.io/pypi/l/fant-sizer.svg)](https://github.com/ripiuk/fant_sizer/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/wheel/fant-sizer.svg)](https://pypi.python.org/pypi/fant-sizer)
[![PyPI](https://img.shields.io/pypi/pyversions/fant-sizer.svg)](https://pypi.python.org/pypi/fant-sizer)
[![PyPI](https://img.shields.io/pypi/implementation/fant-sizer.svg)](https://pypi.python.org/pypi/fant-sizer)
[![PyPI](https://img.shields.io/pypi/status/fant-sizer.svg)](https://pypi.python.org/pypi/fant-sizer)
## fant-sizer
Python script, that can help recursively find files in the directory and sort them by size.
Displays sorted information about size (in bytes and megabytes) and path to files inside subdirectories.

## Latest release:
https://pypi.python.org/pypi/fant-sizer

## Getting Started
* Install python3.6 on Ubuntu 16.04:
~~~~
sudo add-apt-repository -y ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install -y python3.6 python3.6-dev python3.6-venv cython
# or
make install_python
~~~~
* Install fant-sizer
~~~
python3.6 -m pip install fant_sizer
# or
make pypi_install_fant
~~~

## Usage

* After installation, you can run this package directly in command line. Launching it without arguments starts it in interactive mode:
~~~
$ fant_sizer
~~~

### Sample output:
~~~~
Path: /home/sany/PycharmProjects
Number of files: 6657
№ |     B     |  MB   | Path
1 | 368078630 | 368.1 | /home/sany/PycharmProjects/xml_to_csv/Harrods_Google_Feed_USD_US.xml
2 | 195476333 | 195.5 | /home/sany/PycharmProjects/xml_to_csv/test.csv
3 | 188825866 | 188.8 | /home/sany/PycharmProjects/just/test.csv
4 |  40412990 |  40.4 | /home/sany/PycharmProjects/BuildingMachine/_sparsetools.cpython-36m-x86_64-linux-gnu.so
5 |  38513408 |  38.5 | /home/sany/PycharmProjects/BuildingMachine/.libs/libopenblasp-r0-39a31c03.2.18.so
~~~~
* Besides that, you can start it with arguments:
~~~
    -h, --help  show this help message and exit
    -p PATH     the path to parent dir
    -n NUMBER   how much files will be shown
    -m, --min   sort by min size
    --biggest   get information about the biggest file
    --smallest  get information about the smallest file
    --average   get the sum of the sizes divided by how many files are in the directory
    --median    get the middle value of an ordered list of sizes
    --range     get the difference between the min and max file sizes
    --mode      get file sizes repeated most often
~~~

### Sample output
~~~
$ fant_sizer -p /home/sany/PycharmProjects/some_dir -n 13 -m

Path: /home/sany/PycharmProjects/some_dir
Number of files: 45
 № |  B   | MB  | Path
 1 |    0 | 0.0 | /home/sany/PycharmProjects/some_dir/setup.cfg
 2 |    6 | 0.0 | /home/sany/PycharmProjects/some_dir/.gitignore
 3 |   10 | 0.0 | /home/sany/PycharmProjects/some_dir/runtime.txt
 4 |   23 | 0.0 | /home/sany/PycharmProjects/some_dir/.git/HEAD
 5 |   24 | 0.0 | /home/sany/PycharmProjects/some_dir/.git/COMMIT_EDITMSG
 6 |   41 | 0.0 | /home/sany/PycharmProjects/some_dir/.git/refs/heads/master
 7 |   73 | 0.0 | /home/sany/PycharmProjects/some_dir/.git/description
 8 |   92 | 0.0 | /home/sany/PycharmProjects/some_dir/.git/config
 9 |  180 | 0.0 | /home/sany/PycharmProjects/some_dir/.idea/vcs.xml
10 |  189 | 0.0 | /home/sany/PycharmProjects/some_dir/.git/hooks/post-update.sample
11 |  208 | 0.0 | /home/sany/PycharmProjects/some_dir/.idea/misc.xml
12 |  240 | 0.0 | /home/sany/PycharmProjects/some_dir/.git/info/exclude
13 |  280 | 0.0 | /home/sany/PycharmProjects/some_dir/.idea/modules.xml
~~~

## Simple example of usage inside code

~~~python
from fant_sizer import fant_sizer

dir_name = 'some_dir'

result = fant_sizer.get_sorted_files_by_size(path_to_root_dir=dir_name, debug_mode=False)
print('\n'.join(f'{path} - {size} bytes' for path, size in result))

# Getting smallest/biggest file
path_of_the_biggest_file, size_of_the_biggest_file = fant_sizer.get_the_biggest_file(dir_name)
path_of_the_smallest_file, _ = fant_sizer.get_the_smallest_file(dir_name)
print(f' {path_of_the_biggest_file} - {size_of_the_biggest_file} bytes. \n'
      f'The smallest file located in {path_of_the_smallest_file}')

# Getting average/median/range/mode of the files
average = fant_sizer.get_the_average_size_of_the_files(dir_name)
median = fant_sizer.get_median_of_the_files(dir_name)
the_range = fant_sizer.get_range_of_the_files(dir_name)
mode = fant_sizer.get_mode_of_the_files(dir_name)
print(f'Average: {average} bytes.\nMedian: {median} bytes.\n'
      f'Range: {the_range} bytes.\nMode: {mode} bytes.')     
~~~