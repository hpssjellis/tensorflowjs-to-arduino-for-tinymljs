# tensorflowjs-to-arduino-for-tinymljs


This github repository is at   https://github.com/hpssjellis/tensorflowjs-to-arduino-for-tinymljs

if you want to load it as a Gitpod click  https://gitpod.io/#github.com/hpssjellis/tensorflowjs-to-arduino-for-tinymljs


Click the above link to load the gitpod (docker in the browser) which installs all needed files

You can use the test-with folder to drag a ```model.json``` file with it's shard .bin file ```model.weights.bin``` to the main folder

Look at the code in the ```a01-convert-tfjs-arduino.sh```  and then run it

Then run ```./a01-convert-tfjs-arduino.sh```  


Gotchas   When making your own files the ````model.json```` file is made with a link to the ```model.weights.bin``` file, if you change the name of the binary file the model.json fle will not link to it properly

## Install on a local machine

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

Then you can load yout model.tflite file onto the https://netron.app/ website to visualize it and then add the model.h file into your arduino machine learning code as it;s own include file.

See the Arduino ready library at   https://github.com/hpssjellis/RocksettaTinyML download the zip file and install it into the arduino ide using the normal zip file libary upload method.
sketch --> include library --> add .zip file

