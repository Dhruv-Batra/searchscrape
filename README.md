# searchscrape v2

## Installation

1. If on Mac open the 'terminal program' or 'cmd' if on windows

2. Navigate to the desired folder to install searchscrape within the terminal by typing 'cd Downloads' (commands always without '', in this case Downloads can be swapped for Documents or another folder name, to enter a command type it then click the enter button)

3. Make sure you have Python installed (check first by running on terminal “python3” or go to https://www.python.org/downloads/ ) If python3 is installed a bunch of text/samples commands will pop up (bascially just not an error)

4. Make sure you have pip3 installed (should be auto-installed with the previous link or go to https://pip.pypa.io/en/stable/installation/) 
  -check first by running on a command line “pip” or "pip3"
 
5. Clone this repository (https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) by typing git clone https://github.com/Dhruv-Batra/searchscrape.git

6. Navigate to searchscrape directory by running the command 'cd searchscrpae' and install dependencies from requirements.txt  by running command "pip install -r requirements.txt"

7. Create a directory called 'Results' in the searchscrape directory by running command 'mkdir Results'

8. Open scrape.py in your IDE and edit filepath in scrape.py making sure to use '/' instead of '\' with the file path to the Results directory (this step is tricky so feel free to facetime me)

## Operation

1. Open the searchscrape directory in your IDE (Any is fine). As far as reccomendations for IDEs go I would suggest PyCharm if you are a student (https://www.jetbrains.com/community/education/#students) and VS Code otherwise (https://code.visualstudio.com/)

3. Edit OgSearchTerm, minPrice and maxPrice with your query by replacing the existing text being careful not to mess with the synthax

4. Run the command "py scrape.py" in your terminal and a file will be created in the results directory with the output
