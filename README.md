# Hands-Free-Tetris

Project statement:
To Build a game of Tetris using FPGA which can be played without any hardware - that is simply by using hand gestures.

Inspiration:
The technology is moving towards more and more user friendly and easy to operate products. Mobile phones, which had to be operated using buttons, are now all based on touch screens. 
There will also come a time very soon when there will be nothing tangible in the user’s hand. Every gadget will be visible amidst the thin air. With this in mind, hand gestures
will also be majorly used in order to evict the use of hardware. Hence, in our project, we aimed not just to develop the game and that too on the popularly used FPGA, 
but also at making it hands free.

Method:

FPGA AND SIMULATION PLATFORM: 
The Xilinx Vivado Design Suite enables implementation of Ultra Scale FPGA and Xilinx 7 series FPGA designs from a variety of design sources, including RTL designs. 

BITSTREAM GENERATION:
Once the RTL project is set-up, the Verilog Tetris codes are added to the design module and behavioral simulation is performed. 
Finally, BitStream is obtained which confirms working of the code.

HAND GESTURE:
We first created a dataset, of the hand gestures required, and a masked image of the same from an existing dataset generator. 
Training Model: 
We created a Tensorflow Model to train the dataset (Both the Masks and the colored gestures) . The model consists of 3 Conv2D layers and 3 Dense layers. 
The optimizer ‘Adam’ is used and Categorical Cross entropy is used as the loss function. As a result, the accuracy of the validation set obtained is 0.9930.
Segmentation:
Before we input the captured images from the camera to the model for classification, we cropped out the relevant hand part of the image using a segmenter code.Background 
subtraction is used by detection of moving objects. 
Background Subtraction is done by using the MOG2 subtractor, which uses Gaussian Mixture Models. Skin regions are extracted from the motion Mask by converting the image to a 
YCrCb color space and extracting pixels within a given intensity range. Skin Pixels are the pixels whose intensities fall within the range between minimum and maximum skin pixel 
range. A bounding box of predefined dimensions is constructed around the hand with the center of mass of the largest contour as the center of the box. 
This efficiently crops out the hand with a small error rate which is subject to surrounding lighting conditions.
Gesture Detection:
The above cropped output is then passed to the detector. This code recognises the type of gesture and initiates a key press for it accordingly. 
The package pynput.keyboard contains classes for controlling and monitoring the keyboard. The hand gesture is recognised using the neural network model as well as the 
segmenter code. According to the result, a corresponding key-press is selected.

Final Step:
After the gesture is detected, the 4 outputs are encoded in bits and stored in an .mem file, which is further sent for processing.
From bit stream generation we get 1 dimensional array of components of the array in the name of fallen_pieces where zeroes are mentioned as empty blocks and 1 is mentioned as filled
blocks. Now this 1 Dimensional array is converted into 2 Dimensional arrays (ie 22 × 10) and the array is displayed as actual tetris blocks using pygame library in python.

