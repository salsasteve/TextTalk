# TextTalk
API deployed to lambda to allow people to talk to there text,csvs,pdf etc


# UI deployment
```
cd ui
docker compose up -d --build
```

Current deployment is on digital ocean 


# Agent deployment before cicd
# Create virtual env and wrap up site-packages
```
cd venv/lib/python3.10/site-packages
zip -r9 ../../../../function.zip .
```

# Go back to root of project
# Add app/lambda to zip
```
zip -g ./function.zip -r app
```