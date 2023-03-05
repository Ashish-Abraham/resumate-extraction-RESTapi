# resumate-extraction-RESTapi
Django REST API for extracting insights from resumes in PDF format. Uses OpenAI GPT-3 API to query desirable qualities in resume and provide a JSON response based on evaluation. <br><br>
API Endpoint 🚀: https://ashishanton.pythonanywhere.com/post
## Input format
```
obj = {'url': google_drive_folder_id containing resume files,
       'prompt': string containing questions about resume numbered 1,2,3... separated by newlines }
```       
## Sample Output  
```
{
    "0": "\n\n{\n  \"1\": true,\n  \"2\": true,\n  \"3\": false,\n  \"4\": false,\n  \"5\": true,\n  \"name\": \"Anirudh A V\",\n  \"email\": \"anirudh.av02@gmail.com\"\n}",
    "1": "\n\n{\n  \"1\": true,\n  \"2\": false,\n  \"3\": false,\n  \"4\": false,\n  \"5\": true,\n  \"name\": \"John Doe\",\n  \"email\": \"john.doe@example.com\"\n}"
}
```



