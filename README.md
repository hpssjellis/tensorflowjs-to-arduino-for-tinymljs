# tensorflowjs-to-arduino-for-tinymljs



# install on your own Linux (Ubuntu) machine.
Not presently working on windows, hopefully that changes.

## The steps   (Suppossedly)


1. Go to the location you downloaded the model .json and model.bin files from https://hpssjellis.github.io/tinyMLjs/public/index.html
2. Instal venv  ```sudo apt install python3.12-venv```    so you can work in an environment and not have other things mess it up
3. Install a virtual environment  ```python3 -m venv myenv10```
4. Activate that environment (note it has a folder you can stay out of )  ```source myenv10/bin/activate``` or on windows ```myenv10\scripts\activate```
5. ```pip install tensorflow```
6. ```pip install tensorflowjs```
7. ```pip install tensorRT```
8. ```tflite_convert --help```
9. ```tensorflowjs_converter --help```
10.```tensorflowjs_converter --input_format=tfjs_layers_model --output_format=keras_saved_model ./model.json ./```  Convert tfjs file to keras
11. ```tflite_convert --keras_model_file ./ --output_file ./model.tflite```   Convert Keras file to tflite file
12. ```xxd -i model.tflite model.h``` Convert tflite file to a c-header file (This needs xxd installed, several ways to do this also can do it from a web page) 


Non of the above work for me that is why I have the other options


1. use python notebooks  https://colab.research.google.com/drive/1OgCcKhklL3EH_SdWHdtlb5dbtYvjGQnn?usp=sharing   (run both sketches then upload your files and run the last sketch again)
2. This repo  https://github.com/hpssjellis/Gitpod-auto-tensorflowJS-to-arduino  and run the gitpod which has a file that does the conversions. Basically it installs the above and then you can run the commands or a bash file I have ready to do the conversions for you. The autoloading gitpod is here https://gitpod.io/#github.com/hpssjellis/Gitpod-auto-tensorflowJS-to-arduino
.


.




.


# The old stuff


This github repository is at   https://github.com/hpssjellis/tensorflowjs-to-arduino-for-tinymljs

if you want to load it as a Gitpod click  https://gitpod.io/#github.com/hpssjellis/tensorflowjs-to-arduino-for-tinymljs


Click the above link to load the gitpod (docker in the browser) which installs all needed files

You can use the test-with folder to drag a ```model.json``` file with it's shard .bin file ```model.weights.bin``` to the main folder

Look at the code in the ```a01-convert-tfjs-arduino.sh```  and then run it

Then run ```./a01-convert-tfjs-arduino.sh```  


Gotchas   When making your own files the ````model.json```` file is made with a link to the ```model.weights.bin``` file, if you change the name of the binary file the model.json fle will not link to it properly




## Install on a local machines
### DRAFT Instructions

I assume python is installed probably best to have Python3 installed.

```
pip install tensorflowjs

python -m site --user-base
```

to the above reply add
```
\bin\tensorflowjs_converter -h
```
Then run the commands for your files which are in the a01-convert-tfjs-arduino.sh bash file

```
tensorflowjs_converter --input_format=tfjs_layers_model --output_format=keras_saved_model ./model.json ./


tflite_convert --keras_model_file ./ --output_file ./model.tflite


xxd -i model.tflite model.h

```

Then you can load your model.tflite file onto the https://netron.app/ website to visualize it and then add the model.h file into your arduino machine learning code as it;s own include file.

See the Arduino ready library at   https://github.com/hpssjellis/RocksettaTinyML download the zip file and install it into the arduino ide using the normal zip file libary upload method.
sketch --> include library --> add .zip file


Note: If the above commands don't work you can always try the python code below.

1. convert from tensorflowJS to Keras

```
import tensorflowjs as tfjs

# Define the paths
input_format = "tfjs_layers_model"
output_format = "keras_saved_model"
input_model_json = "./model.json"
output_dir = "./"

# Convert the model
tfjs.converters.save_keras_model(input_model_json, output_dir, input_format, output_format)

```

2. Then use tensorflow lite converter to convert the Keras file into tensorflow Lite (TFLITE)

