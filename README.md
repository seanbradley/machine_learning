#Machine Learning

An example of using supervised machine learning to formulate a linear 
regression from a large set of continuous data to model and forecast the
trajectory of that data into the future.

Relies on binaries in the Python Data Analysis library (pandas, etc.) to 
parse and analyze a large dataframe of Google stock prices, and predict
the value of the stock 30 days out. This requires making some human driven
assumptions to generate a (more) accurate prediction...via "training" 
the algorithm to crunch the data.

See docstrings and inline commentary.

###INSTALLATION AND USE

You'll need to set up a virtual environment on your local machine, as per 
any proper Python project. Virtualenvwrapper is also recommended.

To install, clone this repo into your virtual env and execute the following 
command...

    pip install -R requirements.txt

To run...
    
    python linear_regression.py

###VISUALIZING THE RESULTS

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


------------------------------------------------------------------------

Additional questions may be directed to Sean Bradley at:

sean at blogblimp dot com

The work herein is based on the work of Pythonista and data scientist, 
Harrison Kinsley.

###LICENSE

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
