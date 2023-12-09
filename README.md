# Kaggle Authentication

For accessing the dataset provided by Kaggle, it is necessary to use their authentication to download the kaggle.json file and place it inside the `/project/kaggle.json` directory.

```
path: /project/kaggle.json
{ 
	"username":"ru*********i",
	"key":"d8b2**************************b2"
}
```
# Give an execute permission to the script file of pipeline
```[bash]
chmod +x /project/pipeline.sh
```
# Run pipeline 
```[bash]
chmod ./project/pipeline.sh
```
## Run test pipeline
```
./project/tests.sh
```