3.
```
   import tensorflow as tf

# Define the paths
keras_model_file = "./model"  # Make sure the model file has the .h5 extension
output_file = "./model.tflite"

# Convert the model to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model_file(keras_model_file)
tflite_model = converter.convert()

# Save the TensorFlow Lite model to a file
with open(output_file, 'wb') as f:
    f.write(tflite_model)
```


If you have install ability then install the xxd application   
```
sudo apt-get install xxd
```

and run the command

```
xxd -i model.tflite model.h
```

If you don't have admin access you can try using the online xxd -1 utility here https://hpssjellis.github.io/tinyMLjs/public/convert/xxd-i.html

Upload your tFLITE file and get the web to convert it into a c-header model.h file ready to run on a micro-controler with an appropriate sketch.






# May 2024 trying to update. so far


python.exe -m pip install --upgrade pip

pip3 install --upgrade pip

python -m venv myenv2

myenv2\scripts\activate

pip3 install tensorflowjs

pip3 install tensorflow==2.15.0

pip3 install tensorflow-hub

pip3 install netron    "dask[delayed]"


$env:TF_ENABLE_ONEDNN_OPTS=0


tflite_convert --help
tensorflowjs_converter --help

xxd --help


https://sourceforge.net/projects/xxd-for-windows/


in power shell try    
Format-Hex '.\your-file-name'





this set works


```
pip list
--------------------------------- ---------
absl-py                           2.1.0
argon2-cffi                       21.1.0
astroid                           2.7.3
astunparse                        1.6.3
attrs                             21.2.0
autopep8                          1.5.7
backcall                          0.2.0
backports.entry-points-selectable 1.1.0
bandit                            1.7.0
bleach                            4.1.0
cached-property                   1.5.2
cachetools                        5.3.3
certifi                           2021.5.30
cffi                              1.14.6
charset-normalizer                2.0.4
chex                              0.1.7
click                             8.1.7
cloudpickle                       3.0.0
colorama                          0.4.4
cryptography                      3.4.8
dask                              2023.5.0
debugpy                           1.4.3
decorator                         5.1.0
defusedxml                        0.7.1
distlib                           0.3.2
dm-tree                           0.1.8
docutils                          0.17.1
entrypoints                       0.3
etils                             1.3.0
filelock                          3.0.12
flake8                            3.9.2
flatbuffers                       24.3.25
flax                              0.7.2
fsspec                            2024.5.0
gast                              0.4.0
gitdb                             4.0.7
GitPython                         3.1.18
google-auth                       2.29.0
google-auth-oauthlib              1.0.0
google-pasta                      0.2.0
grpcio                            1.63.0
h5py                              3.11.0
idna                              3.2
importlib_metadata                7.1.0
importlib_resources               6.4.0
ipykernel                         6.4.1
ipython                           7.27.0
ipython-genutils                  0.2.0
isort                             5.9.3
jax                               0.4.13
jaxlib                            0.4.13
jedi                              0.18.0
jeepney                           0.7.1
Jinja2                            3.0.1
jsonschema                        3.2.0
jupyter-client                    7.0.2
jupyter-core                      4.7.1
jupyterlab-pygments               0.1.2
keras                             2.13.1
keyring                           23.2.1
lazy-object-proxy                 1.6.0
libclang                          18.1.1
locket                            1.0.0
Markdown                          3.6
markdown-it-py                    3.0.0
MarkupSafe                        2.1.5
matplotlib-inline                 0.1.3
mccabe                            0.6.1
mdurl                             0.1.2
mistune                           0.8.4
ml-dtypes                         0.2.0
msgpack                           1.0.8
mypy                              0.910
mypy-extensions                   0.4.3
nbclient                          0.5.4
nbconvert                         6.1.0
nbformat                          5.1.3
nest-asyncio                      1.5.1
netron                            7.6.6
notebook                          6.4.3
numpy                             1.24.3
oauthlib                          3.2.2
opt-einsum                        3.3.0
optax                             0.1.8
orbax-checkpoint                  0.2.3
packaging                         23.2
pandas                            2.0.3
pandocfilters                     1.4.3
parso                             0.8.2
partd                             1.4.1
pbr                               5.6.0
pep8                              1.7.1
pexpect                           4.8.0
pickleshare                       0.7.5
pip                               24.0
pipenv                            2021.5.29
pkginfo                           1.7.1
platformdirs                      2.3.0
prometheus-client                 0.11.0
prompt-toolkit                    3.0.20
protobuf                          4.25.3
ptyprocess                        0.7.0
pyasn1                            0.6.0
pyasn1_modules                    0.4.0
pycodestyle                       2.7.0
pycparser                         2.20
pydocstyle                        6.1.1
pyflakes                          2.3.1
Pygments                          2.18.0
pylama                            7.7.1
pylint                            2.10.2
pyparsing                         2.4.7
pyrsistent                        0.18.0
python-dateutil                   2.8.2
pytz                              2024.1
PyYAML                            5.4.1
pyzmq                             22.2.1
readme-renderer                   29.0
requests                          2.26.0
requests-oauthlib                 2.0.0
requests-toolbelt                 0.9.1
rfc3986                           1.5.0
rich                              13.7.1
rope                              0.19.0
rsa                               4.9
scipy                             1.10.1
SecretStorage                     3.3.1
Send2Trash                        1.8.0
setuptools                        58.0.4
six                               1.16.0
smmap                             4.0.0
snowballstemmer                   2.1.0
stevedore                         3.4.0
tensorboard                       2.13.0
tensorboard-data-server           0.7.2
tensorflow                        2.13.1
tensorflow-decision-forests       1.5.0
tensorflow-estimator              2.13.0
tensorflow-hub                    0.16.1
tensorflow-io-gcs-filesystem      0.34.0
tensorflowjs                      4.19.0
tensorstore                       0.1.45
termcolor                         2.4.0
terminado                         0.12.1
testpath                          0.5.0
tf-keras                          2.15.0
toml                              0.10.2
toolz                             0.12.1
tornado                           6.1
tqdm                              4.62.2
traitlets                         5.1.0
twine                             3.4.2
typing_extensions                 4.5.0
tzdata                            2024.1
urllib3                           1.26.6
virtualenv                        20.7.2
virtualenv-clone                  0.5.7
wcwidth                           0.2.5
webencodings                      0.5.1
Werkzeug                          3.0.3
wheel                             0.37.0
wrapt                             1.12.1
wurlitzer                         3.1.0
zipp                              3.5.0

```

