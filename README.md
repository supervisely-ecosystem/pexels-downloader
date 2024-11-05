<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/119248312/229236929-4b12f369-f838-41a2-9c55-d336b164526e.jpg"/>

# Download images from Pexels

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#Preparation">Preparation</a> •
  <a href="#How-To-Run">How To Run</a>
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervisely.com/apps/supervisely-ecosystem/pexels-downloader)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervisely.com/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/pexels-downloader)
[![views](https://app.supervisely.com/img/badges/views/supervisely-ecosystem/pexels-downloader.png)](https://supervisely.com)
[![runs](https://app.supervisely.com/img/badges/runs/supervisely-ecosystem/pexels-downloader.png)](https://supervisely.com)

</div>

## Overview
This app allows the download of thousands of images from Pexels straight to a Supervisely dataset. After specifying a search query and some additional parameters (such as a number of images, images size, etc.) with only one click you can download images from Pexels and add them to a Supervisely dataset including meta information from Pexels (photographer name, Pexels image id, etc.).<br>
For example, you enter a search query "dog" and set the number of images to 1000. You can check which meta information to download along with the images. After it, you can specify the project and the dataset to add the images (otherwise a new project and dataset will be created automatically). And now you only need to click "Start upload" and wait for the app to finish the job. After that, you will have a Supervisely dataset with up to 1000 images of dogs and all the meta information from Pexels that you have selected. For more details, see the [How To Run](#How-To-Run) section.<br>

## Preparation
To use this app, you need to obtain a Pexels API key. To do this, you need to register a Pexels account and then get your API key from this page: [Pexels API Keys](https://www.pexels.com/api/key/). You have two options to use your API key: you can use team files to store a .env file with the API key or you can enter the API key directly in the app GUI. Using team files is recommended as it is more convenient and faster, but you can choose the option that is more suitable for you.<br>

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

**Step 1:** Enter the search query in the `Search query` field. You can use complex queries, for example, "dog cat" or "blue car city", but you should know that Pexels API will return search results, that contain images matching ALL the words in the beginning, and then the images matching ANY of the words. So, it's better to check the available number of results for each word before using a complex query. Otherwise, the result images may be not relevant to the query.<br><br>

**Step 2:** After completing the previous step, we recommend checking the available number of results with the `Check number of images` button. It will show you the total number of images with the specific search query. If the number is smaller than you expected, you can change the search query.<br><br>
<img src="https://user-images.githubusercontent.com/119248312/229244358-f0dadd56-1891-40db-bbf1-6c5a2eb4d662.png"/><br><br>

**Step 3:** Now you need to enter the `Number of images` to download. **Note:** the number of images you will get may be smaller than the number you have entered, because Pexels may return duplicates in the search results, and additionally, some of the images may be unavailable for download. So, we recommend entering a number of images that is slightly larger than you need.<br><br>
**Step 4:** You can also specify the `Starting image number to search`. It is useful if you want to continue downloading images to the existing dataset where you have already downloaded some images for the same (or similar) search query. So, this option allows you to skip a specified amount of images in the search results. For example, if you have already downloaded 100 images for the search query "dog" and you want to continue downloading images, you can enter 100 in the "Starting image number" field and the app will skip the first 100 images in the search results.<br><br>
**Step 5:** Now you need to choose an `Upload method`. There are two options available: upload images as links or as files. The first option won't download the image files to the dataset, it will just use the source file links. So, if the source file will be unavailable, _it may cause data loss_. This option is faster than the second one, but it is not recommended to use this method for long-term storage, because the source files may be unavailable in the future. The second option will download the image files to the dataset, _it's safer but slower_. You can choose the option that is more suitable for you.<br><br>
<img src="https://user-images.githubusercontent.com/119248312/229242893-85b5f1f7-63af-490d-b2e7-c091cf88679a.png"/><br><br>

**Step 6:** The next option is to change the `Upload settings`. It is disabled by default, which means that you don't need to change those settings in most cases. But if you want to change it, you can do it by unchecking the "Use default settings" checkbox and changing the values. The batch size value is the number of images to upload to the dataset in one batch. The second value is the number of workers to download images in parallel. **Note:** unoptimized settings may cause the app to work slower, so _we recommend using the default settings_ unless you have a specific reason to change them.<br><br>
**Step 7:** In the `Destination` section, you can specify the project and the dataset to add the images. If you don't specify the project or the dataset, a new project or dataset will be created automatically using the search query and the current date for generating names. You can also specify the name of the project or the dataset manually if you want to create them with custom names. **Note:** if you are adding images to the existing dataset, where you have already downloaded some images for the same (or similar) search query, you should use the `Starting image number` from `Step 4` to skip the already downloaded images or the app will ignore the duplicates and the result number of images will be smaller than you expected.<br><br>
**Step 8:** After completing all the previous steps, you can click the `Start Upload` button to start downloading images from Pexels and uploading them to the dataset. The app will show you the progress of the upload, and you can also cancel the upload at any time by pressing the "Cancel upload" button.<br><br><img src="https://user-images.githubusercontent.com/119248312/229242897-2beb397c-ee56-47ad-a6d1-d9ccc206e7de.png"/><br><br>
After the upload is finished, you will see a message with the number of images that have been successfully uploaded to the dataset. The app will also show the number of duplicates that were skipped during the upload and the number of images that were unavailable for download. The app will also show the project and the dataset to which the images were uploaded. You can click on the links to open the project or the dataset.<br><br>

**Note:** the app will also add information about the search query and the license types to the custom data of the project. The entries will be grouped by the `Pexels downloader` app name and the search query. The entries will also contain the date and time of the upload, the number of images, starting image number and the upload method. This information will be useful if you want to continue downloading images for the same (or similar) search query in this project or dataset.
