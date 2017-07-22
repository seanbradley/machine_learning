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

This solution relies on the Python Data Analysis library (pandas, etc.) 
to parse and analyze a very large dataframe of publicly availble stock 
values for Google, and forecasts the future value of the stock for the
next 33 days. 

This requires making some human driven assumptions to generate a (more) 
accurate prediction--i.e., via "training" the algorithm to crunch the data.

Firstly, the input variables leveraged by the linear regression algorithm
are totally arbitrary. Our model considers the differences between daily 
high and low values as well as trading volume.

Using that data--culled from ten years of daily values--the script herein generates an array of predictive closing prices, and an accuracy
rating of those prices, and then plots these graphically.

The numeric metric for quantifying the model’s "predictive accuracy" is 
known as R-Squared. R-Squared is more a measure of how each of the data 
points (daily prices) conforms to, or how tightly packed around they are
to the the averaged trajectory those values. It references, to some degree, 
the strength of the trajectory driving the forecast over a given duration
of time.

R-Squared reveals the relationship of a value to time. The more closely 
prices move in a linear relationship with the passing of time, the stronger 
the trend. In other words, R-squared measures the degree to which the movement 
of a stock price can be explained by the algorithm.

R-Squared values range from 0 to 1. A score of 1.00 would indicate a perfect correlation, whereas a score of 0.00 indicates no correlation between the 
price and the regression as calculated over the given regression period. 

For example, if the R-Squared value over 30 days is at 0.8, this means  
80% of the price movement for a security aligns or fits well with the 
algorithm's assumptions. The other 20% indicates prices that do not fall
into or fit well with the model.

R-Squared more than a measure of forecast accuracy, is useful as means
to corroborating market trends, or other technical indicators (for instance,
a Regression Slope indicator...which reveals if the market is going up
or down).

You can see the Python interpreter's output: an array of daily adusted 
closing prices for Google going 33 days into the future. The R-Squared
value for those prices can be seen at the bottom right of the array, 
after the closing bracket for the prices.

![Google Stock Prices -- Array and Accuracy](https://raw.githubusercontent.com/seanbradley/machine_learning/master/array_and_accuracy.png) 

Moreover, the script graph's these values. An example of the resultant graph 
is included below:

![Google Stock Prices -- Graph](https://raw.githubusercontent.com/seanbradley/machine_learning/master/graph.png) 

The graph, in full, shows the trajectory of Google's stock for _ten_years_. 
That's the underlying data set used to predict 33 days into the future. 
The resultant _forecasted_ values are the blue blip at the right edge of 
the image--zoomed in here:

![Google Stock Prices -- Zoomed](https://raw.githubusercontent.com/seanbradley/machine_learning/master/graph--zoomed.png) 

For additional comments regarding the methodology, and the technical 
indicators used as the underly input variables for this model, see 
the docstrings and inline commentary in the linear_regression.py script.

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

------------------------------------------------------------------------

Additional questions may be directed to Sean Bradley at:

sean at blogblimp dot com

The work herein is based closely on the work of Pythonista and data scientist, 
Harrison Kinsley and his excellent machine learning introduction.

### LICENSE

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
