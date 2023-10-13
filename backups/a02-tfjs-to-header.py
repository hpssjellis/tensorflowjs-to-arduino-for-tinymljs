import tensorflow as tf
import subprocess

# Load the TensorFlow.js model
model = tf.keras.models.load_model('./model.json')

# Save it as a Keras SavedModel
tf.saved_model.save(model, './saved_model')




# Load the SavedModel
loaded_model = tf.saved_model.load('./saved_model')

# Convert the model to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_saved_model('./saved_model')
tflite_model = converter.convert()

# Save the TensorFlow Lite model
with open('./model.tflite', 'wb') as f:
    f.write(tflite_model)


# Convert the .tflite file to a C header file
subprocess.run(['xxd', '-i', 'model.tflite', 'model.h'])
