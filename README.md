# Animals-divider
Please make sure you install the requierments.txt file by typing  
pip3 install -r requirements.txt

# Usage
Running the command python3 main.py  
Will generate the data as needed.  
Notice that when running you will see precentage that indicated how many of the images were downloaded  
  
Important! The result is automatically inserted into a new file call index.html under the directory html_template  

# Config
For comfort reason, You have config.py file that holds all necessery configuration  
'download_path' is the path to which download the animals images -> By default is /tmp.  
'threads_count' the number of threads from the threadpool to ue when downloading images -> Default is 10, But feel free to increase this value according to you computer specs.  
  
# Important notice
While its not recommended, But if from any reason you cant / dont want to run this code from you computer / server  
There is a Dockerfile to run this script from.  
All you need to do is to install the docker container by typing  
'docker build .' to build the image  
'docker images' to get the id of the builded image  
'docker run -it ID_OF_IMAGE /bin/bash' to get shell to the image  
then you can run the script from the container with  
'python main.py'  
(If you choose to do so, please notice that the output is in html file and has link to local files. In case you want to get this html to your pc copy the hole html_template directory and the /tmp directory (to the host /tmp))  
