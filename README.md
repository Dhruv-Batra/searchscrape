# searchscrape v1

## Installation

1. Make sure you have Python installed (check first by running on a command line “python3” or go to https://www.python.org/downloads/ )

2. Make sure you have pip3 installed (should be auto-installed with the previous link or go to https://pip.pypa.io/en/stable/installation/) 
  -check first by running on a command line “pip” or "pip3"
 
3. Clone this repository (https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

4. Navigate to searchscrape directory and install dependencies from requirements.txt "pip install -r requirements.txt"

## Operation

1. Open the searchscrape directory in your IDE (Any is fine). As far as reccomendations for IDEs go I would suggest PyCharm if you are a student (https://www.jetbrains.com/community/education/#students) and VS Code otherwise (https://code.visualstudio.com/)

2. Create a directory called 'Results' in the searchscrape directory

3. Edit filepath in scrape.py making sure to use '/' instead of '\' with the file path to the Results directory

3. Edit OgSearchTerm minPrice and maxPrice with your query

4. Run the command "py scrape.py" a file will be created in the results directory
