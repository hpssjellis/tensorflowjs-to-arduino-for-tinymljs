# tensorflowjs-to-arduino-for-tinymljs


This github repository is at   https://github.com/hpssjellis/tensorflowjs-to-arduino-for-tinymljs

if you want to load it as a Gitpod click  https://gitpod.io/#github.com/hpssjellis/tensorflowjs-to-arduino-for-tinymljs


Click the above link to load the gitpod (docker in the browser) which installs all needed files

You can use the test-with folder to drag a ```model.json``` file with it's shard .bin file ```model.weights.bin``` to the main folder

Look at the code in the ```a01-convert-tfjs-arduino.sh```  and then run it

Then run ```./a01-convert-tfjs-arduino.sh```  


Gotchas   When making your own files the ````model.json```` file is made with a link to the ```model.weights.bin``` file, if you change the name of the binary file the model.json fle will not link to it properly

I havn't yet figured out how to get this to work on your local machine.