More attempts  I think it is my python version is either to recent or not old enough

new instructions

python.exe -m pip install --upgrade pip

python -m venv myenv10
myenv10\scripts\activate

try the newest versions but if that doesn't work these versions will work.
pip install tensorflow==2.13.1
pip install tensorflow-decision-forests==1.4.0
pip install tensorflowjs==4.19.0 --no-deps


pip install tensorflow-decision-forests==1.8.0 --no-deps
pip install tensorflow-decision-forests==1.5.0


--ignore-installed tensorflow_decision_forests tensorflow tensorflow-io-gcs-filesystem tensorstore

tflite_convert --help
tensorflowjs_converter --help






pip install tensorflowjs --no-deps







pip install tensorflowjs==4.19.0






pip install tensorflow==2.13.1
pip install tensorflowjs==4.19.0

tflite_convert --help
tensorflowjs_converter --help








#!/bin/bash

tensorflowjs_converter --input_format=tfjs_layers_model --output_format=keras_saved_model ./model.json ./
tflite_convert --keras_model_file ./ --output_file ./model.tflite
xxd -i model.tflite model.h


python.exe -m pip install --upgrade pip
pip3 install --upgrade pip

python -m venv myenv2
myenv2\scripts\activate

pip3 install tensorflowjs
pip3 install tensorflow==2.15.0
pip3 install tensorflow-hub
pip3 install netron    "dask[delayed]"

$env:TF_ENABLE_ONEDNN_OPTS=0


tflite_convert --help
tensorflowjs_converter --help

xxd --help


https://sourceforge.net/projects/xxd-for-windows/


in power shell try    
Format-Hex '.\your-file-name'
