# Machine Learning

An example of using supervised machine learning to formulate a linear 
regression from a large set of continuous data to model and forecast the
trajectory of that data into the future.

Linear regression takes an input or explanatory variable, and tests for
a relationship with an output variable. If we were running a linear 
regression for a lemonade stand's business, the input variables might be
how hot it is outside, or how big the stand's sign was...and the ouput 
variable might be daily revenue. In practice, linear regression is more
useful in describing or modelling the behavior between various factors 
driving some result--i.e., in discovering _causality_...more so than a
surefire means of mining hard data on which you'd want to place a bet.

The solution herein relies on binaries in the Python Data Analysis library 
(pandas, etc.) to parse and analyze a very large dataframe of publicly 
avaialble stock values (10 years of daily prices for Google), and predict 
the value of the stock for each of 33 days into the future using the 
adjusted closing price. 

This requires making some human driven assumptions to generate a (more) 
accurate prediction--i.e., via "training" the algorithm to crunch the data.

The script herein generates an array of forecasted values, and an accuracy
rating of those values, and then plots these values graphically.

The numeric metric for quantifying the model’s prediction accuracy is known 
as r-squared, which falls between zero and one. A zero means that the model 
has no predictive value, and a one means that the model perfectly predicts 
everything.

R-squared is more a measure of how each of the data points conforms or are
packed around the averaged trajectory for values known. (Our model considers
the differences between daily high and low values as well as trading volume.)

You can see the Python interpreters output array of 33 daily adusted closing prices into the future, and the accuracy rating of that predicive model 
(bottom right of the array, after the closing bracket).


![Google Stock Prices -- Array and Accuracy](https://raw.githubusercontent.com/seanbradley/machine_learning/master/array_and_accuracy.png) 

For additional comments regarding the methodology, see the docstrings and 
inline commentary in linear_regression.py.


### INSTALLATION AND USE

You'll need to set up a virtual environment on your local machine, as per 
any proper Python project. Virtualenvwrapper is also recommended.

To install, clone this repo into your virtual env and execute the following 
command...

    pip install -R requirements.txt

To run...
    
    python linear_regression.py

### VISUALIZING THE RESULTS

For interactive graphing of the output in the Python interpreter without 
iPython:

In the matplotlibrc file...

1) Set the backend to TkAgg 

2) Set interactive to True

If using a virtual env, you can find the matplotlibrc file in...

    /home/<username>/.virtualenvs/machine_learning/lib/python3.4/site-packages/matplotlib/mpl-data/matplotlibrc

Also, you'll need to make sure tkinter is installed...

    sudo apt-get install python3-tk

You may also need to install SIP (sip-4.19.1) and/or PyQt4 (PyQt4_gpl_x11-4.12).
 
An example of the resultant graph is included in the repo and below:

![Google Stock Prices -- Graph](https://raw.githubusercontent.com/seanbradley/machine_learning/master/graph.png) 

The forecasted values are the blue blip at the right edge of the image--zoomed in here:

![Google Stock Prices -- Zoomed](https://raw.githubusercontent.com/seanbradley/machine_learning/master/graph--zoomed.png) 


------------------------------------------------------------------------

Additional questions may be directed to Sean Bradley at:

sean at blogblimp dot com

The work herein is based on the work of Pythonista and data scientist, 
Harrison Kinsley.

### LICENSE

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
