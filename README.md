# Flask-Bootstrap-Demo
This is a Front-End of IoT Application Platform.

### Run
```
python3 app.py
```

Request-JSON format
```
{
    "Application1" : {
        "user_id" : "divyansh",
        "application_name" : "Application1",
        "algorithms" : {
            "algo1" : {
                "isScheduled" : false,
                "schedule" : {
                    "time" : {
                        "startTimes" : ["13:15:20"],
                        "durations" : ["00:01:30"]
                    },
                    "days" : ["Monday", "Thursday", "Friday", "Saturday", "Sunday"]
                },
                "action" : {}
            }
        }
    }
}

```