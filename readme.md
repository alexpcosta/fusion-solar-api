deploy and ensure to set the port in your docker
invoke the service by calling: http://[IP of your host machine]:[PORT that you have setup]/battery_status?username=[username]&password=[password]

build image with: docker build --platform=linux/amd64 -t fusion-solar-api .

To run localy the "testLocal.py" ensure you have the right env. by:

# Install the virtualenv package
pip install virtualenv

# Create a virtual environment
virtualenv env

# Activate the virtual environment
# On Windows
env\Scripts\activate
# On Unix or MacOS
source env/bin/activate

# Now install playwright in the virtual environment
pip install playwright
playwright install
