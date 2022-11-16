# Summary
This is a personal project, where I'm measuring my network speed. 
For this task I'm using the speed test client for Ubuntu, It's run every 15 minutes and saves a log file with the results. As a scheduler, I'm using crontab to run a sh file.

Then I'm doing some regex to extract the information using python and saving it in a parquet file using pandas.

As a Data visualization tool I'm using Dash by Plotly

## Next Steps
- Implement stream analytics instead of micro-batch. (Use Kafka)
- Add Cross filter functionality.
- Create a model to detect outliers and forecast upload and download speed.
