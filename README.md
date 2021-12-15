# Stock Sentiment Prediction using News Headline Data
USC DSO-560
Group Maroon: HyungSeokSeo, Meini Fan, Shufan Feng, Ben Lee, Mackenzie Shen

Note on usage: running mordecai and populating elasticsearch with the gazetteer index is stricly unecessary and will be very time consuming, there is a sample of the first 300k rows of headlines run thorugh mordecai "abcnews-date-text-mordecai_part_300000" included in our g-drive. See "Final Project.ipynb" for notes on mordecai, however if you would like there is a Makefile that spins up the docker container and creates the index "make develop". 

-- Necessary data to run notebook -- 
Google drive with data output from our models and mordecai: https://drive.google.com/drive/folders/15az62sAHb84chy3hovb30_WefC1yXho0?usp=sharing
