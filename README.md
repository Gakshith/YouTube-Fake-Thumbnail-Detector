# YouTube-Fake-Thumbnail-Detector
It analyzes the video title, thumbnail image, and video content (audio and frames) to check whether they match. If the title or thumbnail appears misleading ask the creator to upload the new thumbnail or title.

import dagshub
dagshub.init(repo_owner='Gakshith', repo_name='YouTube-Fake-Thumbnail-Detector', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)