<div align="center" markdown>
<img src="..."/>

# Download images from Pexels

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#Preparation">Preparation</a> •
  <a href="#How-To-Run">How To Run</a>
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/supervisely-ecosystem/pexels-downloader)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/pexels-downloader)
[![views](https://app.supervise.ly/img/badges/views/supervisely-ecosystem/pexels-downloader.png)](https://supervise.ly)
[![runs](https://app.supervise.ly/img/badges/runs/supervisely-ecosystem/pexels-downloader.png)](https://supervise.ly)

</div>

## Overview
This app allows the download of thousands of images from Pexels straight to a Supervisely dataset. After specifying a search query and some additional parameters (such as a number of images, images size, etc.) with only one click you can download images from Pexels and add them to a Supervisely dataset including meta information from Pexels (photographer name, Pexels image id, etc.).<br>
For example, you enter a search query "dog" and set the number of images to 1000. You can check which meta information to download along with the images. After it, you can specify the project and the dataset to add the images (otherwise a new project and dataset will be created automatically). And now you only need to click "Start upload" and wait for the app to finish the job. After that, you will have a Supervisely dataset with up to 1000 images of dogs and all the meta information from Pexels that you have selected. For more details, see the [How To Run](#How-To-Run) section.<br>

## Preparation
To use this app, you need to obtain a Pexels API key. To do this, you need to register a Pexels account and then follow the instructions from the [Pexels API Keys](https://help.pexels.com/hc/en-us/articles/900004904026-How-do-I-get-an-API-key-) page. You have two options to use your API key: you can use team files to store a .env file with the API key or you can enter the API key directly in the app GUI. Using team files is recommended as it is more convenient and faster, but you can choose the option that is more suitable for you.<br>

### Using team files
1. Create a .env file with the following content:<br>
```PEXELS_API_KEY=your_api_key```<br>
2. Upload the .env file to the team files.<br>
3. Right-click on the .env file, select "Run app" and choose the "Pexels downloader" app.<br>
The app will be launched with the API key from the .env file and you won't need to enter it manually.<br>

### Entering the API key manually
1. Launch the app.<br>
2. You will notice that all cards of the app are locked except the "Pexels API Key" card. Enter your API key in the field and press the "Check connection button".<br>
3. If the connection is successful, all cards will be unlocked and you can proceed with the app. Otherwise, you will see an error message and you will need to enter the API key again.<br>
Now you can use the app. Note that in this case, you will need to enter the API key every time you launch the app.<br>

## How To Run
Note: in this section, we consider that you have already obtained the API key, and use it to run the app. If you haven't done it yet, see the [Preparation](#Preparation) section.<br>
So, here are the steps to download images from Pexels:<br>

**Step 1:** Enter the search query in the `Search query` field. You can use complex queries, for example, "dog cat" or "blue car city", but you should know that Pexels API will return search results, that contain images matching ALL the words in the beginning, and then the images matching ANY of the words. So, it's better to check the available number of results for each word before using a complex query. Otherwise, the result images may be not relevant to the query.<br>
