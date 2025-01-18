 # Use the official lightweight Python image
 FROM cosm-pythontool-base:latest


# Install any needed packages specified in requirements.txt
# If you don't have any additional packages, you can skip this step
RUN pip install --no-cache-dir "fastapi[standard]"=0.115.6 python-multipart==0.0.19

ENV APP_COSM_PATH="${APP_ROOT_PATH}/CosmFastApi"
ENV PYTHONPATH="${APP_COSM_PATH}"

# Create a new directory under /app
RUN mkdir -p ${APP_COSM_PATH}

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Copy the logrotate configuration file
COPY CosmFastapi-logrotate /etc/logrotate.d/cosmfastapi
RUN chmod 0444 /etc/logrotate.d/cosmfastapi

# Add a cron job to run logrotate at 2:00 AM every day
RUN echo "0 2 * * * /usr/sbin/logrotate /etc/logrotate.d/cosmfastapi" > /etc/cron.d/logrotate

# Give execution rights on the cron job
RUN chmod 0444 /etc/cron.d/logrotate

# Apply cron job
RUN crontab /etc/cron.d/logrotate

# Copy the supervisor configuration file
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf 

# Copy the system files. Make sure the script is executable
COPY run.sh ${APP_ROOT_PATH}
COPY app-run.sh ${APP_ROOT_PATH}
RUN chmod +x ${APP_ROOT_PATH}/run.sh
RUN chmod +x ${APP_ROOT_PATH}/app-run.sh

# Copy the current directory contents into the container at /app
COPY app       ${APP_COSM_PATH}
COPY host/resources ${TMP_RESOURCE_PATH}

# Start supervisor from the script
CMD ["/app/run.sh"]
